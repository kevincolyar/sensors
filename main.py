#!/usr/bin/env python3

import logging
import dotenv
from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse
from fastapi_versioning import VersionedFastAPI, version
from pydantic import BaseModel
from typing import List

import exception_formatter
import sensors.commands as commands

# Initialization
# -----------------------------------------------------------------------------
dotenv.load_dotenv()

logger = logging.getLogger(__name__)
app = FastAPI()
db = commands.init_db()

# Types
# -----------------------------------------------------------------------------
class MeasurementRequest(BaseModel):
    data: str = None

class MeasurementResponse(BaseModel):
    overtemp: bool
    device_id: int
    formatted_time: str # TODO: provide format %Y/%m/%d %H:%M:%S

# Routes
# -----------------------------------------------------------------------------
@version(1)
@app.post("/temp")
@app.post("/measurement", response_model=MeasurementResponse)
async def measurement(
        measurement: MeasurementRequest,
        request: Request
):
    """
    Create a measurement record using the following format:

    - `{"data": __data_string__}`
    - where `__data_string__` is format:
    - `__device_id__:__epoch_ms__:__type__:__value__`, where:
      - `__device_id__` is the device ID (int32)
      - `__epoch_ms__` is the timestamp in EpochMS (int64)
      - `__type__` is the measurement type (string)
      - `__value__` is the value (float64)

    - __Note:__ Only measurement type of `'Temperature'` is supported at this time.

    - Example `{"data": "365951380:1640995229697:'Temperature':58.48256793121914"}`
    """
    try:
        return commands.save_measurement(db, measurement.data)

    except (ValueError, OverflowError, KeyError):
        logger.error(exception_formatter.format())

        commands.save_error(db, request.url._url, 'POST', measurement.data)

        return JSONResponse(
            status_code=400,
            content={'error': 'bad request'}
        )

@version(1)
@app.get("/errors", response_model=List[str])
async def get_errors():
    """
    Returns all data strings which have not been in the correct format.
    """
    return commands.get_errors(db)

@version(1)
@app.delete("/errors")
async def delete_errors():
    """
    Clears the error history.
    """
    commands.destroy_errors(db)
    return 'Errors cleared'

app = VersionedFastAPI(app, version_format='{major}', prefix_format='/v{major}')

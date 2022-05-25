#!/usr/bin/env python3

import logging
import dotenv
from fastapi import FastAPI, Query, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

import commands
import responses
from exception_formatter import format_exception
from pipeline import augment_state, parse_data


# Initialization
# -----------------------------------------------------------------------------
dotenv.load_dotenv()

logger = logging.getLogger(__name__)
app = FastAPI()
db = commands.init_db()

# Request Body
# -----------------------------------------------------------------------------
class Measurement(BaseModel):
    data: str

# Routes
# -----------------------------------------------------------------------------

@app.post("/temp")
@app.post("/measurement")
async def measurement(measurement: Measurement, request: Request):
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
    logger.debug("POST /measurement")
    try:
        state = parse_data(measurement.data)
        state = augment_state(state)

        commands.save_measurement(db, state)

        return responses.dispatch(state['measurement'])(state)

    except:
       logger.fatal(format_exception())

       commands.save_error(db, request.url._url, 'POST', measurement.data)

       return JSONResponse(
           status_code=400,
           content={'error': 'bad request'}
       )

@app.get("/errors", response_model=List[str])
async def get_errors():
    """
    Returns all data strings which have not been in the correct format.
    """
    logger.debug("GET /errors")
    return commands.get_errors(db)

@app.delete("/errors")
async def delete_errors():
    """
    Clears the error history.
    """
    logger.debug("DELETE /errors")
    commands.destroy_errors(db)
    return 'Errors cleared'

#!/usr/bin/env python3

import logging
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from exception_formatter import format_exception
from pipeline import augment_state, parse_data, temp_response

logger = logging.getLogger(__name__)

app = FastAPI()

# Response Map
# Contains measurement type and its responder
response_map = {
    'Temperature': temp_response
}

# Request Bodies
# -----------------------------------------------------------------------------
class Measurement(BaseModel):
    data: str

# POST endpoints
# -----------------------------------------------------------------------------
# Device Temperature
@app.post("/temp")
async def measurement(measurement: Measurement):
    try:
        # Parse
        state = augment_state(parse_data(measurement.data))

        # TODO: Persist measurement
        return response_map[state['measurement']](state)

    except:
       logger.fatal(format_exception())

       # TODO: Persist error
       return JSONResponse(
           status_code=400,
           content={'error': 'bad request'}
       )

# GET endpoints
# -----------------------------------------------------------------------------
@app.get("/errors")
async def get_errors():
    logger.debug("GET /errors")
    return {}

# DELETE endpoints
# -----------------------------------------------------------------------------
@app.delete("/errors")
async def delete_errors():
    return {}


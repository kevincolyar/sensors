#!/usr/bin/env python3

import logging

from fastapi import FastAPI, Query

logger = logging.getLogger(__name__)

app = FastAPI()

# POST endpoints
# -----------------------------------------------------------------------------
# Device Temperature
@app.post("/temp")
async def measurement(measurement: Measurement):
    logger.debug("GET /temp")
    return {}

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


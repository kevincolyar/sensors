#!/usr/bin/env python3

import os
import db.postgres.client
import sensors.responses as responses
import sensors.measurements as measurements

def init_db():
    """
    Initializes datatabase. Assumes env vars (POSTGRES_*) in .env file.
    """
    return db.postgres.client.Client(
        host     = os.environ.get('POSTGRES_HOST'),
        port     = os.environ.get('POSTGRES_PORT'),
        user     = os.environ.get('POSTGRES_USER'),
        password = os.environ.get('POSTGRES_PASSWORD'),
        database = os.environ.get('POSTGRES_DATABASE')
    )

def get_errors(db):
    """
    Returns current list of error payloads.
    """
    return [fields[0] for fields in db.select("SELECT payload FROM errors")]

def destroy_errors(db):
    """
    Clears all errors.
    """
    db.execute('DELETE from errors')

def save_measurement(db, data):
    """
    Processes data string for measurement, saves it to the database, and responds with result.
    """
    state = measurements.parse(data)
    state = measurements.augment(state)
    response = responses.dispatch(state['measurement'])(state)

    db.execute("CALL measurements_insert('{}', '{}', '{}', '{}')".format(
        state['measurement'],
        state['device_id'],
        state['value'],
        state['formatted_time']
    ))

    return response

def save_error(db, route, method, err, maxlen=255):
    """
    Saves malformed API request.
    """
    db.execute("CALL errors_insert('{}', '{}', '{}')".format(
        route,
        method,
        (err or '').replace("'", "''")[0:maxlen] # Escape single quote and limit length to `maxlen`
    ))

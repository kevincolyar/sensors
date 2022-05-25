#!/usr/bin/env python3

import os
import db.postgres.client

def init_db():
    return db.postgres.client.Client(
        host     = os.environ.get('POSTGRES_HOST'),
        port     = os.environ.get('POSTGRES_PORT'),
        user     = os.environ.get('POSTGRES_USER'),
        password = os.environ.get('POSTGRES_PASSWORD'),
        database = os.environ.get('POSTGRES_DATABASE')
    )

def get_errors(db):
    return [ fields[0] for fields in db.select("SELECT payload FROM errors") ]

def destroy_errors(db):
    db.execute('DELETE from errors')

def save_measurement(db, state):
    db.execute("CALL measurements_insert('temperature', '{}', '{}', '{}')".format(
        state['device_id'],
        state['value'],
        state['formatted_time']
    ))

def save_error(db, route, method, err):
    db.execute("CALL errors_insert('{}', '{}', '{}')".format(
        route,
        method,
        err.replace("'", "''")[0:255] # Escape single quote and limit length to 255
    ))

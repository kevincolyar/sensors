#!/usr/bin/env python3

def dispatch(measurement):
    """
    Returns response function based on measurement type.
    """
    return {
        'Temperature': temperature
    }[measurement]

def temperature(state, threshold=90):
    """
    Returns hashmap based on status of temperature.
    """
    if state['value'] >= threshold:
        return {
            'overtemp': True,
            'device_id': state['device_id'],
            'formatted_time': state['formatted_time']
        }
    else:
        return {'overtemp': False}

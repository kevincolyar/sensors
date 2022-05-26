#!/usr/bin/env python3
import datetime
import numpy as np

def parse(data, delim=':'):
    """
    Parses data string into `state` hashmap containing the following:
      - `__device_id__` is the device ID (int32)
      - `__epoch_ms__` is the timestamp in EpochMS (int64)
      - `__type__` is the measurement type (string)
      - `__value__` is the value (float64)
    """
    if data is None:
        raise ValueError("data is None")

    split = data.split(delim)

    if len(split) != 4:
        raise ValueError("Wrong number of fields")

    device_id   = int(split[0])
    epoch_ms    = int(split[1])
    measurement = split[2].strip(' \'\"')
    value       = float(split[3])

    # Use numpy to raise any type errors.
    # Don't like this; Would be easier in Rust.
    if device_id != np.int32(device_id):
        raise ValueError("device_id is not int32")

    if epoch_ms != np.int64(epoch_ms):
        raise ValueError("epoch_ms is not int64")

    if value != np.float64(value):
        raise ValueError("value is not float64")

    if value == float('-inf') or value == float('inf'):
        raise ValueError("value is out of range")

    return {
        'device_id':   device_id,
        'epoch_ms':    epoch_ms,
        'measurement': measurement,
        'value':       value
    }

def augment(state, fmt='%Y/%m/%d %H:%M:%S'):
    """
    Adds `formatted_time` datetime string in UTC to state hashmap.
    """
    ms = state['epoch_ms'] / 1000
    t = datetime.datetime.fromtimestamp(ms, tz=datetime.timezone.utc)
    state['formatted_time'] = t.strftime(fmt)

    return state

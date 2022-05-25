#!/usr/bin/env python3
import datetime
import numpy as np

def parse_data(data, delim=':'):
    """
    Parses data string into `state` hashmap containing the following:
      - `__device_id__` is the device ID (int32)
      - `__epoch_ms__` is the timestamp in EpochMS (int64)
      - `__type__` is the measurement type (string)
      - `__value__` is the value (float64)
    """
    split = data.split(delim)

    if len(split) != 4:
        raise Exception("Wrong number of fields")

    # Use np.uint32 to raise any type errors.
    # Don't like this; Would be easier in Rust.
    device_id   = int(np.uint32(split[0]))
    epoch_ms    = int(np.uint64(split[1]))
    measurement = split[2].strip(' \'\"')
    value       = float(np.float64(split[3]))

    return {
        'device_id':   device_id,
        'epoch_ms':    epoch_ms,
        'measurement': measurement,
        'value':       value
    }

def augment_state(state, fmt='%Y/%m/%d %H:%M:%S'):
    """
    Adds `formatted_time` datetime string in UTC to state hashmap.
    """
    ms = state['epoch_ms'] / 1000
    t = datetime.datetime.fromtimestamp(ms, tz=datetime.timezone.utc)
    state['formatted_time'] = t.strftime(fmt)

    return state


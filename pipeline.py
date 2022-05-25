#!/usr/bin/env python3
import logging
import datetime
import numpy as np

logger = logging.getLogger(__name__)

def parse_data(data, delim=':'):
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
    # Add formatted_time datetime string in UTC
    ms = state['epoch_ms'] / 1000
    t = datetime.datetime.fromtimestamp(ms, tz=datetime.timezone.utc)
    state['formatted_time'] = t.strftime(fmt)

    return state


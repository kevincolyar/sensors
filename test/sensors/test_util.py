#!/usr/bin/env python3

import pytest
import numpy as np
from sensors.util import parse_data, augment_state

def test_parse_data():
    assert parse_data(
        "365951380:1640995229697:'Temperature':58.48256793121914"
    ) == {
        'device_id': 365951380,
        'epoch_ms': 1640995229697,
        'measurement': 'Temperature',
        'value': 58.48256793121914
    }

def test_parse_data_bad_device_id_1():
    with pytest.raises(ValueError):
        parse_data(
            ":1640995229697:'Temperature':58.48256793121914"
        )

def test_parse_data_bad_device_id_2():
    with pytest.raises(ValueError):
        parse_data(
            "foo:1640995229697:'Temperature':58.48256793121914"
        )

def test_parse_data_bad_device_id_under_min():
    with pytest.raises(ValueError):
        parse_data(
            "{}:1640995229697:'Temperature':58.48256793121914".format(np.iinfo(np.int32).min - 1)
        )

def test_parse_data_bad_device_id_over_max():
    with pytest.raises(ValueError):
        parse_data(
            "{}:1640995229697:'Temperature':58.48256793121914".format(np.iinfo(np.int32).max + 1)
        )

def test_parse_data_negative_ephoch_ms():
    assert parse_data(
        "365951380:-1640995229697:'Temperature':58.48256793121914"
    ) == {
        'device_id': 365951380,
        'epoch_ms': -1640995229697,
        'measurement': 'Temperature',
        'value': 58.48256793121914
    }

def test_parse_data_bad_epoch_ms_1():
    with pytest.raises(ValueError):
        parse_data(
            "365951380::'Temperature':58.48256793121914"
        )

def test_parse_data_bad_epoch_ms_2():
    with pytest.raises(ValueError):
        parse_data(
            "365951380:foo:'Temperature':58.48256793121914"
        )

def test_parse_data_bad_epoch_ms_3():
    with pytest.raises(OverflowError):
        parse_data(
            "365951380:{}:'Temperature':58.48256793121914".format(np.iinfo(np.int64).min - 1)
        )

def test_parse_data_bad_epoch_ms_4():
    with pytest.raises(OverflowError):
        parse_data(
            "365951380:{}:'Temperature':58.48256793121914".format(np.iinfo(np.int64).max + 1)
        )


def test_parse_data_bad_value_1():
    with pytest.raises(ValueError):
        parse_data(
            "365951380:1640995229697:'Temperature':"
        )

def test_parse_data_bad_value_2():
    with pytest.raises(ValueError):
        parse_data(
            "365951380:1640995229697:'Temperature':foo"
        )

def test_parse_data_bad_value_3():
    with pytest.raises(ValueError):
        parse_data(
            "365951380:1640995229697:'Temperature':-1e1000"
        )

def test_parse_data_bad_value_4():
    with pytest.raises(ValueError):
        parse_data(
            "365951380:1640995229697:'Temperature':1e1000"
        )

def test_augment_data():
    assert augment_state({
        'epoch_ms': 1653428445377
    }) == {
        'epoch_ms': 1653428445377,
        'formatted_time': '2022/05/24 21:40:45'
    }

    assert augment_state({
        'epoch_ms': -1653428445377
    }) == {
        'epoch_ms': -1653428445377,
        'formatted_time': '1917/08/10 02:19:14'
    }

#!/usr/bin/env python3

import pytest
import numpy as np
from sensors.measurements import parse, augment

def test_parse():
    assert parse(
        "365951380:1640995229697:'Temperature':58.48256793121914"
    ) == {
        'device_id': 365951380,
        'epoch_ms': 1640995229697,
        'measurement': 'Temperature',
        'value': 58.48256793121914
    }

def test_parse_bad_device_id_1():
    with pytest.raises(ValueError):
        parse(
            ":1640995229697:'Temperature':58.48256793121914"
        )

def test_parse_bad_device_id_2():
    with pytest.raises(ValueError):
        parse(
            "foo:1640995229697:'Temperature':58.48256793121914"
        )

def test_parse_bad_device_id_under_min():
    with pytest.raises(ValueError):
        parse(
            "{}:1640995229697:'Temperature':58.48256793121914".format(np.iinfo(np.int32).min - 1)
        )

def test_parse_bad_device_id_over_max():
    with pytest.raises(ValueError):
        parse(
            "{}:1640995229697:'Temperature':58.48256793121914".format(np.iinfo(np.int32).max + 1)
        )

def test_parse_negative_ephoch_ms():
    assert parse(
        "365951380:-1640995229697:'Temperature':58.48256793121914"
    ) == {
        'device_id': 365951380,
        'epoch_ms': -1640995229697,
        'measurement': 'Temperature',
        'value': 58.48256793121914
    }

def test_parse_bad_epoch_ms_1():
    with pytest.raises(ValueError):
        parse(
            "365951380::'Temperature':58.48256793121914"
        )

def test_parse_bad_epoch_ms_2():
    with pytest.raises(ValueError):
        parse(
            "365951380:foo:'Temperature':58.48256793121914"
        )

def test_parse_bad_epoch_ms_3():
    with pytest.raises(OverflowError):
        parse(
            "365951380:{}:'Temperature':58.48256793121914".format(np.iinfo(np.int64).min - 1)
        )

def test_parse_bad_epoch_ms_4():
    with pytest.raises(OverflowError):
        parse(
            "365951380:{}:'Temperature':58.48256793121914".format(np.iinfo(np.int64).max + 1)
        )


def test_parse_bad_value_1():
    with pytest.raises(ValueError):
        parse(
            "365951380:1640995229697:'Temperature':"
        )

def test_parse_bad_value_2():
    with pytest.raises(ValueError):
        parse(
            "365951380:1640995229697:'Temperature':foo"
        )

def test_parse_bad_value_3():
    with pytest.raises(ValueError):
        parse(
            "365951380:1640995229697:'Temperature':-1e1000"
        )

def test_parse_bad_value_4():
    with pytest.raises(ValueError):
        parse(
            "365951380:1640995229697:'Temperature':1e1000"
        )

def test_augment():
    assert augment({
        'epoch_ms': 1653428445377
    }) == {
        'epoch_ms': 1653428445377,
        'formatted_time': '2022/05/24 21:40:45'
    }

    assert augment({
        'epoch_ms': -1653428445377
    }) == {
        'epoch_ms': -1653428445377,
        'formatted_time': '1917/08/10 02:19:14'
    }

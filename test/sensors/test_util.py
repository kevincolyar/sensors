#!/usr/bin/env python3

import pytest
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
            "-1:1640995229697:'Temperature':58.48256793121914"
        )

def test_parse_data_bad_device_id_3():
    with pytest.raises(ValueError):
        parse_data(
            "foo:1640995229697:'Temperature':58.48256793121914"
        )

def test_parse_data_bad_epoch_ms_1():
    with pytest.raises(ValueError):
        parse_data(
            "365951380::'Temperature':58.48256793121914"
        )

def test_parse_data_bad_epoch_ms_2():
    with pytest.raises(ValueError):
        parse_data(
            "365951380:-1:'Temperature':58.48256793121914"
        )

def test_parse_data_bad_epoch_ms_3():
    with pytest.raises(ValueError):
        parse_data(
            "365951380:foo:'Temperature':58.48256793121914"
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

def test_augment_data():
    assert augment_state({
        'epoch_ms': 1653428445377
    }) == {
        'epoch_ms': 1653428445377,
        'formatted_time': '2022/05/24 21:40:45'
    }

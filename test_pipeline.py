#!/usr/bin/env python3

import pytest
from pipeline import parse_data, temp_response, augment_state

def test_parse_data():
    assert parse_data(
        "365951380:1640995229697:'Temperature':58.48256793121914"
    ) == {
        'device_id': 365951380,
        'epoch_ms': 1640995229697,
        'measurement': 'Temperature',
        'value': 58.48256793121914
    }

def test_parse_data_bad_device_id():
    with pytest.raises(ValueError):
        parse_data(
            ":1640995229697:'Temperature':58.48256793121914"
        ) == {
            'device_id': 365951380,
            'epoch_ms': 1640995229697,
            'measurement': 'Temperature',
            'value': 58.48256793121914
        }

def test_parse_data_bad_device_id():
    with pytest.raises(ValueError):
        parse_data(
            "-1:1640995229697:'Temperature':58.48256793121914"
        ) == {
            'device_id': 365951380,
            'epoch_ms': 1640995229697,
            'measurement': 'Temperature',
            'value': 58.48256793121914
        }

def test_augment_data():
    assert augment_state({
        'epoch_ms': 1653428445377
    }) == {
        'epoch_ms': 1653428445377,
        'formatted_time': '2022/05/24 21:40:45'
    }

def test_temp_response_overtemp_false():
    assert temp_response({'value': 89}) == {
        'overtemp': False
    }

def test_temp_response_overtemp_true():
    assert temp_response({
        'device_id': 1,
        'formatted_time': '2022/5/22/24 14:27:10',
        'value': 90
    }) == {
        'overtemp': True,
        'device_id': 1,
        'formatted_time': '2022/5/22/24 14:27:10'
    }

#!/usr/bin/env python3
import responses

def test_temperature_overtemp_false():
    assert responses.temperature({'value': 89}) == {
        'overtemp': False
    }

def test_temperature_overtemp_true():
    assert responses.temperature({
        'device_id': 1,
        'formatted_time': '2022/5/22/24 14:27:10',
        'value': 90
    }) == {
        'overtemp': True,
        'device_id': 1,
        'formatted_time': '2022/5/22/24 14:27:10'
    }

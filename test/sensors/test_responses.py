#!/usr/bin/env python3

import pytest

from sensors.responses import dispatch, temperature

def test_dispatch():
    assert dispatch('Temperature')  == temperature

def test_dispatch_fail():
    with pytest.raises(KeyError):
        assert dispatch('Temp')

def test_temperature_overtemp_false():
    assert temperature({'value': 89}) == {
        'overtemp': False
    }

def test_temperature_overtemp_true():
    assert temperature({
        'device_id': 1,
        'formatted_time': '2022/5/22/24 14:27:10',
        'value': 90
    }) == {
        'overtemp': True,
        'device_id': 1,
        'formatted_time': '2022/5/22/24 14:27:10'
    }

import pytest
import sample

def test_add_int():
    assert sample.add(3, 4) == 7

def test_add_float():
    assert sample.add(2., 5.) == 7.0

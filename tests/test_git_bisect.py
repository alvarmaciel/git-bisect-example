import pytest

def test_working():
    a_number = 1
    a_number_as_string = "1"
    assert isinstance(a_number, int)
    assert isinstance(a_number_as_string, str)

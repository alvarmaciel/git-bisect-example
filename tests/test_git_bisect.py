import pytest

def test_asert_instance():
    a_number = 1
    a_string = "1"
    assert isinstance(a_number, int)
    assert isinstance(a_number_as_string, str)

def test_assert_value():
    a_number = 1
    a_string = "1"
    assert a_number == 1
    assert a_number == "1"

def test_assert_existence():
    a_number = 1
    a_string = "1"
    assert a_number
    assert a_string

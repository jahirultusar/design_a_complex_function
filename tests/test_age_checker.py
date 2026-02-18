from lib.age_checker import age_checker
import pytest

def test_returns_correct_string_input_formats():
    """Required string input format should be YYYY-MM-DD
    If input is in a different format raise an Exception"""
    with pytest.raises(ValueError, match="Incorrect date format!"):
        age_checker("2024 -12")

def test_returns_correct_string_input_formats_wrong_order():
    """Required string input format should be YYYY-MM-DD
    If input is in a different format raise an Exception"""
    with pytest.raises(ValueError, match="Incorrect date format!"):
        age_checker("12-2024-01")

def test_returns_access_denied():
    """Check if age is < 16
    Return "Access Denied"""
    assert age_checker("2021-01-01") == "Too young to enter. Access denied!"

def test_returns_access_granted():
    """Check if age is > 16
    Return "Access Granted"""
    assert age_checker("1986-01-01") == "Welcome to the club!"

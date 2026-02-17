from lib.age_checker import age_checker
import pytest

"""
Required string input format should be YYYY-MM-DD
If input is in a different format raise an Exception
"""
def test_with_invalid_date_format():
    with pytest.raises(ValueError):
        age_checker("2021-12")

"""
Check if age is => 16
Return "Access Granted"
"""

def test_with_age_of_over_16():
    input_dob = age_checker("2003-12-02")
    assert input_dob == "Access granted!"


"""
Check if age is < 16
Return "Access Denied"
"""

def test_with_age_of_under_16():
    input_dob = age_checker("2021-12-02")
    assert input_dob == (f"Access denied. You are 4 years old, but must be at least 16.")


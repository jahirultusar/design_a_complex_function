from lib.age_checker import age_checker
import pytest

"""
Required string input format should be YYYY-MM-DD
If input is in a different format raise an Exception
"""
def test_returns_formatted_dob():
    with pytest.raises(Exception) as err:
        dob1 = age_checker("2012-02")
    assert str(err.value) == "Incorrect DOB format"


"""
Check if age is => 16
Return "Access Granted"
"""

"""
Check if age is < 16
Return "Access Denied"
"""
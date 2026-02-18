
# will try to solve age check with datetime module 
    # datetime module
        # - will check correct user input/format  
        # - will check todays date
        # - will calculate the age with .year method
# then return message to user if access is granted or denied 

import datetime
from dateutil.relativedelta import relativedelta

def age_checker(user_dob):
    """checks dob in correct format and 
    returns access message"""
    try:
        formatted_dob = datetime.datetime.strptime(user_dob, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Incorrect date format!")
    today = datetime.datetime.today()
    age = relativedelta(today, formatted_dob).years

    if age < 16:
        return "Too young to enter. Access denied!"
    else: 
        return "Welcome to the club!"

from datetime import datetime, date
from dateutil.relativedelta import relativedelta
# Dateutil will be squiggly - to install dateutil, please run the below:
# pip install python-dateutil      

def age_checker(dob_str):
    """
    Checks if someone is at least 16 years old based on their date of birth.
    
    Args:
        dob_str (str): Date of birth in 'YYYY-MM-DD' format
    
    Returns:
        str: Access message
    """
    
    # Convert the string to a datetime object using datetime
    dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
    
    # Get today's date
    today = date.today()
    # print(dob)
    # print(today)

    # Calculate age using dateutil.relativedelta
    age = relativedelta(today, dob).years
    # print(age)

    # Check age
    if age < 16:
        print(f"Access denied. You are {age} years old, but must be at least 16.")
    else:
        print("Access granted!")
    
age_checker("2003-12-02")
age_checker("2021-12-02")
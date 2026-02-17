# Age Checker Recipe

## User story
>_As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`._

>_As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16)._

>_As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted._

## Function Design

Basic structure of the function:

``` python
def age_checker(dob_str):
    """
    Checks if someone is at least 16 years old based on their date of birth.
    
    Args:
        dob_str (str): Date of birth in 'YYYY-MM-DD' format
    
    Returns:
        str: Access message
    """

    # Convert the string to a datetime object using datetime
    # (add code here)

    # Get today's date
    # (add code here)

    # Calculate age using dateutil.relativedelta
    # (add code here)

    # Check age
    # (add code here)
```

## Tests
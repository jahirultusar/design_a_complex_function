import datetime

def age_checker(date_of_birth):
    dob = date_of_birth.split("-")
    if len(dob) < 3:
        raise Exception("Incorrect DOB format")
    print(dob)

# age_checker("2003-12-02")


############### 





def age_checker(dob):
    datetime.datetime.strptime(dob, "%Y-%m-%d")











    # if date_of_birth != dob:
    #     # raise Exception("Incorrect DOB format")
    #     raise ValueError("Incorrect format")

student={
    "name": "faezeh",
    "student_id": 26821022,
    "feedback": None
}
student["last_name"] = "mobasheri"

try:
    last_name = student["last_name"]
    last_name = 3 + last_name
except KeyError:
    print("error finding last name")
except TypeError as error:
    print("string and integer cannot be added")
    print(error)



print("the code has been executed")

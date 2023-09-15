"""
Functions Assignment
- Create a function that takes in 3 parameters(firstname, lastname, age) and
    return a dictionary based on those values
"""

def user_dictionary(firstname, lastname, age) :
    created_user_dictionary = {
        "firstname" : firstname,
        "lastname" : lastname,
        "age" : age
    }

    return created_user_dictionary

solution_dictionary = user_dictionary(firstname="Amin", lastname="shahnani", age=37)
print(solution_dictionary)
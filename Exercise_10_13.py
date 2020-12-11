#Verify User:
import json
def get_stored_username():
    """Get stored username if available."""
    filename = 'Excercise_10_13.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'Excercise_10_13.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username == None:
        username = get_new_username()
    else:
        useraccept = input("Is your username is '" + str(username) + "' ?(y/n)")
        if useraccept == 'y' or useraccept == 'Y':
            print("Welcome back, " + str(username) + "!")
        else:
            username = get_new_username()   
            print("We'll remember you when you come back, " + str(username) + "!")

greet_user()
import json

# username = input('What is your name?')

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back:" + username)
    else:
        username = input("What is your name? ")
        with open(filename) as f_obj:
            json.dump(username, f_obj)
            print("has been saved")

greet_user()

def greet_user():
    """显示简单的问候语"""
    print("Hello")

greet_user()

def greet_user(username):
    print("Hello," + str(username).title() + "!")

greet_user(123)

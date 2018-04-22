def greet_users(names):
    """向列表中每位用户都发出简单的问候"""
    for name in names:
        print("Hello, " + name.title() + "!")

greet_users(['a', 'b', 'asdf', 'asdf',])


def my_decotator(f):
    print('before...')
    result = f()
    print('after...')
    return result


@my_decotator
def fuck_life():
    print('asdf')


fuck_life
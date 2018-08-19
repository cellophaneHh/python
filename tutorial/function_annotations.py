def f(ham: str, eggs: str = 'eggs') -> str:
    print(f.__annotations__)
    print(ham, eggs)
    return ham + ' and' + eggs

f('spam')
f('driver')

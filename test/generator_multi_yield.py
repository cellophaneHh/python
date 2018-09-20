'''
多个yield
'''


class MyClass:
    def __init__(self):
        print('MyClass...')


def num_generator():
    '''有两个返回的生成器'''
    yield 1000
    mc = MyClass()
    yield mc


ng = num_generator()
# 对于同一个生成器来说，每次next得到一个yield的返回值
print(next(ng))
print(next(ng))

for i in num_generator():
    print(i)

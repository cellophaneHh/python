'''
测试生成器和yield
'''


def simple_generator_function():
    print('1--')
    yield 1
    print('2---')
    yield 2
    print('3---')
    yield 3


for value in simple_generator_function():
    print(value)


our_generator = simple_generator_function()
print(next(our_generator))



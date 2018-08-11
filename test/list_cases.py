'''
...
'''


def foo(*values):
    print(values)
    counter = 1
    for i in values:
        print(counter)
        print(type(i))
        counter += 1


temp = [1, 2, 3, 4, 5]
foo(temp)
print('==============')
foo(*temp)
print('==============')
# 临时分配一个名字
test_list = [_ for _ in [1, 2, 3]]
print(test_list)

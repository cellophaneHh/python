'''
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
foo(*temp)  # 自动对list进行解包

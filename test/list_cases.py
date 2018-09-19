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
# foo(temp)
# print('==============')
# foo(*temp)
# print('==============')
# # 临时分配一个名字
# test_list = [_ for _ in [1, 2, 3]]
# print(test_list)

# list转字符串
print(' '.join(str(i) for i in temp))

# len_temp = len(temp)
# for i in range(len_temp):
#     print(temp[len_temp - i - 1])
#     print(temp.pop())


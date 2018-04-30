# 遍历集合的方法

# 通过dict.items()函数遍历字典
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, ":",  v)

# 遍历一个序列时，可以通过enumerate()函数得到蓄力中的索引
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# 同时循环多个序列时，可以使用zip()函数
questions = ['name', 'questions', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

# 逆序遍历一个列表，调用reversed()函数
for i in reversed(range(1, 10, 2)):
    print(i)

# 排序后再遍历，调用sorted()函数
basket_list = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket_list)):
    print(f)

# 修改列表时建议新建一个列表进行存储，下列方式不推荐
a = [1, 2, 3]
for i, d in enumerate(a):
    del a[i]
print(a)

"""
迭代器
"""

# for语句调用容器对象的iter()函数， 该函数返回一个定义了next()方法的迭代器对象，其逐一访问元素，没有后续元素时会引发StopIteration异常，告诉for循环种植
for i in [1,2,3]:
    print(i)

# 利用iter和next，模仿for循环工作

s = 'abc'

it = iter(s)
print(it)

print(next(it))
print(next(it))
print(next(it))

print(next(it))  # 抛出异常

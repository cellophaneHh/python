"""
元组
"""

# 只有一个元素的元组，必须加逗号
t1 = (1,)
print(type(t1))
t1 = (1)  ##这种写法是错误的
print(type(t1))

# 元组重复

t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(t1 + t2)
print((t1 + t2)[1:2])
print((t1 + t2)[2])

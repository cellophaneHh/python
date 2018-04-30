# 集合， 一种没有重复元素、无序的数据集
# 集合也支持一些数学操作，并集(union)、交集(intersection)、差集(difference)和对称差(symmetric difference)

basket_set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket_set)
print('orange' in basket_set)

# 使用set()函数, 这个会自动迭代可序列化的数据创建set
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print('数学集合操作')
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

# 支持类似列表推导式，可以使用集合推导式
print('集合推导式创建集合')
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

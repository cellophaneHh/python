from generators import int_generator_random

L = list(int_generator_random(100))
print(L)
L.sort()
print(L)

L = list(int_generator_random(100))
print(L)
print(sorted(L))

my_dic = {1:2, 2:4, 5:23}
# 对字典执行sorted函数会返回排序的键
print(sorted(my_dic))
my_dic.sort()

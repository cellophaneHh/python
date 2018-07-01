my_set = set([1, 2, 3, 4, 5])
print(my_set)
my_set = {1, 2, 4, 5}
print(my_set)
my_set.add('6')
print(my_set)
print(len(my_set))
print(1 in my_set)
print(11 not in my_set)
my_set1 = {1, 2, 4}
my_set2 = {3, 5, 6}
# 两个集合不相交
print(my_set1.isdisjoint(my_set2))

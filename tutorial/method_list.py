ll = []
# 两种写法，在最后增加一个元素
ll.append('a')
ll[len(ll):] = ['b']
print(ll)


print("==============")

ll = []

# 连接另一个列表
ll.extend([1,2,3])
print(ll)
ll[len(ll):] = [22,2,3]


print('==============')

ll = []

# 插入一个元素
ll.insert(0, '1')
ll.insert(len(ll), '2')
print(ll)

print('=========')
ll = []

# 移除一个元素
ll = [1,2,3]
ll.remove(1)
print(ll)


# 移除指定位置的元素
ll = [1,2,3,4,5,6]
ll.pop(1)
print(ll)


# 返回两个索引之间第一个x的索引，默认从整个表查询
ll = [11, 22, 44, 8, 2, 5]
d = ll.index(22, 0, 5)
print(d)
d = ll.index(22)
print(d)

print("=======返回元素x出现的次数=========")
ll = [11, 22, 11, 22, 33, 'a', 'asdf', 'asdf']
print(ll)
print('11-' + str(ll.count(11)))
print('a-' + str(ll.count('a')))
print('asdf-' + str(ll.count('asdf')))


print("===========对list进行排序==============")
ll = ['a','A', '89', 'kkk']
ll.sort()
print(ll)
ll.sort(key=str.lower)
print(ll)


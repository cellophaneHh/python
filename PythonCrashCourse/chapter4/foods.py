#复制列表，通过切片实现
#[:], 不指定开始和结束，即表示复制整个列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(friend_foods)

#在friend_foods插入一个元素后，my_foods没有改变，说明生成了一个新的列表
friend_foods.insert(0, 'aaa')
friend_foods.append("ddd")
print(my_foods)
print(friend_foods)


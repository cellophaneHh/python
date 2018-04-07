#切片

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])#从1开始到3结束，不包含3
print(players[:3])#不指定开始，默认0
print(players[1:])#不指定结束，默认列表长度

#也可以使用负数索引，默认最后一个元素索引为-1
#取最后三个
print(players[-3:])

#遍历切片
for p in players[1:3]:
    print(p.title())

x = 1
print(players[x:])

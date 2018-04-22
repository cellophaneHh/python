#元组: 即不可变的列表。列表可以增删改查，元组不能修改，只能查

dimensions = (200, 40)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 10
# print(dimensions)

#遍历
for d in dimensions:
    print(d)

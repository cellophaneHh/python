# del

a = [-1, 1, 66.25, 333, 333, 1234, 5]
del a[0]

print(a)

del a[2:4]
print(a)

del a[:]
print(a)

# del可用来删除变量
del a
print(a)  # NameError: name 'a' is not defined



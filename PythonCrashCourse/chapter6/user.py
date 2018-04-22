#遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
#1. 遍历字典的键和值
for key, value in user_0.items():
    print("\nkey: " + key)
    print("\nvalue: " + value)

print(user_0.items())

#2. 遍历字典的键
#显式调用keys方法
for key in user_0.keys():
    print("\nkey: " + key)
#隐式遍历键
for key in user_0:
    print("\nkey: " + key)

print(user_0.keys())

#使用sorted排序之后在遍历
for key in sorted(user_0.keys()):
    print("\nkey: " + key)

#3.遍历字典的值
for value in user_0.values():
    print("\nvalue: " + value)

#去掉重复元素set()


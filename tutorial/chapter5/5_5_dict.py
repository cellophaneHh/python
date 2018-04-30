# 字典

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

del tel['sape']
print(tel)

tel['irv'] = 4127
print(tel)

print(list(tel.keys()))

print(sorted(tel.keys()))

print('guide' in tel)
print('jack' in tel)

# 使用dict()创建字典
print(dict([('sape', 4192), ('guido', '4127')]))

# 推导式构建
print({x: x**2 for x in (2, 4, 6)})

# 使用dict()的关键字参数构建
print(dict(sape=4139, guido=4127, jack=4098))

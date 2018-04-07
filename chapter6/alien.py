#声明一个字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

print(type(alien_0['color']))
print(type(str(alien_0['points'])))

#向字典中添加键值
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#修改
alien_0['color'] = 'red'
print(alien_0)

#删除一个键值
print(alien_0)


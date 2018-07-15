'''
元组
需要使用索引访问元组的每个元素
'''

bob = ('Bob', 30, 'male')
print('Representation:', bob)

jane = ('Jane', 29, 'femal')
print('\nField by index:', jane[0])

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is a {} year old {}'.format(*p))

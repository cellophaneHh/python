import pandas as pd

print()
d1 = pd.DataFrame({
    'a': range(7),
    'b': range(7, 0, -1),
    'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
    'd': list('hjklmno')
})
print(d1)

d2 = d1.set_index(['c', 'd'])
print(d2)

d3 = d2['a']
print(type(d3))
print(d3['one']['j'])

d4 = d1.set_index(['d', 'c'])
print(d4)
print(d4['a'])
# 取第二个索引c对应的数据
print(d4.swaplevel().loc['one'])

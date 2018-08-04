import collections

item = {'id': 'a', 'children': ['a', 'b']}

dd = collections.defaultdict()

for k, v in item.items():
    dd[k] = v

dd.setdefault('children', [])

print(dd)


print('=================')

dd = collections.defaultdict(list)
dd[1] = 'a'
dd[2].append('b')
print(dd)
mapped_values = {'a': [1, 2, 3], 'b': [4, 5, 6]}
for key, value in mapped_values.items():
    dd[key].append(value)

import collections

item = {'id': 'a', 'children': ['a', 'b']}

dd = collections.defaultdict()

for k, v in item.items():
    dd[k] = v

dd.setdefault('children', [])

print(dd)
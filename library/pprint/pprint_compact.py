from pprint import pprint

from pprint_data import data

print('default:')
pprint(data, compact=False)
print('\ncompact:')
pprint(data, compact=True)
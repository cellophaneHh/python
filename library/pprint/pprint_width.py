from pprint import pprint

from pprint_data import data

for width in [80, 5]:
    print('Width = ', width)
    pprint(data, width=width)
    print()
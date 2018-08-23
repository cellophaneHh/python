import os

PATHS = [
    ('one', 'two', 'three'),
    ('/', 'one', 'two', 'three'),
    ('/one', '/two', '/three'),
]

print()
for parts in PATHS:
    print('{} : {!r}'.format(parts, os.path.join(*parts)))

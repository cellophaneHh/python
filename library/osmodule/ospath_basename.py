import os.path

PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
]
print()
for path in PATHS:
    print('{!r:>17} : {!r}'.format(path, os.path.basename(path)))

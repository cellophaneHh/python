import os.path

PATHS = [
    '/one/two/three',
    '/one/two/three.jpg',
    '/',
    '.',
    '',
]
print()
for path in PATHS:
    print('{!r:>17} : {}'.format(path, os.path.split(path)))

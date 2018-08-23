import os.path

paths = [
    '/one/two/three/four',
    '/one/two/threefold',
    '/one/two/three/',
]
print()
for path in paths:
    print('PATH:', path)

print()
print('COMMON_PREFIX:', os.path.commonprefix(paths))
print('COMMON_PATH:', os.path.commonpath(paths))

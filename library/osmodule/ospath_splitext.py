import os.path

PATHS = [
    'filename.txt',
    'filename',
    '/path/to/filename.txt',
    '/',
    '',
    'my-archive.tar.gz',
    'no-extension.',
]
print()
for path in PATHS:
    print('{!r:>21} : {!r}'.format(path, os.path.splitext(path)))

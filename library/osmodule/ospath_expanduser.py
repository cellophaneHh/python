import os

for user in ['', 'zh', 'nosuchuser']:
    lookup = '~' + user
    print('{!r:>15} : {!r}'.format(
        lookup, os.path.expanduser(lookup)))

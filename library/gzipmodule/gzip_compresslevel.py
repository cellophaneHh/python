import gzip
import io
import os
import hashlib

def get_hash(data):
    _md5 = hashlib.md5(data)
    print(_md5)
    print(type(_md5))
    return _md5.hexdigest()


data = open('D:/document/技术书/2019电商词库/dsciku.1w/dsciku.1w', 'r', encoding='utf8').read() * 100
cksum = get_hash(data.encode('utf-8'))

print('Level  Size        Checksum')
print('-----  ----------  ---------------------------------')
print('data   {:>10}  {}'.format(len(data), cksum))

for i in range(0, 10):
    filename = 'd:/data/compress-level-{}.gz'.format(i)
    with gzip.open(filename, 'wb', compresslevel=i) as output:
        with io.TextIOWrapper(output, encoding='utf-8') as enc:
            enc.write(data)
    size = os.stat(filename).st_size
    cksum = get_hash(open(filename, 'rb').read())
    print('{:>5d}  {:>10d}  {}'.format(i, size, cksum))

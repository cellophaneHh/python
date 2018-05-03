"""
数据压缩
zlib, gzip, bz2, lzma, zipfile, tarfile
"""

import zlib

s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))

print(zlib.crc32(s))


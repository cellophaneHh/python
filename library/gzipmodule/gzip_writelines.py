import gzip
import io
import itertools
import os

filename = 'example_lines.txt.gz';
with gzip.open(filename, 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.writelines(itertools.repeat('the same line, over and over.\n', 10))

with gzip.open(filename, 'rb') as input:
    with io.TextIOWrapper(input, encoding='utf-8') as denc:
        print(denc.read())
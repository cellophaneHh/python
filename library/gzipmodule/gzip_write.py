import gzip
import io
import os
import base64

orginal_content = "contents of the 呵呵 file go here.\n"
outfilename = 'example.txt.gz'
with gzip.open(outfilename, 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.write(orginal_content)

print('orginal_content len: ', len(orginal_content))
print(outfilename, 'contains', os.stat(outfilename).st_size, 'bytes')
# os.system('file -b --mime {}'.format(outfilename))

import gzip
from io import BytesIO
import binascii
import base64

uncompressed_data = b'The same line, over and over.\n' * 10
print("UNCOMPRESSED:", len(uncompressed_data))
print(uncompressed_data)

buf = BytesIO()
with gzip.GzipFile(mode='wb', fileobj=buf) as f:
    f.write(uncompressed_data)

compressed_data = buf.getvalue();
print('COMPRESSED_DATA:', len(compressed_data))
print(binascii.hexlify(compressed_data))
base64_enc = base64.b64encode(compressed_data)
print(base64_enc)
base64_str = str(base64_enc, encoding='utf-8')
print(base64_str)
base64_dec = base64.b64decode(base64_enc)
print(str(base64_dec))

inbuffer = BytesIO(compressed_data)
with gzip.GzipFile(mode='rb', fileobj=inbuffer) as file:
    reread_data = file.read(len(uncompressed_data))

print('\nREREAD:', len(reread_data))
print(reread_data)

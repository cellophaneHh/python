import hmac
import hashlib
import base64

with open('test.txt', 'rb') as f:
    body = f.read()

# 文本较短时，可以直接将文本传入new的第二个参数，不用调用update方法了
disgest_maker = hmac.new(
    b'secret-shared-key-goes-here',
    body,
    hashlib.sha1,
)

digest = disgest_maker.digest()
print(base64.encodebytes(digest))

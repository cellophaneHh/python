import hmac
import hashlib

disgest_maker = hmac.new(
    b'secret-shared-key-goes-here',
    b'',
    hashlib.sha1,
)

with open('test.txt', 'rb') as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        disgest_maker.update(block)

digest = disgest_maker.hexdigest()
print(digest)

import hmac

disgest_maker = hmac.new(b'secret-shared-key-goes-here')

with open('d:/private/python/library/hmac/test.txt', 'rb') as f:
    while True:
        block = f.read(1024)
        print(type(block))
        if not block:
            break
        disgest_maker.update(block)

digest = disgest_maker.hexdigest()
print(digest)

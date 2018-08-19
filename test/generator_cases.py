a = [i for i in range(10) if i % 2 == 0]
print(a)


g = (i for i in range(100))

for i in range(10):
    print(next(g))

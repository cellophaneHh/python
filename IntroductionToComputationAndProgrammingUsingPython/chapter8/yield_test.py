"""生成器"""

def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

# for n in fab(5000):
#     print(n)

# for n in range(500000):
#     print(n)


class Fab:
   """Fab实现了__iter__和__next__方法是一个iterator"""
   def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

   def __iter__(self):
       return self

   def __next__(self):
       if self.n < self.max:
           r = self.b
           self.a, self.b = self.b, self.a + self.b
           self.n = self.n + 1
           return r
       raise StopIteration()


for n in Fab(5):
    print(n)


print('=======================')
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

for n in fab(1000):
    print(n)


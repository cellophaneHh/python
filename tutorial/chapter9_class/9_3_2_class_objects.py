class Complex:
    def __init__(self, real_part, image_part):
        self.r = real_part
        self.i = image_part

    def f(self):
        return self.r


x = Complex(3.0, -4.5)

print(x.r, x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

print("===========方法对象==================")
# 方法对象
print(x.f())
xf = x.f

print(type(xf), xf())


"""
补充说明
"""
# 方法不一定必须定义在类中，也可以赋值给类的一个变量

def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

c = C()
print(c.f(10, 11))


# 类中的方法可以通过self调用其他方法
class Bag:

    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwitce(self, x):
        self.add(x)
        self.add(x)

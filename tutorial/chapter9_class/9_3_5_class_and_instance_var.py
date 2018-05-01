"""
类和实力变量
"""

class Dog:
    kind = 'canine'         # 被所有实例共享的类变量

    def __init__(self, name):
        self.name = name    # 每个实例单独的实例变量

d = Dog('Fibo')
e = Dog('Buddy')

print(d.kind)
print(e.kind)

print(d.name)
print(e.name)

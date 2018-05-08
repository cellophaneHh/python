"""
弱引用
weakref
"""
import weakref, gc

class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

a = A(11)
print(type(a))

# 这个键试了下不能是str和int
d = weakref.WeakKeyDictionary({a:a})
print(d.get(a))

# 删除a之后d中的a也不存在了
del a
gc.collect()

print(d.get(a))


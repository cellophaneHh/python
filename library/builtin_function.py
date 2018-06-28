"""
内置函数
"""
print("======abs======")
print(abs(-1))
print("==========all======")
it1 = [True, True, "asdf"]
it2 = []
print(all(it1))
print(all(it2))
print("=====any============")
print(any(it1))
print(any(it2))

print("=====bin=====")
print(bin(3))
print(bin(-10))
print(format(14, '#b'), format(14, 'b'))
print(f'{14:#b}', f'{14:b}')

print('====bool')
print(bool(True))
print(bool([]))
print(bool(-1), bool(0))

print('=======bytearray')
print(bytearray(str.encode('张恒')))
print(bytearray(1))

print('=======callable')


class MyClass:
    pass
    # def __call__(self):
    #     print("调用call")
    #     return False


print(callable(MyClass()))

print('====@classmethod')


class MyCLass1:
    @classmethod
    def show(self):
        print('asdfasdfasdfasdf')


MyCLass1.show()

print('===complex')
print('1+2+539')

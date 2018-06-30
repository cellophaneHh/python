"""
内置函数
"""
import struct


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

print('===complex复数')
print(complex('1+2j'))
print(complex(1, 2))

print("=======dir")

print(dir())
print(dir(map))
print(dir(struct))


class Shape:
    def __dir__(self):
        return ['area', 'perimeter', 'location']


shape = Shape()
print(dir(shape))

print('=====divmod')
a = 10
b = 3
print(divmod(a, b))
print(a // b, a % b)

print('====enumerate')
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(type(seasons))
print(list(seasons))
print(list(enumerate(seasons)))
# equivalent to


def enumerate_me(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1


enumerate_me_test = enumerate_me([1, 2, 3, 4], 1)
print(enumerate_me_test)
print(type(enumerate_me_test))

print('====eval')
x = 1
print(eval("x+1"))

print('===exec')
x = 20
exec("print(x)")

print('=====filter, 返回一个生成器')

names = ['zhangsan', 'lisi', 'wangwu']
print(list(filter(lambda name: name == 'zhangsan', names)))

print('===float')
print(float('+1.23'))
print(float('nan'))
print(float('    -12345\n'))
print(float('1e-003'))
print(float('+1E6'))
print(float('1e6'))
print(float('Infinity'))

print('===format')
print(format('123{0}', '10')) # 没效果...
print('123{0}'.format('10'))

print('====globals, 获得当前上下文中的所有符号表')
print(globals())

print('====hasattr')
print(hasattr(shape, 'name'))

print('========hash')
print(hash(shape))

print('======help,获得一个对象的帮助信息')
print(help(dir))

print('===hex, 返回16进制')

print(hex(255))
print(hex(-42))

print('====id')
print(id(shape), hash(shape))

print('====input')
print(input('请随意输入一些信息:'))

print('====int')
print(int('10'))

print('====isinstance, issubclass')
print(isinstance(shape, Shape))
print(issubclass(shape.__class__, Shape))

print('====pow')
print(pow(2, 10), 2**10)

print('=====range')
print(range(0, 10))

print('====reversed')
for c in reversed('123'):
    print(c)

print('====zip')
# print(help(zip))
x = [1, 2, 3]
y = [4, 5, 6, 8]
zipped = zip(x, y)
print(type(zipped))
print(list(zipped))
x2, y2 = zip(*zip(x, y))
print(list(x2), list(y2))
print(type(x2))

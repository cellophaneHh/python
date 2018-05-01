s = "Hello, world."
print(str(s))

print(repr(s))

print(type(repr(1)))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ' , and y is ' + repr(y) + '...'
print(s)

hello = 'hello, world\n'
print(repr(hello))
print(hello)

print(repr((x, y, ('spam', 'eggs'))))



print("====================")
# 这个rjust()是设置向右对齐，占2个字符
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))



# str.zfile()设置位数，不够时用0填充
print('12'.zfill(3))

# format()各种使用方法
print('We ar the {} who say "{}"!'.format('knights', 'Ni'))

# 设置索引
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# 根据键取值
print('The {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

#!a调用ascii()  !r调用repr()
contents = 'eels'
print("{!a}, {!r}".format(contents, contents))

# ':'可用来格式化数字
import math
print('{:.5f}'.format(math.pi))

# 使用[] 访问key
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}'.format(table))


# % 操作符
import math
print('The value of PI is approximately %5.3f.' % math.pi)

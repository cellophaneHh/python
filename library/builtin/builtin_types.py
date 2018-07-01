import math

print('======math.trunc，保留整数部分，完全抛弃小数')
print(math.trunc(11.1))

print('=========四舍五入')
print(round(11.1))
print(round(11.51))
print('==========bitwise operation')
print(0 | 1) # 或，存在1，为1， 其他为0
print(0 & 1) # 与，两个都为1，为1，其他为0
print(0 ^ 1 ) # 抑或，相同为0，其他为1
print(1 << 2)
print(2 >> 1)

print('====sequence')
print('asdf' * 2) # 复制一个字符串
seq = [0, 1, 2, 3, 4, 5]
print(seq[0:1]) # 截取一个字符串，前闭后开区间
print(seq[1:3])
print(seq[1:len(seq):2])
print(len(seq))
print(max(seq))
print(min(seq))
print(seq.index(1))

seq.append(0)
print(seq)
seq.insert(0, 1)
print(seq)
seq.extend([10])
print(seq)
# 这也可以，和extend一样的操作
seq[len(seq):len(seq)] = [11]
print(seq)

seq_copy = seq.copy()

print(seq)
seq.pop()
print(seq)

print(seq.remove(11))
print(seq)
del seq[0]
print(seq)

list = [1,3,2]
list.sort()
print(list)
print(sorted(list))

print('===========str')
print(('asdf ' 'asdf') == 'asdf asdf')
print(str(b'Zoot!'))

print('asdf'.capitalize())
print('ASDFß'.casefold())  # 对unicode字符起效，变为小写
print('ASDFß'.lower())  # 只对ascii字符起效，变为小写
# 字符串asdf作为center，*号填充，总长度为6的字符串
print('asdf'.center(6, '*'))

print('aasdf'.count('a'))
print('张恒asdf'.encode('utf-8'))
print('asdf'.endswith('f'))
# 替换tab为固定长度空格
print('asdf\tlk;j;ljk\t'.expandtabs(4))

print('{1}, {0}, {2}'.format('0', '1', '2'))

print('asdf-'.isalnum())
print('1234'.isdigit())
print('  '.isspace())
print('asdf'.join([';']))
print('asdf'.partition('as'))
print('asdfa'.replace('a', 'q', 1))
print('asdfa'.rfind('a'))
print('asdfa'.find('a'))
print('asdfa'.upper())
print('asdf'.zfill(5))

print('%(language)s has %(number)03d quote types.' %
      {'language': "Python", 'number': 2})

v = memoryview(b'abcefg')
print(v[1])
print(v[-1])
print(v[1:4])
print(bytes(v[1:4]))

s = [1, 2, 3, 4]
print(s[::])
print(s[::2])

import array

a = array.array('l', [-11111111, 22222222, -33333333, 44444444])
m = memoryview(a)
print(m[0])
print(m[-1])
print(m[::2].tolist())

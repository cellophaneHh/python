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

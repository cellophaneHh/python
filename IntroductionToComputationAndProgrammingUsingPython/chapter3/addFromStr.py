# !coding=utf8

s = '1.23, 2.4, 3.123'

ints = s.split(', ')

result = 0;
for i in ints:
    result += float(i)

print(result)

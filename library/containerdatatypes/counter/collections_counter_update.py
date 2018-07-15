import collections

c = collections.Counter()
print('Initial: ', c)

# 根据序列中元素个数更新c中值
c.update('abcdaab')
print('Sequence:', c)

# 根据字典中键更新c中值, 字典中key肯定只有一个，所有出现的都是+1
c.update({'a': 1, 'd': 5, 'e': 1})
print('Dict: ', c)

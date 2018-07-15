import collections

c = collections.Counter()
with open('/usr/share/dict/words', 'rt') as f:
    for line in f:
        c.update(line.rstrip().lower())

# 计算出现最多的值
print('Most common:')
for letter, count in c.most_common(3):
    print('{}: {:>7}'.format(letter, count))

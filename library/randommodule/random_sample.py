'''
随机抽取固定个数的样本
'''
import random

with open('/usr/share/dict/words', 'rt') as f:
    words = f.readlines()

words = [w.rstrip() for w in words]
for w in random.sample(words, 5):
    print(w)

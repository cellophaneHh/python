import collections
import random

Data = collections.namedtuple('data', ['name', 'msg'])


class A:
    def __init__(self):
        self.datas = [Data(name=str(i) + "d", msg='msg') for i in range(10)]

    def __getitem__(self, i):
        return self.datas[i]

    def __len__(self):
        return len(self.datas)


a = A()
print(len(a))
print(a[1])
print('*' * 10)
print(random.choice(a))

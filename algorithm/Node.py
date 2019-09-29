'''
树节点
'''


class Node:
    def __init__(self, key, value, N):
        self.key = key
        self.value = value
        self.N = N
        self.left = None
        self.right = None

    def __str__(self):
        return str({'key': self.key, 'value': self.value, 'N': self.N})

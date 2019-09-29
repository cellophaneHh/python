from Node import Node
import random
import time


class BST:
    def __init__(self, root):
        self.root = root

    def get(self, key):
        if not self.root:
            return
        node = self.root
        while node:
            if node.key == key:
                return node
            elif node.key > key:
                node = node.left
            else:
                node = node.right

    def put(self, key, value):
        if not self.root:
            self.root = Node(key, value, 1)
            return self.root
        node = self.root
        while node:
            if node.key == key:
                node.value = value
                break
            elif node.key > key:
                if not node.left:
                    node.left = Node(key, value, 1)
                    node.N += 1
                    node = node.left
                    break
                else:
                    node.N += 1
                    node = node.left
            else:
                if not node.right:
                    node.right = Node(key, value, 1)
                    node.N += 1
                    node = node.right
                    break
                else:
                    node.N += 1
                    node = node.right
        self.root.N = self.__size(self.root.left) + self.__size(
            self.root.right) + 1
        return node

    def delete(self, key):
        pass

    def size(self):
        return self.__size(self.root)

    def __size(self, node):
        if not node:
            return 0
        return self.__size(node.left) + self.__size(node.right) + 1


bst = BST(Node(500, '1', 1))
start = time.time()
for i in range(0, 1000):
    bst.put(random.randint(0, 1000), '1')

print(bst.size())
print(bst.get(200))
print(time.time() - start)

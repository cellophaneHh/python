# 作为栈使用
stack = []
stack.append('1')
stack.append('2')
stack.append('3')
print(stack)
stack.pop()
print(stack)

# 作为队列使用, 由于线率不高，使用deque
from collections import deque
queue = deque(["Eric", "John", 'Michael'])
queue.append('Terry')
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue)

squares = list(map(lambda x: x**2, range(10)))
print(squares)
squares = [x**2 for x in range(10)]
print(squares)

tuples = [(x, y) for x in [1,2,3] for y in [4, 5, 6]]
print(tuples)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec if x > 0])

vec = [[1,2,3], [4,5,6], [7,8,9]]
nums = [num for elem in vec for num in elem]
print(nums)

# 矩阵行转列
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
matrix_t = [[row[i] for row in matrix] for i in range(4)]
print(matrix_t)
# zip
zip_t = zip(*matrix)
print(type(zip_t))
print(list(zip_t))



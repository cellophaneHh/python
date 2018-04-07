#平方
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

#max min sum
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits))
print(min(digits))
print(sum(digits))

#通过列表解析生成列表
#生成函数 value**2   值列表: for循环
squares = [value**2 for value in range(1, 11)]
print(squares)

number = [value*2 for value in range(1, 10)]
print(number)

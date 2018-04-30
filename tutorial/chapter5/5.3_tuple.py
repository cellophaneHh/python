# 元组和序列
# 元组是由逗号分割的一组值，也可以由圆括号包裹起来，是不可变的
t = 12345, 54321, 'hello!'
print(type(t))
print(t[0])
print(t)

u  = t, (1,2,3)
print(u)
#t[0] = '123' # TypeError

# 空元组
empty = ()
print(empty)
# 只有一个元素的元组
singlon = 1,
print(singlon)

# 序列是可变的，通常序列中的元素是一类的
l = []


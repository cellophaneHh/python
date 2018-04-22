#练习导入模块
#导入整个模块,这是需要使用ipizza.funname方式调用函数
# import pizza

#导入一个模块中某个函数, 并指定别名(可以不指定)
# from pizza import make_pizza as m
# mp('s', 'g', 'dd', 'ddd')
#导入模块中所有函数，与第一个不同的是不需要使用'.'调用函数
from pizza import *

make_pizza('a','b','c')
make_pizza('sdf')


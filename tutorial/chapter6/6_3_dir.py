"""
dir()函数
用于寻找模块定义的所有名称，返回一个有序字符串列表
"""
import fibo, sys

print(dir(fibo))

print(dir(sys))

# 没有参数时，dir()列出当前模块的定义,包括import进来的模块
print(dir())

# dir()不列出内置函数和变量的名称，如果需要的话要引入builtins模块
print("\n================")
import builtins

print(dir(builtins))

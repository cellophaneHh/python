"""
from sound.effects import* 做了什么?

1、如果__init__.py中定义了一个名叫__all__的列表，使用这个列表进行导入
2、如果没有定义，则只保证模块sound.errects被导入进来
"""
from sound.formats import *

# 这个相对引用没看懂。。。。
# 也可以是用相对路径的引用
# . 当前目录 .. 父目录
# from . import fibo
# from ..sound.formats import *

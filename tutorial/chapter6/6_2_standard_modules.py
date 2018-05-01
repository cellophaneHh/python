"""
python自带一些标准库
sys 是一个特殊的模块
"""
import sys

print('=========')
# sys.ps1 定义了python的主提示符
print(sys.ps1)
# sys.ps2定义了python的副提示符
print(sys.ps2)

# sys.path定义了模块搜索路径，从环境变量PYTHONPATH中初始化，可以修改

print("==========")
print(sys.path)
sys.path.append('~/github/testpy')
print(sys.path)

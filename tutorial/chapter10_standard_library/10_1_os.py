"""
os模块，提供了很多与操作系统交互的功能
"""
import os

import shutil


# 获取当前工作目录
print(os.getcwd())
# 改变工作目录
os.chdir('/home/zh2683/github')

# 执行一条命令
# d = os.system('mkdir today')
# print(d)

dir(os)
# 显示帮助信息，好长。。。
help(os)

"""
shutil模块提供了一些高级的文件操作借口
"""
f = shutil.copyfile('/home/zh2683/github/virtualenvcstart.txt', '/home/zh2683/github/virtualenvcstart_backup.txt')
print(f)
f = shutil.move('/home/zh2683/github/today', '/home/zh2683/github/tomorrow')
print(f)

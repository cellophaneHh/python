"""
文件通配符
glob模块提供了根据通配符从目录中查找文件的功能
"""
import os
import glob

os.chdir('/home/zh2683/github/python/tutorial/chapter10_standard_library')
l = glob.glob("*.py")

print(l)


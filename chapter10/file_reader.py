"""
文件操作
"""
import os

print(os.getcwd())

#一次读取
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#逐行读取
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

#将文件内容逐行存储在一个列表中
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

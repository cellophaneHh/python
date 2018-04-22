"""写文件练习"""

filename = 'programming.txt'

#写文件，覆盖
with open(filename, 'w') as file_object:
    file_object.write("I love programming\n")

#追加写，不覆盖
with open(filename, 'a') as file_object:
    file_object.write("I love python\n")


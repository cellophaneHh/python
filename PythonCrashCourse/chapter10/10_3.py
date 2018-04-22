"""读取用户输入并写入文件"""

name = input("your name: ")
with open('guest.txt', "w") as file_object:
    file_object.write(name + "\n")

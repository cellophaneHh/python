# open 打开一个文件
# r 读  w写 a追加  r+读写
# 上面模式后面加b，说明是二进制文件
# 这个open会新建文件
f = open('workfile', 'w')
with open('workfile') as f:
    read_data = f.read()

print(f.closed)

with open('workfile', 'w') as f:
    f.write("asdf")

with open('workfile', 'r') as f:
    line = f.readline()
    if line:
        print(line)


f = open('workfile', 'rb+')
i = f.write(b'0123456789abcdef')
print(i)
print(f.seek(5))
print(f.read(1))
# offset:3 代表偏移量  whence:2 定义从哪里开始便宜 0：文件头，1：当前位置 2：文件末尾
print(f.seek(-3, 2)) # 这里是值从文件末尾(2)开始，偏移量为3
print(f.read(1))

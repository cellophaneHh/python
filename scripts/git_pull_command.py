'''
更新机器上的所有git目录，病打印更新结果
'''
import os

parentDir = '/home/zh/Projects/'

result = os.chdir(parentDir)
print(result)

dirs = os.listdir()

for dir in dirs:
    os.chdir(parentDir + "/" + dir)
    print("cwd:", dir)

    subDirs = os.listdir()
    try:
        if '.git' in subDirs:
            result = os.system('git pull origin master')
            print("更新结果:", result)
    except Exception as e:
        print("异常", dir, e)

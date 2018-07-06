'''
更新机器上的所有git目录，病打印更新结果
'''
import os

parentDir = '/home/zh/Projects/'

os.chdir(parentDir)

dirs = os.listdir()

for d in dirs:
    os.chdir(parentDir + "/" + d)
    print("cwd:", d)

    subDirs = os.listdir()
    try:
        if '.git' in subDirs:
            result = os.system('git pull origin master')
            print("更新结果:", result)
    except Exception as e:
        print("异常", d, e)

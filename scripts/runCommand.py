import os

# print(os.getcwd())

parentDir = '/home/zh/Projects/'

result = os.chdir(parentDir)
print(result)

dirs = os.listdir()

for dir in dirs:
    os.chdir(parentDir + "/" + dir)
    print("cwd", dir)

    subDirs = os.listdir()
    try:
        if '.git' in subDirs:
            result = os.system('git pull origin master')
            print("更新结果", result)
    except:
        print("异常", dir)

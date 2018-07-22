'''
如果命令执行有错误，抛出
'''
import subprocess

try:
    subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print('ERROR', err)


# 没有指定check=True, 不会抛出异常
subprocess.run(['false'])

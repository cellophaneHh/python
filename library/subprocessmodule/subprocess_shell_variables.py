'''
shell=True参数意味着，shell中各种变量，特性都可以得到
'''
import subprocess

completed = subprocess.run('echo $HOME', shell=True)
print('returncode: ', completed.returncode)

# 没有设置shell所以得不到此属性，会报错
# subprocess.run('echo $JAVA_HOME')

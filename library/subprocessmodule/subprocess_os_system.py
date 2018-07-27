'''
可以运行调用run()方法执行系统命令
'''
import subprocess

completed = subprocess.run(['ls', '-l'])
print('returncode: ', completed.returncode)


subprocess.run('git status')

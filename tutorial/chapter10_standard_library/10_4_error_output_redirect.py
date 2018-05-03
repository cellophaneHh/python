"""
错误输出重定向
sys模块提供了stdin， stdout，stderr
"""
import sys

sys.stderr.write('Warning, log file not found starting a new one\n')
sys.stdout.write('asdf')
sys.exit()


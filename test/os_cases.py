import os
import sys

print('os.path.realpath(__file__): {}'.format(os.path.realpath(__file__)))
print('')
print(sys.argv)
print('')
print('sys.argv[0]: {}'.format(sys.argv[0]))
print('')
print('os.path.abspath(sys.argv[0]): {}'.format(os.path.abspath(sys.argv[0])))
print('')
print('os.path: {}'.format(sys.path))

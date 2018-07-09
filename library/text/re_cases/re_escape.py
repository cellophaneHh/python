import re
import string

print(re.escape('python.exe'))

legal_chars = string.ascii_lowercase + string.digits + "!#$%&"
print('[%s]+' % re.escape(legal_chars))

print(string.ascii_lowercase)
print(string.digits)

operators = ['+', '-', '*', '/', '**']
print('|'.join(map(re.escape, sorted(operators, reverse=True))))

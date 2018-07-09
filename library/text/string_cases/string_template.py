import string

values = {'var': 'foo'}

t = string.Template('''
Variable  : $var
Escape    : $$
Variable in text  : ${var}iable
''')

# substitute 替换模板中的变量
print('TEMPLATE', t.substitute(values))

s = """
Variable : %(var)s
Escape : %%
Variable in text : %(var)siable
"""
print("INTERPOLATION:", s % values)

s = """
Variable : {var}
Escape : {{}}
Variable in text : {var}iable
"""

print("FORMAT:", s.format(**values))

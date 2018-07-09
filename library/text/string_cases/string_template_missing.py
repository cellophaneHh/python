import string

values = {'var': 'foo'}

t = string.Template("$var is here but $missing is not provid")

try:
    print(t.substitute(values))
except KeyError as err:
    print('ERROR', str(err))

print(t.safe_substitute(values))

import string

s = "Thre quick brown fox jumped over the lazy dog"

# 句子每个单词首字母大写
print(s)
print(string.capwords(s))

values = {'name': 'zh', 'address': 'hangzhou'}
s = "case:$name,asdf:$address, "
template = string.Template(s)
print(template.substitute(values))

print('%s----%d' % ('1', 21))
print('%(name)s %(address)s' % {'name': 'asdf', 'address': 'asdf'})

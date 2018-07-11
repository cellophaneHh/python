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

print("%(name)s" % {'name': '%号进行字符串格式化'})
print("{name}".format(name="str.format进行字符串格式化"))
name = 'f进行字符串格式化'
print(f"{name}")

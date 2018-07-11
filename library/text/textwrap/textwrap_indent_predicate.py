import textwrap
from textwrap_example import sample_text


def should_indent(line):
    print("Indent. {!r}".format(line))
    return len(line.strip()) % 2 == 0


dedented_text = textwrap.dedent(sample_text)
wrapped = textwrap.fill(dedented_text, width=50)
# 过滤格式化后那些句子需要输出
final = textwrap.indent(wrapped, 'EVEN ',
                        predicate=should_indent)

print('\Quoted block:\n')
print(final)

import textwrap
from textwrap_example import sample_text

# 去除首层的缩进
dedented_text = textwrap.dedent(sample_text)
print('Dedented: ')
print(dedented_text)

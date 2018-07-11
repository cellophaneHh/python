import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text).strip()

# 设置初始缩进和下一层缩进
print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=50))

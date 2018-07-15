import re

detail_url_pattern = re.compile(('<div class="post_weidaopic"'
                                 '>[\s\S]*?<a href="(.*?)"'))
source = ('<div class="post_weidaopic">http'
          'asdlfjasdfljasdfljk<a href="asdfl;asldfjlasjdf"')

result = detail_url_pattern.findall(source)


print(result)

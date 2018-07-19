import requests
import time

# 王刚微博主页链接
url = 'https://weibo.com/p/1005052804506181/home?from=page_100505_profile&wvr=6&mod=data&is_all=1#place'

session = requests.session();
session.headers["user-agent"] = ('Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) '
                                 'Gecko/20100101 Firefox/61.0')
session.headers['cookie'] = ('YF-V5-G0=73b58b9e32dedf309da5103c77c3af4f; SUBP=0033WrS'
                             'XqPxfM725Ws9jqgMF55529P9D9WFr6rZm6kIiqB.if_ZxUW5R5JpX5Kz'
                             'hUgL.Fo2Re0BNeKBcSKe2dJLoI7DAIsyLdJMESon0; login_sid_t=97'
                             '09ccb4d0a5cb16a827b803ac4e7f0a; cross_origin_proto=SSL; '
                             'YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; wb_view_log=1366*7681; _'
                             's_tentry=passport.weibo.com; Apache=2095907165313.8982.1531975504375; '
                             'SINAGLOBAL=2095907165313.8982.1531975504375; '
                             'ULV=1531975504377:1:1:1:2095907165313.8982.1531975504375:; '
                             'SUHB=04WfTXMHM7P2_k; ALF=1563511625; SSOLoginState=1531975626; '
                             'wvr=6; YF-Page-G0=e3ff5d70990110a1418af5c145dfe402; '
                             'wb_view_log_1834714653=1366*7681; UOR=,,spr_sinamktbd_bd_baidub_weibo_t001')
response = session.get(url)
print(response.status_code)
print(response.headers)
file_name = str(round(time.time() * 1000)) + ".html"
with open('./html/' + file_name, 'w+', encoding=response.encoding) as f:
    f.write(response.text)

print(session.headers)
response = session.get("https://weibo.com/p/1005052804506181/home?from=page_100505_profile&wvr=6&mod=data&is_all=1&display=0&retcode=6102")
print(response.status_code)
print(response.headers)
print(response.encoding)
file_name = str(round(time.time() * 1000)) + ".html"
with open('./html/' + file_name, 'w+', encoding=response.encoding) as f:
    f.write(response.text)

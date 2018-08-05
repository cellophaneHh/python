import requests
import json
import time

cookie = 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFr6rZm6kIiqB.if_ZxUW5R5JpX5K2hUgL.Fo2Re0BNeKBcSKe2dJLoI7DAIsyLdJMESon0; wb_view_log=1376*7741.3953488372093024%26975*5501.3953488372093024; SINAGLOBAL=8679527586613.035.1533454611803; ULV=1533455822493:2:2:2:5526924593627.423.1533455822491:1533454611805; SCF=AsYm-8NQFWrarPNriRTdhKu6BrzR7FAvvIBrY0qFq7HtWv1s8O5U_zxUafEWEn1D7AKKblIzt3vockACH5GFbWA.; SUHB=0U14EHT9UCXJb_; un=18518381557; wb_view_log_1834714653=1376*7741.3953488372093024%26975*5501.3953488372093024; UOR=,,login.sina.com.cn; YF-V5-G0=f0aa2e6d566ccd1c288fae19df01df56; SUB=_2A252YsihDeRhGedG6FYW8SrKzj-IHXVVGb1prDV8PUNbmtBeLUHNkW9NUVX0-E7Gk1VzoVzeKTOMweN99vuDvqfw; YF-Page-G0=1ac418838b431e81ff2d99457147068c; _s_tentry=login.sina.com.cn; Apache=5526924593627.423.1533455822491; YF-Ugrow-G0=ad83bc19c1269e709f753b172bddb094; login_sid_t=e18a78d1ad45a5c278f490a2df5755bd; cross_origin_proto=SSL; WBtopGlobal_register_version=2b2691ab11833cbd; ALF=1534063473; SSOLoginState=1533458674; wvr=6'

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'

referer = "https://weibo.com/"

headers = {
    'cookie': cookie,
    'referer': referer,
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'accept-encoding': 'gzip,deflate,br',
    'user-agent': user_agent,
}

re = requests.get('https://weibo.com/u/1834714653/home?wvr=5', headers=headers)
print(re.status_code)
html_source = re.text
print(html_source[0:100])
with open('weibo_zh.html', 'w+', encoding='utf-8') as f:
    f.write(html_source)
print('完了..')

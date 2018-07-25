from selenium import webdriver
import time

url = 'https://weibo.com/u/1834714653'
cookie = ('YF-V5-G0=73b58b9e32dedf309da5103c77c3af4f; SUB=_2A252VdAYDeRhGedG6FYW8SrKzj-IHXVVI0bQrDV8PUNbmtBeLUjfkW9NUVX0-HFv8BsvSWDSJvr_2yXSSr_r3a1n; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFr6rZm6kIiqB.if_ZxUW5R5JpX5KMhUgL.Fo2Re0BNeKBcSKe2dJLoI7DAIsyLdJMESon0; login_sid_t=9709ccb4d0a5cb16a827b803ac4e7f0a; cross_origin_proto=SSL; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; _s_tentry=passport.weibo.com; Apache=2095907165313.8982.1531975504375; SINAGLOBAL=2095907165313.8982.1531975504375; ULV=1531975504377:1:1:1:2095907165313.8982.1531975504375:; SUHB=079SjqazQ9gDTJ; ALF=1563612104; SSOLoginState=1531975626; wvr=6; YF-Page-G0=e3ff5d70990110a1418af5c145dfe402; UOR=,,spr_sinamktbd_bd_baidub_weibo_t001; SCF=At3BE_sTggTPpG0mZ_KdszYYcmI6LDGEk_g3hYSy5RS7XGajw6iw3r-reW92aRpGcNUI5tM6RoevJzosrHA-xAA.; wb_view_log_1834714653=1366*7681')
cookie_list = cookie.split("; ")
cookies = []
for cookie in cookie_list:
    temp = cookie.split("=")
    single_cookie = dict()
    single_cookie['name'] = temp[0]
    if len(temp) == 2:
        single_cookie['value'] = temp[1]
    cookies.append(single_cookie)
print(cookies)
firefox = webdriver.Firefox()
try:
    firefox.get(url)
    time.sleep(2)
    firefox.delete_all_cookies()
    print('==========wait 2 second')
    for cookie in cookies:
        firefox.add_cookie(cookie)
    # firefox.add_cookie(srf)
    print(firefox.get_cookies())
    time.sleep(2)
    firefox.get(url)
    print(firefox.get_cookies())
    html_source = firefox.page_source
    print(html_source)
    with open('weibo.html', 'w+', encoding='utf-8') as f:
        f.write(html_source)
finally:
    firefox.close()
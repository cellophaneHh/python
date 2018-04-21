import requests

from operator import itemgetter

# 调用api(被墙了。。)
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
# 代理
proxies = {'https':'socks5://127.0.0.1:1080', 'http':'socks5://127.0.0.1:1080'}

r = requests.get(url, proxies=proxies)
print("Status Code:", r.status_code)

#
submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:3]:
    url = "https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json"
    submission_r = requests.get(url, proxies=proxies)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])




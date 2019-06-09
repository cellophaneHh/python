import requests
import time
import random


def real_task(url):
    time.sleep(1)
    i = random.randint(1, 2)
    if i == 1:
        return requests.get(url).status_code
    else:
        return requests.head(url).status_code


def task(url):
    result = real_task(url)
    filename = str(time.time())
    with open(filename, 'w') as f:
        f.write(filename)
    print("result: {}, time: {}".format(result, time.time()))


now = time.time()
urls = []
for i in range(10):
    task('http://httpbin.org')
print(time.time() - now)

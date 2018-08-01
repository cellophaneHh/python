import requests
import threading


url = "http://www.beautylegmm.com/"


def work(url):
    for i in range(10):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print('ok')
            else:
                print(response.status_code, response.reason)
        except Exception:
            print('...')


q = [
    threading.Thread(
        target=work,
        args=(url,),
        name="worker-" + str(i))
    for i in range(10)
]


for t in q:
    t.start()
    t.join()

print('finished.....')

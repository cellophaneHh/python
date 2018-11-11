import requests

url = "http://ovpm8j198.bkt.clouddn.com/fhuqlvsvgy5y4qkskk-1bkao8hwu"

res = requests.get(url)

with open('/home/zh/Pictures/test.jpg', 'wb') as file:
    file.write(res.content)

print("完了...")

import requests

# 执行API调用并存储响应
url = 'https://api.github.com/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print(type(response_dict[0]))

# 处理结果
print(response_dict[0].keys())
for key,value in response_dict[0].items():
    print(key + '-' + str(value) + "\n")

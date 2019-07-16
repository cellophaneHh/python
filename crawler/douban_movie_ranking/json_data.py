from db.redis_pool import redis_client
import pandas as pd
import json

key = 'movie_info'
datas = []
cursor, data = redis_client.hscan(key, 0)
for key, value in data.items():
    datas.append(json.loads(value, encoding='utf-8'))

while cursor > 0:
    cursor, data = redis_client.hscan(key, cursor)
    for key, value in data.items():
        datas.append(json.loads(value, encoding='utf-8'))

print(len(datas))
df = pd.read_json(json.dumps(datas, ensure_ascii=False))
print(df.info())

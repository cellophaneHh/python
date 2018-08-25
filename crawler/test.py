import json


info_json = {'a': 'b'}
with open('test_json.json', 'a') as f:
    json.dump(info_json, f, ensure_ascii=False, separators=(',', ':'))
    f.write('\n')
print('finished...')

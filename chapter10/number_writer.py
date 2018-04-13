"""json写文件"""
import json

numbers = [1, 2, 3, 4, 5, 10, 111]

filename = 'numbers.json'
with open(filename, 'w') as file_obj:
    json.dump(numbers, file_obj)


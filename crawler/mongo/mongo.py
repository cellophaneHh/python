from pymongo import MongoClient

conn = MongoClient()
db = conn.admin
db.authenticate('zh', '1234qwer')

# doc = db.baike_detail_html_source.find_one(
#     {"url": "http://baike.baidu.com/item/计算机网络/19437489#viewPageContent"})
# print(doc)

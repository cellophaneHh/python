from redisclient.redis_pool import redis_client
from mongo.mongo import db

detail_urls_result = redis_client.sscan("baike_detail_urls_raw", 0, count=100)
while True:
    cursor, detail_urls = detail_urls_result
    if cursor == 0:
        break

    urls = []

    for detail_url in detail_urls:
        urls.append({"url": detail_url})

    db.baike_detail_urls_raw.insert_many(urls)

    detail_urls_result = redis_client.sscan("baike_detail_urls_raw",
                                            cursor,
                                            count=100)
print("结束")

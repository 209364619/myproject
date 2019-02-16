#!coding=utf-8
from pymongo import MongoClient

month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# 数据库建立连接
client = MongoClient(host="10.10.10.50", port=27000)
db = client['test']
collection = db['tweets']
target_db = client['tweets_database_test']


# 日期转化
def get_month_day(date_str):
    month_str = date_str[4:7]
    month = (month_list.index(month_str)) + 1
    month = str(month)
    if len(month) < 2:
        month = '0' + month
    str_day = date_str[8:10]
    str_year = date_str[26:30]
    collection_name = 'tweets-' + str_year + '-' + month + '-' + str_day
    if str_year == '2018':
        return collection_name
    else:
        return 'false'


# 数据获取
rs = collection.find().limit()
print rs.count()
for record in rs:
    del record['_id']
    unicode_date = record['created_at']
    str_date = unicode_date.encode('utf-8')
    collection_name = get_month_day(str_date)
    if collection_name == 'false':
        continue
    else:
        print collection_name
        target_collection = target_db[collection_name]
        target_collection.insert(record)

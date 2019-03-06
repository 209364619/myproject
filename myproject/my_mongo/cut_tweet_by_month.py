#!coding=utf-8
from pymongo import MongoClient

# 将推文按照日期存储到数据库
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# 数据库建立连接
client = MongoClient(host="10.10.10.50", port=27000)
db = client['test']
collection = db['tweets']
target_db = client['tweets_database_test']

str_year = "2017"

if str_year == '2018':
    print 'false'

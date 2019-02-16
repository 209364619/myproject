#!coding=utf-8
from pymongo import MongoClient

client = MongoClient("10.10.10.50", 27000)
# client = MongoClient("192.168.209.110", 27017)
# user_db = client['item_baike_analysis']
# collection = user_db['baike']
db = client['my_test']
collection = db['test']

rs = collection.find({'name': 'lisi'})
for item in rs:
    print item

# collection.update_many({'name': 'lisi'}, {'$set': {'age': 22}})

rs = collection.find()
for item in rs:
    print item['age']
# collection.update({}, {'$set': {'item_type': '黑客'}})
# collection.updata({}, {'$set': {'item_type_id': '154486141479'}})
# for item in rs:
#     # print item['item_type']
#     # item['item_type'] = '黑客'
#     print type(item)
#     print item['item_type']
#     print item['item_type_id']# = 154486141479
#     # collection.update({'$set':{'item_type': '黑客'}})
#     # collection.update()
#     print ''

# for item in rs:
#     print item['item_type']
#     print item['item_type_id']


# base_type_collection = user_db['base_type']
# base_type = base_type_collection.find_one()
# print base_type['value'][2]['item_type_id']  154486141479

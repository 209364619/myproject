#!coding=utf-8
from pymongo import MongoClient

# 删除时间格式不符合要求的记录

client = MongoClient(host="192.168.8.200", port=27000)

db = client['tweets_database']
# 遍历数据库中所有表
collection_name = db.list_collection_names()


def dele_doc_without_ts():
    # collection_name = ['tweets-2018-09']
    for name in collection_name:
        collection = db[name]
        # body = {"create_at_ts": {"$exists": "false"}}
        body = {"created_at_ts": None}
        # print name, collection.find(body).count()
        rs = collection.delete_many(body)
        print rs.deleted_count, "个文档已删除"


def drop_empty_collections():
    for name in collection_name:
        collection = db[name]
        if collection.find().count() <= 0:
            db.drop_collection(collection)
            print collection_name, ":被删除！"


def count_created_ts():
    for name in collection_name:
        collection = db[name]
        print name
        print '记录总数：', collection.find().count()
        print '存在created字段数：', collection.find({"created_at_ts": {"$exists": True}}).count()
    print '查询结束'


# 创建测试数据库
def create_database(num):
    db = client['my_test']
    for i in range(num):
        collection = db["collection" + str(i)]
        collection.insert({"id": i})
    print '创建完成'


# 删除集合
def drop_collection():
    db = client['my_test']
    collection_list = db.collection_names()
    for collection in collection_list:
        db.drop_collection(collection)
    print '删除完成'


# 重新处理没有created_at_ts的记录
def deal_created_at_ts():
    month_list = ["08", "09", "10", "11", "12"]
    for month in month_list:
        month_str1 = "tweets-2018-" + month
        for i in range(1, 31):
            if i < 10:
                collection_name = month_str1 + "-0" + str(i)
            else:
                collection_name = month_str1 + "-" + str(i)
            collection = db[collection_name]
            # rs = collection.find_one({"created_at_ts":{"$exists": True}})
            # print collection_name
            rs = collection.find()
            if rs is not None:
                for item in rs:
                    created_at_ts = item.get("created_at_ts")
                    if not isinstance(created_at_ts, int):
                        print(collection_name, created_at_ts)


# 将double类型的created_at_ts修改为int
def data_transform():
    collection_name_list = ["tweets-2018-09-03", "tweets-2018-11-28", "tweets-2018-11-29"]
    for name in collection_name_list:
        collection = db[name]
        rs = collection.find()
        for item in rs:
            # print item['_id']
            # print item['created_at_ts'],type(item['created_at_ts'])
            if not isinstance(item['created_at_ts'], int):
                int_time = int(item['created_at_ts'])
                # print type(int_time)
                collection.update_one({"_id": item['_id']}, {"$set": {"created_at_ts": int_time}})


def drop_collection_by_year(year):
    monthlist = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    for month in monthlist:
        for date in range(1, 31):
            if date < 10:
                date = "0" + str(date)
            else:
                date = str(date)
            collection_name = "tweets-" + str(year) + "-" + month + "-" + date
            collection = db[collection_name]
            collection.drop()


def translate_double_to_int():
    collection = db["tweets-2018-09-03"]
    rs = collection.find()
    for item in rs:
        _id = item["_id"]
        id = item['user']['id']
        # print id, type(id)
        id = long(id)
        print id, type(id)
        collection.update({"_id": _id}, {"$set": {"user.id": id}})
    print "double 转换为int完毕！"


def remove_data():
    collection_list = ["tweets-2018-08", "tweets-2018-09-03", "tweets-2018-12", "tweets-2018-11", ]
    for item in collection_list:
        collection = db[item]
        print item, collection.count()
        collection.drop()
        print item, "集合删除成功"


if __name__ == '__main__':
    remove_data()

# coding=utf-8
from pymongo import MongoClient
import time

test_host1 = "192.168.8.200"
test_host2 = "192.168.209.113"
port1 = 27000
port2 = 27017
client = MongoClient(host=test_host2, port=port2)


def translate_objectid_to_timestamp():
    '''
    mongodb生成的Objectid是12字节的Bson类型字符串
    4字节：UNIX时间戳
    3字节：表示运行MongoDB的机器
    2字节：表示生成此_id的进程
    3字节：由一个随机数开始的计数器生成的值
    :return:
    '''
    test_db = client['my_test']
    test_collection = test_db['timestamptest']
    rs = test_collection.find().limit(100).sort("_id")
    for item in rs:
        struct_time = item['_id'].generation_time.timetuple()
        timestamp = time.mktime(struct_time)
        print timestamp
        print time.asctime(struct_time)


def search_object_in_doc():
    test_db = client.tweets_database
    test_collection = test_db['tweets-2010-05 ']
    rs = test_collection.find({"user.name": "袁腾飞"})
    for item in rs:
        print item['user']['name']


def use_update_oprate_array():
    db = client['test']
    collect = db['test']
    # 插入测试数据
    # list = []
    # for i in range(20):
    #     list.append(i)
    # doc = {
    #     "array": list
    # }
    # collect.insert_one(doc)
    # 增加test1字段
    # collect.update({},{"$set":{"name":"test1"}})
    # 修改name的值为changed
    # collect.update({"name":"test1"},{"$set":{"name":"changed"}})
    # 数组中元素增加
    # collect.update({"name": "changed"}, {"$push": {"array": 21}})
    # 使用addToSet可以避免插入相同的元素,再次向数组中添加元素21,添加22元素便会继续增加
    # collect.update({"name": "changed"}, {"$addToSet":{"array":21}})
    # collect.update({"name": "changed"}, {"$addToSet": {"array": 22}})
    # 移除数组中的元素，可以将数组当做栈和队列使用pop和push，通过key可以指定出发端执行
    # pop key 为 -1 从数组头部开始删除，1 则从尾部
    # collect.update({"name": "changed"}, {"$pop": {"array": -1}})
    # collect.update({"name": "changed"}, {"$pop": {"array": 1}})
    # 使用pull则可以删除指定值,存在多个将会全部被删除
    # collect.update({"name": "changed"}, {"$push": {"array": 5}})
    collect.update({"name": "changed"}, {"$pull": {"array": 5}})


if __name__ == '__main__':
    use_update_oprate_array()

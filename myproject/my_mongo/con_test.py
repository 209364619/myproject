#!coding=utf-8

# 针对mongodb连接数进行的测试
# 结论：操作系统连接数限制导致mongo副本集无法创建足够连接数
# ulimit -n 65535 临时性增大操作系统连接数

from pymongo import MongoClient
import time


def without_close_client():
    for i in range(1, 1000, 1):
        # client = MongoClient(host="192.168.209.113", port=27017)
        client = MongoClient(host="192.168.8.200", port=27000)
        db = client['conn_test']
        collection = db['collection' + str(i)]
        collection.insert({"num": i})
        print i
        time.sleep(0.1)
        # client.close()


def close_client():
    for i in range(1, 1000, 2):
        # client = MongoClient(host="192.168.209.113", port=27017)
        client = MongoClient(host="192.168.8.200", port=27000)
        db = client['conn_test']
        collection = db['collection' + str(i)]
        collection.insert({"num": i})
        print i
        time.sleep(0.1)
        client.close()


if __name__ == '__main__':
    without_close_client()

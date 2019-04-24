# coding=utf-8
from pymongo import MongoClient
import pymongo
import json
from bson.objectid import ObjectId

client = MongoClient("192.168.8.200:27000")

target_db = client['single_cluster']
target_collection = target_db['clusters']


def move_to_one_collection():
    db = client['cluster_demo']
    collection_name_list = db.list_collection_names()
    for name in collection_name_list:
        collection = db[name]
        records = collection.find()
        for item in records:
            target_collection.insert_one(item)
    print 'finished'


def get_event_by_pagenum_pagesize(pagenum, pagesize, collection):
    '''
    获取事件,事件列表
    :param pagenum: 页码
    :param pagesize: 页显示条数
    :param collection: 对应事件数据库
    :return: str(json) 事
                id：     事件唯一标识
                tweet：   事件推文概览
                summary：关键词概要
    '''
    records = target_collection.find().skip((pagenum - 1) * pagesize).limit(pagesize).sort("_id", pymongo.ASCENDING)
    events_list = []
    for record in records:
        simple_msg = {}
        simple_msg['id'] = str(record.get("_id"))
        simple_msg['tweet'] = record.get('tweet_list')[0]['text']
        simple_msg['keyword'] = record.get('summary').get('keywords')
        if len(simple_msg['keyword']) > 15:
            simple_msg['keyword'] = simple_msg['keyword'][0:15]
        events_list.append(simple_msg)
    print json.dumps(events_list, indent=4, ensure_ascii=False)


def get_tweets_by_id(obj_id, page_num=1, pagesize=10):
    obj_id = ObjectId(obj_id)
    event = target_collection.find_one({'_id': obj_id})
    tweets_list = []
    if event is not None:
        tweets = event.get('tweet_list')
        paged_tweets = tweets[(page_num - 1) * pagesize:page_num * pagesize]
        for item in paged_tweets:
            pass
        # print paged_tweets


if __name__ == '__main__':
    get_event_by_pagenum_pagesize(2, 10, target_collection)
    # id = "5baf287917cc126f44e3bb55"
    # get_tweets_by_id(id)

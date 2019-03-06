# coding=utf-8
'''
使用tweets  api进行数据采集
'''

from TwitterAPI import TwitterAPI, TwitterRestPager
import json
from tweets_api import api_list


class Tweets:
    consumer_key = api_list[1]["consumer_key"]
    consumer_secret = api_list[1]["consumer_secret"]
    access_token_key = api_list[1]["access_token"]
    access_token_secret = api_list[1]["access_token_secret"]

    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

    def get_tweet_by_key_word(self, keyword, num):
        result = {}
        try:
            r = self.api.request('search/tweets', {'q': keyword, "count": num})
            self.store_tweets_into_mongo(r)
            result['status'] = 'success'
        except:
            result['status'] = 'false'
            result['tweets'] = r
        return result

    def store_tweets_into_mongo(self, result):
        # 获取数据库连接
        db = self.get_Mongo_client()
        import datetime
        collection_name = datetime.datetime.now().strftime('%Y-%m')
        collection = db[collection_name]
        # 记录逐条存入数据库,如果推文id存在则不再重复插入
        for item in result.get_iterator():
            collection.insert_one(item)

    def get_Mongo_client(self):
        from pymongo import MongoClient
        from myproject import properties
        client = MongoClient(properties.MONGO_ADDR, properties.MONGO_PORT)
        db = client[properties.TWEETS_DB_NAME]
        return db


if __name__ == '__main__':
    test = Tweets()
    test.get_tweet_by_key_word("banana", 6)

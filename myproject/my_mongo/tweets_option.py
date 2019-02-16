# coding =utf-8
from pymongo import MongoClient
from myproject.properties import MONGO_ADDR, MONGO_PORT, TWEETS_DB_NAME


class TweetsOperate:
    client = MongoClient(MONGO_ADDR, MONGO_PORT)
    db = client[TWEETS_DB_NAME]

    def store_origin_tweets(self, collection_name, doc):
        collection = self.db[collection_name]
        collection.insert_one(doc)
        return True


if __name__ == '__main__':
    op = TweetsOperate()
    op.store_origin_tweets("test", {"test": "info"})

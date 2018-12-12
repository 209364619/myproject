from pymongo import MongoClient
from myproject.my_kafka import study_kafka_producer

MONGO_HOST = "192.168.209.110"
MONGO_PORT = 27017
MONGO_DB = "test"
MONGO_COLLECTION = "politics_users"

mongo_client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
db = mongo_client[MONGO_DB]
collection = db[MONGO_COLLECTION]

rs = collection.find().limit(5)
for user in rs:
    # print user, type(user)
    msg = user['description']
    # print type(msg), msg
    study_kafka_producer.my_producer(msg)

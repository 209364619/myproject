from pyspark.sql.types import Row
from pymongo import MongoClient

client = MongoClient("192.168.1.165:27017")
db = client['test']
collection = db['rs']

list1 = ["1", "2", "3"]
for i in list1:
    print i
list2 = [('this', 3), ('orange', 1), ('is', 3), ('apple', 1), ('banana', 1)]
import json

for i in list2:
    print i
    record = {i[0]: i[1]}
    print record
    collection.insert(record)

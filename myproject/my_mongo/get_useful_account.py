# coding=utf-8
# 通过上级标签获得小标签
# 遍历数据库查看标签小标签是否合适
# 符合条件记录入库存储
#                600        760        680        660         740
from pymongo import MongoClient
import threading
import json

label_db = "zwy_test"
label_collection = "label_management"
uplabel_dict = {u'国际政要': 500, u'国防军事': 500, u'国家安全': 500, u'新闻媒体': 500, u'智库与智库人员': 500, u'新闻媒体从业者': 500}

client = MongoClient(host="192.168.8.200", port=27000)
db = client[label_db]
collection = db[label_collection]


def get_labels(uplabel):
    simple_labels_list = []
    values = collection.find_one({"label_type": "base_type"})['value']
    labels_complex_list = values[uplabel]
    for item in labels_complex_list:
        simple_labels_list.append(item['english'])
    return simple_labels_list


def get_users(num, label_list):
    db_name = 'labeled_users'
    collection_name = 'labeled_user'
    db = client[db_name]
    collection = db[collection_name]
    count = 0

    target_db = client['target_user']
    target_collection = target_db['labeled_user']

    for user in collection.find({}):
        # print json.dumps(item, ensure_ascii=False, indent=4, encoding='utf-8')
        if count < num:
            for label in user['category_by_user'][0]['labels']:
                if label in label_list:
                    try:
                        target_collection.insert_one(user)
                        count += 1
                        break
                    except:
                        break

    print threading.currentThread().getName(), "存储完成！"


if __name__ == '__main__':
    for key in uplabel_dict:
        label_list = get_labels(key)
        t = threading.Thread(target=get_users, args=(uplabel_dict[key], label_list))
        t.start()
    print "Main thread: 结束"

    # target_db = client['target_user']
    # target_collection = target_db['labeled_user']
    # body = {
    #     "_id": "5c6f6853761f545b8086c0ef",
    #     "test": "test_info"
    # }
    #
    # body = target_collection.find_one({"test":{"$exists":"true"}})
    # try:
    # print target_collection.insert_one(document=body)
    # exception:
    #     pass

# coding=utf-8
mongo_host = "10.10.10.50"


# mongo_host = "192.168.209.113"
def read_mongo_user_id_import_image_to_hbase():
    from pymongo import MongoClient
    client = MongoClient(host=mongo_host, port=27000)
    db = client['tw_user_database']
    collections = db.list_collection_names()
    count = 0
    for collect_name in collections:
        collection = db[collect_name]
        user_list = collection.find()
        for user in user_list:
            count += 1
            if count % 1000 == 0:
                print "1000"
            info = {}
            user_id = user['id']
            info['rowkey'] = str(user_id) + ".jpg"
            from get_image_name import get_random_image
            info['path'] = get_random_image()
            from upload_hbase import upLoadByRowKeyAndPath
            upLoadByRowKeyAndPath(info)
    print '导入数量：', count


read_mongo_user_id_import_image_to_hbase()

#!coding=utf-8
from pymongo import MongoClient


def get_four_list():
    client = MongoClient("192.168.8.200", 27000)
    # 获取156个用户分成4个列表
    userlist1 = []
    userlist2 = []
    userlist3 = []
    userlist4 = []
    db = client['labeled_users']
    collection = db['labeled_user']
    users = collection.find().limit(126)
    count = 0


if __name__ == '__main__':
    get_four_list()

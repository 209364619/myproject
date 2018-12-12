#!coding=utf-8
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase

# server端地址和端口,web是HMaster也就是thriftServer主机名,9090是thriftServer默认端口
transport = TSocket.TSocket(host='10.10.10.50', port=9090)
# transport.setTimeout(5000)
# 传输方式
trans = TTransport.TBufferedTransport(transport)
# 传输协议
protocol = TBinaryProtocol.TBinaryProtocol(trans)
# 确认客户端
client = Hbase.Client(protocol)
# 打开连接
transport.open()

from hbase.ttypes import ColumnDescriptor, Mutation, BatchMutation, TRegionInfo
from hbase.ttypes import IOError, AlreadyExists

# 设置列簇
# col_family = ColumnDescriptor(name='content')
# 创建表结构
# client.createTable(tableName='twitter_images', columnFamilies=[col_family])
# tables = client.getTableNames()
# print tables
#


# mutations = [Mutation(column="image", value="1")]
# client.mutateRow('twitter', row, mutations)
# print client.getColumnDescriptors('twitter')
# print client.getTableRegions('test')
# print client.getColumnDescriptors('test')
# mutations = Mutation(column='col_family:col_1', value="1")
# rowkey = '1'
# client.mutateRow("test", rowkey, [mutations])
# print client.getRowWithColumns('test', 'row1', 'twitter_images:image')
# 从本地目录文件读取图片上传到hbase中
import os


# count =0
# for filename in os.listdir("I:\\hph\\all_images\\"):              #listdir的参数是文件夹的路径
#      filepath = "I:\\hph\\all_images\\"+ filename
#      fh = open(filepath, 'rb').read()
#      mutations = Mutation(column="content:image", value=fh)
#      client.mutateRow("twitter_images", filename, [mutations])
#      count+=1
# print count
#
# fh = open("I:\\hph\\all_images\\761563271702937600.jpg", 'rb').read()
# mutations = Mutation(column="content:image", value=fh)
# client.mutateRow("twitter_images", "17685258.jpg", [mutations])
# print client.getRow('twitter_images', '25073877.jpg')

def read_mongo_user_id_import_image_to_hbase():
    from pymongo import MongoClient
    client = MongoClient(host="10.10.10.50", port=27000)
    db = client['tw_user_database']
    collections = db.list_collection_names()
    for collect_name in collections:
        collection = db[collect_name]
        print collection, type(collection)


read_mongo_user_id_import_image_to_hbase()

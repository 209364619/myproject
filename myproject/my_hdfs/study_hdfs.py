# coding=utf-8
from hdfs import *

host1 = "http://192.168.8.200:50070"
host2 = "http://192.168.209.110:50080"
hdfs_client = Client(host2, root='/', timeout=100, session=False)
# print "支持的方法"
# print dir(hdfs_client)
#
print '根目录文件查看：'
# status True 包括子目录输出  False （默认）只显示当前
dirs = hdfs_client.list("/", status=True)
print type(dirs), dirs

with hdfs_client.read('/input.txt') as reader:
    for line in reader:
        print type(line), line
#
# print("路径文件信息查看")
# # strict True:路径不存在抛出异常
# #       False：路径不存在返回None
# print hdfs_client.status("/", strict=False)
#
# hdfs_client.makedirs('644', permission=644)
#
# print("重命名：")
# hdfs_client.rename("/644", "/rename")

# hdfs_client.set_permission("/rename", permission=777)
# hdfs_client.upload("/rename", "C:\Users\y500\Desktop\TensorFlow.html")

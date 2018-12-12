# coding=utf-8
from hdfs import *

hdfs_client = Client("http://192.168.1.231:50070", root='/', timeout=100, session=False)
# print "支持的方法"
# print dir(hdfs_client)
#
print '根目录文件查看：'
# status True 包括子目录输出  False （默认）只显示当前
dirs = hdfs_client.list("/", status=True)
print dirs, type(dirs)
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
hdfs_client.upload("/rename", "C:\Users\y500\Desktop\TensorFlow.html")

#!coding = utf-8
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import ColumnDescriptor, Mutation, BatchMutation, TRegionInfo

socket = TSocket.TSocket(host='192.168.8.200', port=9090)
# socket.setTimeout(5000)

transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)

client = Hbase.Client(protocol)
socket.open()

print(client.getTableNames())

print("图片上传！！！")
rowkey = "3193822087.jpg"
print(rowkey, type(rowkey))
key_type = "<class 'str'>"
print(key_type)

if isinstance(rowkey, bytes):
    print("this is str")
path = "C:\\Users\\y500\\Desktop\\timg.jpg"
fh = open(path, 'rb').read()
mutations = Mutation(column="content:image", value=fh)
client.mutateRow("twitter_images", rowkey, [mutations])
print("上传成功")

# rowkey = "3193822087.jpg".encode('utf-8')
# print(rowkey,type(rowkey))
# if isinstance(rowkey,bytes):
#     rowkey = str(rowkey,encoding='utf-8')
# print(type(rowkey),rowkey)

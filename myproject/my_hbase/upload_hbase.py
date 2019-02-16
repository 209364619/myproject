#!coding=utf-8
from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from hbase import Hbase
from hbase.ttypes import ColumnDescriptor, Mutation, BatchMutation, TRegionInfo
from hbase.ttypes import IOError, AlreadyExists

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
print client.getTableNames()


def upLoadByRowKeyAndPath(info):
    rowkey = info['rowkey']
    path = info['path']
    fh = open(path, 'rb').read()
    mutations = Mutation(column="content:image", value=fh)
    client.mutateRow("twitter_images", rowkey, [mutations])

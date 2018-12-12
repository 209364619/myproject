# coding=utf-8
from thrift.transport import TSSLSocket
from thrift.transport.TTransport import TBufferedTransport
from thrift.protocol import TBinaryProtocol

from hbase import Hbase
from hbase.ttypes import ColumnDescriptor
from hbase.ttypes import Mutation


class HBaseClient(object):
    def__init__(self, ip, port=9090):
    self.__transport = TBufferedTransport(T)

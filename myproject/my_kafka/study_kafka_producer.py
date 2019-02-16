# coding=utf-8
import time
from pykafka import KafkaClient

# hosts='192.168.1.165:9092',
# kafka_client = KafkaClient(zookeeper_hosts='192.168.1.165:2181')
#
# topic = kafka_client.topics["python_topic"]
#
# partitions = topic.partitions
# print (u"查看所有分区 {}".format(partitions))
#
#
# producer = topic.get_sync_producer()
# msg = "this is a message created for test"
# producer.produce(msg)
#
# consumer = topic.get_simple_consumer(consumer_group='mygroup')

import json
from kafka import KafkaProducer

IPADDR = "192.168.209.110:9092"


# IPADDR="192.168.1.165:9092"

def my_producer(msg):
    msg = msg.encode('utf-8')
    producer = KafkaProducer(bootstrap_servers=IPADDR)
    producer.send('new_test', msg, partition=0)
    producer.close()


my_producer("xixi")

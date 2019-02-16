from kafka import KafkaConsumer

IPADDR = "192.168.209.110:9092"
consumer = KafkaConsumer('new_test', bootstrap_servers=IPADDR)
for msg in consumer:
    # recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print type(msg), msg
    print msg.value

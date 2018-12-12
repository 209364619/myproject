from pyspark import SparkContext, SparkConf

conf = SparkConf()
conf.setAppName("first test in node110")
conf.setMaster("spark://192.168.209.110:7077")
sc = SparkContext(conf=conf)
lines = sc.textFile("hdfs://192.168.209.110:8020/input.txt")
words = lines.flatMap(lambda line: line.split(" "))
keyvalue = words.map(lambda word: (word, 1))
result = keyvalue.reduceByKey(lambda x, y: x + y)

print(result.collect())

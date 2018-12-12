from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import DataFrame
from pyspark import SparkContext, SparkConf
from pymongo import MongoClient

client = MongoClient("192.168.1.165:27017")
db = client['test']
collection = db['rs']

# sc = SparkContext()
# ctx = SQLContext(sc)
# test_collection = ctx.read.format("com.mongodb.spark.sql").options(uri="mongodb://192.168.209.110:27017", database="test", collection="politics_users").load()
# test_collection.printSchema()
# test_collection.first()

input_uri = "mongodb://192.168.1.165:27017/test.politics_users"
output_uri = "mongodb://192.168.1.165:27017/test.rs"
# input_uri = "mongodb://192.168.209.110:27017/test.fruit"
# output_uri = "mongodb://192.168.209.110:27017/test.rs"

my_spark = SparkSession \
    .builder \
    .appName("MyApp") \
    .config("spark.mongodb.input.uri", input_uri) \
    .config("spark.mongodb.output.uri", output_uri) \
    .config('spark.jars.packages', "org.mongodb.spark:mongo-spark-connector_2.11:2.3.0") \
    .getOrCreate()

# dataframe = my_spark.read.format('com.mongodb.spark.sql.DefaultSource').load()
# dataframe.first()

fruit = my_spark.read.format('com.mongodb.spark.sql.DefaultSource').option("database", "test").option("collection",
                                                                                                      "fruit").load()
# fruit.createTempView("temp")
# name_df = my_spark.sql("select type from temp")

# name_df = fruit.type

# name_df = fruit['type']

# name_df = fruit.select('type')
# rs = name_df.groupBy('type').count()
# print rs.collect()

# fruit_name_col=fruit['type']
# print type(fruit_name_col)
# print fruit_name_col
#
# def word_count():


# filter
# fruit.filter(fruit['qty']>=10).show()

# SQL
# fruit.createOrReplaceTempView("temp")
# some_fruit = my_spark.sql("select type,qty from temp where type='apple'")
# some_fruit.show()
import json


def get(line):
    print line, type(line)
    line_str = line.asDict()
    value = line_str['describe'].encode('utf-8')
    rs = value.split(" ")
    print rs, type(value)
    return rs


def word_count():
    fruit.show()
    fruit.createTempView('temp')
    col_df = my_spark.sql('select describe from temp')
    print type(col_df)
    col_df.show()
    my_rdd = col_df.rdd

    words = my_rdd.flatMap(lambda line: get(line))
    keyvalue = words.map(lambda word: (word, 1))
    result = keyvalue.reduceByKey(lambda x, y: x + y)

    print(result.collect())
    # describes_col = fruit["describe"]

    # print type(describes_df)


word_count()

from pyspark import SparkContext, SparkConf

conf = SparkConf.setAppName().setMaster()
sc = SparkContext(conf)

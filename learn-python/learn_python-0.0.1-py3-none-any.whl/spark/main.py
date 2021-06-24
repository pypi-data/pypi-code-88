import pyspark
from pyspark.sql import SparkSession


conf = pyspark.SparkConf()
conf.setMaster('local[*]')

spark = SparkSession.builder \
      .appName("test-app") \
      .config(conf=conf) \
      .getOrCreate()


def hello_spark():
    txt = spark.sparkContext.textFile("file:///E:/DEV/dev-python/learn-python/src/spark/test.txt")
    print(txt.count())
    python_lines = txt.filter(lambda line: 'python' in line.lower())
    print(python_lines.count())


def odds_number():
    big_list = range(10000)
    rdd = spark.sparkContext.parallelize(big_list, 2)
    odds = rdd.filter(lambda item: item % 2 != 0)
    return odds.take(5)


if __name__ == '__main__':

    print("Start")
    x = ['Python', 'programming', 'is', 'awesome!']
    print(list(filter(lambda arg: len(arg) < 8, x)))
    hello_spark()
    print(odds_number())
    print("End")

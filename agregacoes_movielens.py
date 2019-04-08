from pyspark.sql import SparkSession
import pyspark.sql.functions as f

# cria o sparkSession
spark = SparkSession \
    .builder \
    .appName("agregações no dataset movielens") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# le o arquivo csv
rdd = spark.read.csv("ratings.csv", sep=",", header="true", inferSchema="true")
print()

# novo dataframe com agrupamentos, filtros e ordenação
rdd2 = rdd.groupBy("movieId") \
    .agg(f.sum("rating").alias("sum_rating"),
         f.max("rating").alias("max_rating"),
         f.min("rating").alias("min_rating"),
         f.round(f.avg("rating"), 3).alias("avg_rating")) \
    .filter(rdd["movieId"].between(10, 20)) \
    .orderBy(rdd["movieId"])

# cria outro dataframe com filtro e ordenação
rdd3 = rdd.filter(rdd["userId"].isin(1, 10, 100, 1000) & rdd["movieId"].between(10, 20)) \
    .orderBy(rdd["movieId"])

# imprime os dataframe
print(rdd2.show())
print(rdd3.show())

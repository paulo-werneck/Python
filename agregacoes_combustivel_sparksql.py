#!/usr/bin/python3

"""
Autor: Paulo Werneck
Data: 21/03/2019

Analise descritiava usando pyspark para analisar dataset de posto de gasolina de combustível

Input: Dataset do site dados.gov.br (http://dados.gov.br/dataset/infopreco)
Output: Agregações por postos e por combustíveis
""""

import os
from pyspark.sql import SparkSession
from pyspark.sql.types import FloatType, TimestampType
from pyspark.sql.functions import udf, countDistinct, round
from datetime import datetime

# setando as variaveis do spark
os.environ["PYSPARK_PYTHON"] = "/home/werneck/anaconda3/envs/Python-37-Labs/bin/python3.7"
os.environ["SPARK_HOME"] = "/home/werneck/spark-2.4.0-bin-hadoop2.7"

# cria o sparkSession
spark = SparkSession \
    .builder \
    .appName("Agregações dos preços de combustíveis") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# cria um DataFrame a partir do dataset de combustivel
df = spark.read.csv("../infopreco_utf8.csv", sep=";", header=True)

# cria e transforma a funcao em uma funcao udf
udf_comma_to_dot = udf(lambda s: float(s.replace(',', '.')), FloatType())
udf_text_to_date = udf(lambda s: datetime.strptime(s, "%d/%m/%Y %H:%M"), TimestampType())

# substitui a coluna por uma de mesmo nome aplicando a funcao
df = df.withColumn("VALOR_VENDA", udf_comma_to_dot(df["VALOR_VENDA"]))
df = df.withColumn("DATA_CADASTRO", udf_text_to_date(df["DATA_CADASTRO"]))

# Quantitativo de postos para analise
df_count_posto = df.agg(countDistinct("CNPJ").alias("QTD_POSTOS")).show()

# tipos de combustiveis disponiveis para analise
df_tipo_combustivel = df.select("PRODUTO").distinct().orderBy("PRODUTO").show(truncate=False)

# media dos precos por estado por combustivel
df_media_preco_uf = df.groupBy("UF") \
    .pivot("PRODUTO") \
    .avg("VALOR_VENDA") \
    .select("UF",
            round("Diesel S10", 3).alias("Diesel_S10"),
            round("Diesel S500", 3).alias("Diesel_S500"),
            round("Etanol", 3).alias("Etanol"),
            round("GNV", 3).alias("GNV"),
            round("Gasolina C Comum", 3).alias("Gasolina_Comum")) \
    .orderBy("Gasolina_Comum", ascending=False) \
    .show(30)

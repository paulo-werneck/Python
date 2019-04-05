"""
Paulo Werneck
03/04/2019

Classe com estatistíscias descritivas

IN: Conexão teradata
OUT: aggregações em pyspark
"""

from teradata_gpa.connection_teradata import Connection
from pyspark.sql import SparkSession


class Aggregations(Connection):

    def __init__(self):
        super().__init__()

    def query_fato_fm16(self, cod_loja, dat_apur_venda_inicio, dat_apur_venda_fim, cod_transac_venda):
        query = 'SELECT * FROM DP_TEDW.FM16_MOV_VEND_CRM ' \
                'WHERE COD_LOJA = {0} ' \
                'AND DAT_APURACAO_VENDA BETWEEN {1} AND {2} ' \
                'AND COD_TRANSAC_VENDA = {3} ' \
                'ORDER BY NUM_LNH_TRANSAC_VENDA'.format(cod_loja, dat_apur_venda_inicio,
                                                        dat_apur_venda_fim, cod_transac_venda)
        return Connection.connection_gpa(self).cursor().execute(query).fetchall()


if __name__ == '__main__':

    a = Aggregations()
    result = a.query_fato_fm16(1, 1181201, 1181231, 8173178654)

    # cria o sparkSession
    spark = SparkSession \
        .builder \
        .appName("Analises descritivas de lojas utilizando pyspark") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    df = spark.createDataFrame(result, )
    df.printSchema()

    #print(df.show())

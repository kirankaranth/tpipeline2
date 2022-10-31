from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from job.config.ConfigStore import *
from job.udfs.UDFs import *

def Orders(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(StructType([StructField("testddd", StringType(), True)]))\
        .option("header", True)\
        .option("sep", ",")\
        .csv("https://kiran.com")

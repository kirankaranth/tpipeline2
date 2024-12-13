from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from ppp1.config.ConfigStore import *
from ppp1.functions import *

def Lookup_1(spark: SparkSession, in0: DataFrame):
    keyColumns = []
    valueColumns = []
    createLookup("", in0, spark, keyColumns, valueColumns)

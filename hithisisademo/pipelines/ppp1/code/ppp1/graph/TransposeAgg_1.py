from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from ppp1.config.ConfigStore import *
from ppp1.functions import *

def TransposeAgg_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.agg()

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from ppp1.config.ConfigStore import *
from ppp1.functions import *
from prophecy.utils import *
from ppp1.graph import *

def pipeline(spark: SparkSession) -> None:
    Lookup_1(spark)
    df_TransposeAgg_1 = TransposeAgg_1(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("ppp1")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/ppp1")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/ppp1", config = Config)(pipeline)

if __name__ == "__main__":
    main()

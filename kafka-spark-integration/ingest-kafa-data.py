import logging
from pyspark.sql import SparkSession


def run_spark_job(spark):
    #TODO set this entry point so that you can start ingesting kafka data 
    # set to use the Kafka Server Port#
    # set the topic name you are subscribing to; to be something you called in your producer 
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "uber.event.pickup") \
        .option("startingOffsets", "earliest") \
        .option("maxOffsetsPerTrigger", 10) \
        .option("stopGracefullyOnShutdown", "true") \
        .load()


    # Show schema for the incoming resources for checks
    df.printSchema()


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("StructuredStreamingSetup") \
        .getOrCreate()

    logger.info("Spark started")


    spark.stop()

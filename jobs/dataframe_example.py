from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName("demo").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    df = spark.createDataFrame(
        [("Sue", 28), ("Jake", 35), ("Alice", 45)], ["name", "age"]
    )

    df.show()

    spark.stop()


if __name__ == "__main__":
    main()

from pyspark.sql.types import StructField, StructType, StringType, FloatType

breed_schema = StructType(
    [
        StructField("breed", StringType(), False),
        StructField("proportion", FloatType(), False),
    ]
)

from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    FloatType,
    ArrayType,
)
from .cow import cow_schema


herd_schema = StructType(
    [
        StructField("herdIdentifier", IntegerType(), False),
        StructField("name", StringType(), True),
        StructField("sourceId", IntegerType(), True),
        StructField("dataProviderGuid", StringType(), True),
        StructField("street", StringType(), True),
        StructField("number", StringType(), True),
        StructField("registrationNumber", StringType(), True),
        StructField("zip", StringType(), True),
        StructField("city", StringType(), True),
        StructField("state", StringType(), True),
        StructField("country", StringType(), True),
        StructField("countryCode", StringType(), True),
        StructField("latitude", FloatType(), True),
        StructField("longitude", FloatType(), True),
        StructField("email", StringType(), True),
        StructField("mobilePhoneNumber", StringType(), True),
        StructField("telephoneNumber", StringType(), True),
        StructField("cows", ArrayType(cow_schema), False),
    ]
)

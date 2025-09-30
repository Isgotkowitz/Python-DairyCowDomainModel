from pyspark.sql.types import (
    StructField,
    StructType,
    IntegerType,
    StringType,
    TimestampType,
    ArrayType,
    BooleanType,
)

from .breed_part import breed_schema
from .timeline_event import timeline_event_schema


cow_schema = StructType(
    [
        StructField("animal_id", IntegerType(), False),
        StructField("gender", StringType(), False),
        StructField("birth_date", TimestampType(), False),
        StructField("current_status", StringType(), False),
        StructField("breed", ArrayType(breed_schema), False),
        StructField("timeline_events", ArrayType(timeline_event_schema), False),
        StructField("animalEarTag", StringType(), True),
        StructField("animalFarmName", StringType(), True),
        StructField("animalFarmNumber", IntegerType(), True),
        StructField("geneticDamEarTag", StringType(), True),
        StructField("geneticDamIdentifier", IntegerType(), True),
        StructField("sireEarTag", StringType(), True),
        StructField("sireIdentifier", IntegerType(), True),
        StructField("animalLegalIdentifier", StringType(), True),
        StructField("animalISORFIDStartingManufacturer", StringType(), True),
        StructField("animalISORFIDStartingCountryCode", StringType(), True),
        StructField("animalHerdBookName", StringType(), True),
        StructField("animalUSDA", StringType(), True),
        StructField("animalDHIA", StringType(), True),
        StructField("recipientDamIdentifier", IntegerType(), True),
        StructField("bornOnFarm", BooleanType(), True),
    ]
)

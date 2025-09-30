from pyspark.sql.types import (
    StructField,
    StructType,
    StringType,
    IntegerType,
    FloatType,
    TimestampType,
    BooleanType,
)


timeline_metadata_schema = StructType(
    [
        # Birth event
        StructField("calving_ease_type", StringType(), True),
        StructField("parturition_birth_status_type", StringType(), True),
        # Breeding event
        StructField("bull_indentifier", FloatType(), True),
        StructField("bull_ear_tag", StringType(), True),
        StructField("bull_name", StringType(), True),
        StructField("bull_number", FloatType(), True),
        StructField("insemination_number", IntegerType(), True),
        StructField("breeding_type", StringType(), True),
        StructField("reproduction_type", IntegerType(), True),
        StructField("gender_sorted", StringType(), True),
        # Calving event
        StructField("calving_ease_type", StringType(), True),
        StructField("parturition_birth_status_type", StringType(), True),
        # Exit event
        StructField("departure_type", StringType(), True),
        StructField("departure_reason", StringType(), True),
        # Dry Off
        # -- No fields --
        # Abortion
        # -- No fields --
        # Heat
        # -- No fields --
        # DNBdecision
        # -- No fields --
        # Milk recording event
        StructField("lactose_percentage", FloatType(), True),
        StructField("fat_percentage", FloatType(), True),
        StructField("protein_percentage", FloatType(), True),
        StructField("scc", IntegerType(), True),
        StructField("milking_yield", FloatType(), True),
        # Milk Meter Yield event
        StructField("milking_yield", FloatType(), True),
        StructField("start_time", TimestampType(), True),
        StructField("end_time", TimestampType(), True),
        StructField("robot_id", IntegerType(), True),
        StructField("robot_name", StringType(), True),
        StructField("failure", BooleanType(), True),
        StructField("refusal", BooleanType(), True),
        StructField("milking_speed", FloatType(), True),
        StructField("body_weight", IntegerType(), True),
        StructField("milking_session", IntegerType(), True),
        # Feed Intake Event
        StructField("product_id", IntegerType(), True),
        StructField("product_category", StringType(), True),
        StructField("feed_dry_matter_content_unit_id", IntegerType(), True),
        StructField("product_name", StringType(), True),
        StructField("intake_programmed_kg", FloatType(), True),
        StructField("intake_consumed_kg", FloatType(), True),
        StructField("feed_intake_session", IntegerType(), True),
        StructField("start_time", TimestampType(), True),
        StructField("end_time", TimestampType(), True),
    ]
)

timeline_event_schema = StructType(
    [
        StructField("event_type", StringType(), False),
        StructField("event_date", TimestampType(), False),
        StructField("metadata", timeline_metadata_schema, False),
    ]
)

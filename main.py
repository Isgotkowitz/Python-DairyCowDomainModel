from DairyCowDomainModel.cow import Cow
from DairyCowDomainModel.breed_part import BreedPart
from DairyCowDomainModel.enums import AnimalGender
from DairyCowDomainModel.raw_data_schema import RAW_COW_SCHEMA
from datetime import date

from pyspark.sql import SparkSession
from pyspark.sql.functions import arrays_zip, transform, struct


def _make_cow() -> Cow:
    breeds = [BreedPart("HOL", 0.75), BreedPart("JER", 0.25)]

    return Cow(
        animal_id=12,
        animal_ear_tag="NL5656",
        animal_farm_name="Josje",
        animal_farm_number=123,
        genetic_dam_ear_tag=None,
        genetic_dam_identifier=654,
        gender=AnimalGender.FEMALE,
        sire_ear_tag="NL223",
        birth_date=date(2022, 3, 1),
        breed=breeds,
    )


def main() -> None:
    spark = SparkSession.builder.master("local[*]").appName("pyDCDM_demo").getOrCreate()

    raw_df = spark.read.json(
        "data/prettyZoetisFirst10Rows.json", schema=RAW_COW_SCHEMA, multiLine=True
    )

    # raw_df.printSchema()

    complex_lactations = raw_df.select(
        "Lactations.complexLactations", "Lactations.lactationNumber"
    )

    # complex_lactations.printSchema()

    zipped_complex_lactations = complex_lactations.select(
        arrays_zip(
            complex_lactations.complexLactations, complex_lactations.lactationNumber
        )
    )
    # .alias("zippedComplexLacts") \

    zipped_complex_lactations.printSchema()

    _numbered_complex_lactations = (
        zipped_complex_lactations.withColumn(
            "arrays_zip(complexLactations, lactationNumber)",
            transform(
                "arrays_zip(complexLactations, lactationNumber)",
                lambda x: struct(
                    x["lactationNumber"].alias("lactationNumber"),
                    struct(
                        x["complexLactations"]["LactationDays"],
                        x["lactationNumber"].alias("lactationNumber"),
                    ).alias("complexLactations"),
                ),
            ),
        )
        .drop("lactationNumber")
        .printSchema()
    )

    spark.stop()


if __name__ == "__main__":
    main()

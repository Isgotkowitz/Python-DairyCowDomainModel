from DairyCowDomainModel.cow import Cow
from DairyCowDomainModel.breed_part import BreedPart
from DairyCowDomainModel.enums import AnimalGender
from datetime import date


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
    cow = _make_cow()

    print(cow)
    print("Cow created successfully.")


if __name__ == "__main__":
    main()

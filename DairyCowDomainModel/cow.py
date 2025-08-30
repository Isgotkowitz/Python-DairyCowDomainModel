from dataclasses import dataclass, field
from datetime import date

from .breed_part import BreedPart
from .enums import AnimalGender
from .timeline_event import TimelineEvent


@dataclass
class Cow:
    animal_id: int
    gender: AnimalGender
    birth_date: date
    animal_ear_tag: str | None = None
    animal_farm_name: str | None = None
    animal_farm_number: int | None = None
    genetic_dam_ear_tag: str | None = None
    genetic_dam_identifier: int | None = None
    sire_ear_tag: str | None = None
    sire_identifier: int | None = None
    animal_legal_identifier: str | None = None
    animal_iso_rfid_starting_manufacturer: str | None = None
    animal_iso_rfid_starting_country_code: str | None = None
    animal_herd_book_name: str | None = None
    animal_usda: str | None = None
    animal_dhia: str | None = None
    recipient_dam_identifier: int | None = None

    breed: list[BreedPart] = field(default_factory=lambda: [BreedPart("HOL", 0.99)])
    born_on_farm: bool | None = None
    timeline_events: list[TimelineEvent] = field(default_factory=list)

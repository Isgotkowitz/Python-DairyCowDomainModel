from dataclasses import dataclass, field

from .cow import Cow


@dataclass
class Herd:
    herd_identifier: int
    name: str | None = None
    source_id: int | None = None
    data_provider_guid: str | None = None
    street: str | None = None
    number: str | None = None
    registration_number: str | None = None
    zip_code: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    country_code: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    email: str | None = None
    mobile_phone_number: str | None = None
    telephone_number: str | None = None
    cows: list[Cow] = field(default_factory=list)

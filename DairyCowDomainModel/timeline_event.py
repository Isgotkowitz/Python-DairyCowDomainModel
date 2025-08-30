from dataclasses import dataclass
from datetime import date, datetime

from .enums import (
    CalvingEaseType,
    ParturitionBirthStatusType,
    BreedingType,
    GenderSorting,
    DepartureType,
    DepartureReason,
)


@dataclass
class TimelineEvent:
    event_date: date

    @property
    def event_type(self) -> str:
        """Return class name as the event type string."""
        return self.__class__.__name__


@dataclass
class Birth(TimelineEvent):
    calving_ease_type: CalvingEaseType | None = None
    parturition_birth_status_type: ParturitionBirthStatusType | None = None


@dataclass
class Breeding(TimelineEvent):
    bull_identifier: int | None = None
    bull_ear_tag: str | None = None
    bull_name: str | None = None
    bull_number: int | None = None
    insemination_number: int | None = None
    breeding_type: BreedingType | None = None
    reproduction_type: int | None = None
    gender_sorted: GenderSorting | None = None


@dataclass
class Calving(TimelineEvent):
    calving_ease_type: CalvingEaseType | None = None
    parturition_birth_status_type: ParturitionBirthStatusType | None = None


@dataclass
class Exit(TimelineEvent):
    departure_type: DepartureType | None = None
    departure_reason: DepartureReason | None = None


@dataclass
class MilkRecording(TimelineEvent):
    lactose_percentage: float | None = None
    fat_percentage: float | None = None
    protein_percentage: float | None = None
    scc: int | None = None
    milking_yield: float | None = None


@dataclass
class MilkMeterYields(TimelineEvent):
    milking_yield: float | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None
    robot_id: int | None = None
    robot_name: str | None = None
    failure: bool | None = None
    refusal: bool | None = None
    milking_speed: float | None = None
    body_weight: int | None = None
    milking_session: int | None = None


@dataclass
class FeedIntake(TimelineEvent):
    product_id: int | None = None
    product_category: str | None = None
    feed_dry_matter_content_uni_id: int | None = None
    product_name: str | None = None
    intake_programmed_kg: float | None = None
    intake_consumed_kg: float | None = None
    feed_intake_session: int | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None


@dataclass
class Diagnosis(TimelineEvent):
    pass


@dataclass
class Treatment(TimelineEvent):
    pass


@dataclass
class Heat(TimelineEvent):
    pass


@dataclass
class Abortion(TimelineEvent):
    pass


@dataclass
class DryOff(TimelineEvent):
    pass


@dataclass
class DNBdecision(TimelineEvent):
    pass

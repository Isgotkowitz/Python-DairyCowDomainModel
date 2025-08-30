from enum import Enum


class AnimalGender(Enum):
    FEMALE = "Female"
    FEMALE_NEUTER = "FemaleNeuter"
    MALE = "Male"
    MALE_CRYPTORCHID = "MaleCryptorchid"
    UNKNOWN = "Unknown"


class BreedingType(Enum):
    ARTIFICIAL_INSEMINATION = "ArtificialInsemination"
    DO_IT_YOURSELF = "DoItYourself"
    NATURAL_SERVICE = "NaturalService"
    WITH_BULL = "WithBull"
    EMBRYO_TRANSFER = "EmbryoTransfer"


class GenderSorting(Enum):
    CONVENTIONAL = "Conventional"
    FEMALE_SORTED = "FemaleSorted"
    MALE_SORTED = "MaleSorted"
    UNKNOWN = "Unknown"


class CalvingEaseType(Enum):
    EASY_UNASSISTED = "EasyUnassisted"
    EASY_ASSISTED = "EasyAssisted"
    DIFFICULT_EXTRA_ASSISTANCE = "DifficultExtraAssistance"
    DIFFICULT_VETERINARY_CARE = "DifficultVeterinaryCare"
    CAESAREAN_OR_SURGERY = "CaesareanOrSurgery"


class ParturitionBirthStatusType(Enum):
    ALIVE = "Alive"
    STILLBORN = "Stillborn"
    ABORTED = "Aborted"
    DIED_BEFORE_TAGGING_DATE = "DiedBeforeTaggingDate"
    DIED_AFTER_TAGGING_DATE = "DiedAfterTaggingDate"
    SLAUGHTERED_AT_BIRTH = "SlaughteredAtBirth"
    EUTHANISED_AT_BIRTH = "EuthanisedAtBirth"


class DepartureType(Enum):
    DAIRY_SALE = "DairySale"
    SLAUGHTER = "Slaughter"
    DEATH = "Death"


class DepartureReason(Enum):
    AGE = "Age"
    SUPERFLUOUS = "Superfluous"
    SLAUGHTER = "Slaughter"
    SALE = "Sale"
    NEWBORN = "Newborn"
    LEG_OR_CLAW = "LegOrClaw"
    NUTRITION = "Nutrition"
    PARTURITION = "Parturition"
    MASTITIS = "Mastitis"
    FERTILITY = "Fertility"
    HEALTH = "Health"
    PRODUCTION = "Production"
    MILKING_ABILITY = "MilkingAbility"
    BAD_TYPE = "BadType"
    BEHAVIOUR = "Behaviour"
    OTHER = "Other"
    UNKNOWN = "Unknown"

from dataclasses import dataclass


class BreedPart(dataclass):
    breed: str
    proportion: float

    def __post_init__(self) -> None:
        if not (0.0 <= self.proportion <= 1.0):
            raise ValueError("Percentage must be between 0.0 and 1.0")

    def __str__(self) -> str:
        return f"{self.breed} {int(self.proportion * 100)}%"

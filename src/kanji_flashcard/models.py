from dataclasses import dataclass


@dataclass
class Kanji:
    character: str
    meanings: list[str]
    onyomi: list[str]
    kunyomi: list[str]

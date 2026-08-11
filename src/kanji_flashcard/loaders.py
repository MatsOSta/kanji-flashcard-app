import json
from pathlib import Path

from kanji_flashcard.models import Kanji


def load_kanji(path: str | Path) -> list[Kanji]:
    with Path(path).open(encoding="utf-8") as json_file:
        records = json.load(json_file)

    return [Kanji(**record) for record in records]

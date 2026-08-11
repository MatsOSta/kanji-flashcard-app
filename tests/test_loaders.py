from pathlib import Path

from kanji_flashcard.loaders import load_kanji
from kanji_flashcard.models import Kanji


def test_load_kanji_returns_kanji_from_json_file() -> None:
    fixture_path = Path(__file__).parent / "fixtures" / "kanji.json"

    kanji = load_kanji(fixture_path)

    assert kanji == [
        Kanji("日", ["day", "sun"], ["ニチ", "ジツ"], ["ひ", "か"]),
        Kanji("月", ["month", "moon"], ["ゲツ", "ガツ"], ["つき"]),
    ]

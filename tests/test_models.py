from kanji_flashcard.models import Kanji


def test_kanji_stores_character_meanings_and_readings() -> None:
    kanji = Kanji(
        character="日",
        meanings=["day", "sun"],
        onyomi=["ニチ", "ジツ"],
        kunyomi=["ひ", "か"],
    )

    assert kanji.character == "日"
    assert kanji.meanings == ["day", "sun"]
    assert kanji.onyomi == ["ニチ", "ジツ"]
    assert kanji.kunyomi == ["ひ", "か"]


def test_kanji_instances_with_the_same_values_are_equal() -> None:
    first = Kanji("日", ["day", "sun"], ["ニチ", "ジツ"], ["ひ", "か"])
    second = Kanji("日", ["day", "sun"], ["ニチ", "ジツ"], ["ひ", "か"])

    assert first == second

from pathlib import Path

from kanji_flashcard.cli import main


def test_main_prints_placeholder_message(capsys) -> None:
    main([])

    captured = capsys.readouterr()
    assert captured.out == "Kanji Flashcard App is ready.\n"


def test_study_reveals_first_kanji_after_input(capsys) -> None:
    fixture_path = Path(__file__).parent / "fixtures" / "kanji.json"
    input_was_requested = False

    def press_enter() -> str:
        nonlocal input_was_requested
        input_was_requested = True
        return ""

    main(["study", str(fixture_path)], read_input=press_enter)

    captured = capsys.readouterr()
    assert input_was_requested
    assert captured.out == (
        "日\n"
        "Press Enter to reveal the answer.\n"
        "Meanings: day, sun\n"
        "Onyomi: ニチ, ジツ\n"
        "Kunyomi: ひ, か\n"
    )

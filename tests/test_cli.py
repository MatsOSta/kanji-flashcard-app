from pathlib import Path

from kanji_flashcard.cli import main


def test_main_prints_placeholder_message(capsys) -> None:
    main([])

    captured = capsys.readouterr()
    assert captured.out == "Kanji Flashcard App is ready.\n"


def test_study_reveals_each_kanji_in_file_order(capsys) -> None:
    fixture_path = Path(__file__).parent / "fixtures" / "kanji.json"
    responses = iter(["", "y", "", "n"])

    main(["study", str(fixture_path)], read_input=lambda: next(responses))

    captured = capsys.readouterr()
    assert captured.out == (
        "日\n"
        "Press Enter to reveal the answer.\n"
        "Meanings: day, sun\n"
        "Onyomi: ニチ, ジツ\n"
        "Kunyomi: ひ, か\n"
        "Did you know it? [y/n]:\n"
        "月\n"
        "Press Enter to reveal the answer.\n"
        "Meanings: month, moon\n"
        "Onyomi: ゲツ, ガツ\n"
        "Kunyomi: つき\n"
        "Did you know it? [y/n]:\n"
        "Study complete.\n"
        "Total Kanji studied: 2\n"
        "Known: 1\n"
        "Unknown: 1\n"
    )


def test_study_asks_again_after_an_invalid_answer(capsys) -> None:
    fixture_path = Path(__file__).parent / "fixtures" / "kanji.json"
    responses = iter(["", "maybe", "y", "", "n"])

    main(["study", str(fixture_path)], read_input=lambda: next(responses))

    captured = capsys.readouterr()
    assert captured.out.count("Did you know it? [y/n]:\n") == 3


def test_study_reports_an_empty_dataset(capsys) -> None:
    fixture_path = Path(__file__).parent / "fixtures" / "empty_kanji.json"

    main(["study", str(fixture_path)])

    captured = capsys.readouterr()
    assert captured.out == "There are no Kanji to study.\n"

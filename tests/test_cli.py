from kanji_flashcard.cli import main


def test_main_prints_placeholder_message(capsys) -> None:
    main()

    captured = capsys.readouterr()
    assert captured.out == "Kanji Flashcard App is ready.\n"

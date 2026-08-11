"""Command-line entry point for the kanji flashcard application."""

import argparse
from collections.abc import Callable, Sequence
from pathlib import Path

from kanji_flashcard.loaders import load_kanji


def study(path: Path, read_input: Callable[[], str] = input) -> None:
    """Study each Kanji in a JSON file."""
    kanji_list = load_kanji(path)

    if not kanji_list:
        print("There are no Kanji to study.")
        return

    known_count = 0
    unknown_count = 0

    for kanji in kanji_list:
        print(kanji.character)
        print("Press Enter to reveal the answer.")
        read_input()
        print(f"Meanings: {', '.join(kanji.meanings)}")
        print(f"Onyomi: {', '.join(kanji.onyomi)}")
        print(f"Kunyomi: {', '.join(kanji.kunyomi)}")

        answer = ""
        while answer not in {"y", "n"}:
            print("Did you know it? [y/n]:")
            answer = read_input()

        if answer == "y":
            known_count += 1
        else:
            unknown_count += 1

    print("Study complete.")
    print(f"Total Kanji studied: {len(kanji_list)}")
    print(f"Known: {known_count}")
    print(f"Unknown: {unknown_count}")


def main(
    argv: Sequence[str] | None = None,
    read_input: Callable[[], str] = input,
) -> None:
    """Run the command-line application."""
    parser = argparse.ArgumentParser(prog="kanji-flashcard")
    subparsers = parser.add_subparsers(dest="command")
    study_parser = subparsers.add_parser("study", help="study Kanji from a JSON file")
    study_parser.add_argument("path", type=Path)

    args = parser.parse_args(argv)

    if args.command == "study":
        study(args.path, read_input)
    else:
        print("Kanji Flashcard App is ready.")


if __name__ == "__main__":
    main()

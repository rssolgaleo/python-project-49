#!/usr/bin/env python3

from brain_games.progress_game import progress_game
from brain_games.even import is_even


def main():
    play()
    text: str = 'Answer "yes" if the number is even, otherwise answer "no".'
    progress_game(is_even, text)


if __name__ == "__main__":
    main()

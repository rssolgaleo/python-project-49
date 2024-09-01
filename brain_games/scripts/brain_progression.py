#!/usr/bin/env python3

from brain_games.progress_game import progress_game
from brain_games.progression import hide_number


def main():
    progress_game(hide_number, 'What number is missing in the progression?')


if __name__ == "__main__":
    main()

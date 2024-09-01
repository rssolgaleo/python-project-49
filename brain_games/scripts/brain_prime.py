#!/usr/bin/env python3

from brain_games.progress_game import progress_game
from brain_games.prime import is_prime


def main():
    text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    progress_game(is_prime, text)


if __name__ == "__main__":
    main()

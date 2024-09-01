#!/usr/bin/env python3

from brain_games.progress_game import progress_game
from brain_games.gcd import gcd


def main():
    progress_game(gcd, 'Find the greatest common divisor of given numbers.')


if __name__ == "__main__":
    main()

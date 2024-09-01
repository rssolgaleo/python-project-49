#!/usr/bin/env python3

from brain_games.progress_game import progress_game
from brain_games.calc import calculator


def main():
    progress_game(calculator, 'What is the result of the expression?')


if __name__ == '__main__':
    main()

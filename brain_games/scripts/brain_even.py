#!/usr/bin/env python3

import random
from brain_games.cli import welcome_user


def is_even(n):
    return n % 2 == 0


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    score = 0
    while (score < 3):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        a = input('Your answer: ')
        correct = 'yes' if is_even(number) else 'no'
        if a == correct:
            print("Correct!")
            score += 1
        else:
            print(f"'{a}' is wrong answer ;(. Correct answer was '{correct}'")
            print(f"Let's try again, {name}!")
            break
    if score == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

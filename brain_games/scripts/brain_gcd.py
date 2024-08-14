#!/usr/bin/env python3

import random
from brain_games.cli import welcome_user


def gcd(a, b):
    if a == 0 or b == 0:
        return(max(a, b))
    else:
        if a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    score = 0
    while (score < 3):
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        print(f'Question: {a} {b}')
        answer = input('Your answer: ')
        if answer == gcd(a, b):
            print("Correct!")
        else:
            print(f"'{answer} is wrong answer ;(. Correct answer was '{gcd(a, b)}'")
    if score == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
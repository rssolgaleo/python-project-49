#!/usr/bin/env python3

import random
from brain_games.cli import welcome_user


def gcd(a, b):
    while a != 0 and b != 0:
        if (a > b):
            a = a % b
        else:
            b = b % a
    return a + b


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    score = 0
    while (score < 3):
        a = random.randint(0, 50)
        b = random.randint(0, 50)
        print(f'Question: {a} {b}')
        right = gcd(a, b)
        answ = int(input('Your answer: '))
        if answ == right:
            score += 1
            print("Correct!")
        else:
            print(f"'{answ}' is wrong answer ;(. Correct answer was '{right}'")
            print(f"Let's try again, {name}!")
            break
    if score == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

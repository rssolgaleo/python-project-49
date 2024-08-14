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
        correct = gcd(a, b)
        answer = int(input('Your answer: '))
        print(answer)
        if answer == correct:
            score += 1
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'")
            break
    if score == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
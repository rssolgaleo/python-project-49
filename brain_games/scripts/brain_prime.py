#!/usr/bin/env python3

import random
from brain_games.cli import welcome_user


def is_prime(n):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    score = 0
    while (score < 3):
        number = random.randint(1, 50)
        print(f"Question: {number}")
        a = str(input('Your answer: '))
        correct = 'yes' if is_prime(number) else 'no'
        if a == correct:
            print("Correct!")
            score += 1
        else:
            print(f"'{a}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            break
    if score == 3:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

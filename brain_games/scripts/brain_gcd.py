#!/usr/bin/env python3

import random
from brain_games.cli import hi, user_answer, check, number_count, end


def gcd(a, b):
    while a != 0 and b != 0:
        if (a > b):
            a = a % b
        else:
            b = b % a
    return a + b


def main():
    name = hi()
    count = number_count()
    correct_count = 0
    print('Find the greatest common divisor of given numbers.')
    for _ in range(count):
        a = random.randint(0, 50)
        b = random.randint(0, 50)
        print(f"Question: {a} {b}")
        answer = int(user_answer())
        correct = gcd(a, b)
        if check(name, answer, correct):
            correct_count += 1
            if end(name, correct_count):
                break
        else:
            break


if __name__ == "__main__":
    main()

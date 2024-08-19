#!/usr/bin/env python3

import random
from brain_games.cli import hi, user_answer, check, number_count, end


def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def main():
    name = hi()
    count = number_count()
    correct_count = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(count):
        number = random.randint(2, 50)
        print(f"Question: {number}")

        answer = str(user_answer())
        correct = 'yes' if is_prime(number) else 'no'
        if check(name, answer, correct):
            correct_count += 1
            if end(name, correct_count):
                break
        else:
            break


if __name__ == "__main__":
    main()

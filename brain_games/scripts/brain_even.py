#!/usr/bin/env python3

import random
from brain_games.cli import hi, user_answer, check, number_count, end


def is_even(n):
    if n % 2 == 0:
        return True
    return False


def main():
    name = hi()
    count = number_count()
    correct_count = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(count):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = user_answer()
        correct = 'yes' if is_even(number) else 'no'
        if check(name, answer, correct):
            correct_count += 1
            if end(name, correct_count):
                break
        else:
            break


if __name__ == "__main__":
    main()

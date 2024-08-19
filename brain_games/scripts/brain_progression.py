#!/usr/bin/env python3

import random
from brain_games.cli import hi, user_answer, check, number_count, end


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 7)
    progression = [start + i * step for i in range(10)]
    return progression


def hide_number(progression):
    index = random.randint(0, len(progression) - 1)
    hidden_number = progression[index]
    progression[index] = '..'
    return progression, hidden_number


def main():
    name = hi()
    count = number_count()
    correct_count = 0
    print('What number is missing in the progression?')
    for _ in range(count):
        progression = generate_progression()
        progression, hidden = hide_number(progression)
        print("Question:", *progression)
        answer = int(user_answer())
        if check(name, answer, hidden):
            correct_count += 1
            if end(name, correct_count):
                break
        else:
            break


if __name__ == "__main__":
    main()

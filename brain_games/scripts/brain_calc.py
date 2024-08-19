#!/usr/bin/env python3

from brain_games.cli import hi, user_answer, check, number_count, end, bye
import random


def calc(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b


def main():
    name = hi()
    count = number_count()
    correct_count = 0
    operations = ['+', '-', '*']
    print('What is the result of the expression?')
    for _ in range(count):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        operation = random.choice(operations)
        correct = calc(a, b, operation)
        print(f'Question: {a} {operation} {b}')
        answer = int(user_answer())
        if check(name, answer, correct):
            correct_count += 1
            if end(name, correct_count):
                break
        else:
            bye(name, answer, correct)
            break


if __name__ == '__main__':
    main()

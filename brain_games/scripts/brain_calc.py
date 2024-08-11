#!/usr/bin/env python3

from brain_games.cli import welcome_user
import random


def main():
    name = welcome_user()
    operations = ['+', '-', '*']
    print('What is the result of the expression?')
    for operation in operations:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        if operation == '+':
            correct_answer = a + b
        elif operation == '-':
            correct_answer = a - b
        elif operation == '*':
            correct_answer = a * b
        print(f'Question: {a} {operation} {b}')
        answer = int(input('Your answer: '))
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()

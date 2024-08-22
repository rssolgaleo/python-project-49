import random
from brain_games.cli import hi, number_count, check, win, lose, input

def calculator(a, b):
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    if operation == '+':
        print(f'Question: {a} + {b}')
        return a + b
    if operation == '-':
        print(f'Question: {a} - {b}')
        return a - b
    if operation == '*':
        print(f'Question: {a} * {b}')
        return a * b


def function():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    return a, b


def progress_game():
    name = hi()
    cycle = number_count()
    count = 0

    print('What is the result of the expression?')

    for _ in range(cycle):
        a, b = function()
        answer = calculator(a, b)
        user_answer = int(input())
        if check(user_answer, answer):
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)

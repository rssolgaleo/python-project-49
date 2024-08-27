import random
from brain_games.cli import hi, number_count, check, win, lose, reply


def calculator():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    if operation == '+':
        print(f'Question: {a} + {b}')
        return str(a + b)
    if operation == '-':
        print(f'Question: {a} - {b}')
        return str(a - b)
    if operation == '*':
        print(f'Question: {a} * {b}')
        return str(a * b)


def progress_game():
    name = hi()
    cycle = number_count()
    count = 0

    print('What is the result of the expression?')

    for _ in range(cycle):
        answer = calculator()
        user_answer = reply()
        if check(user_answer, answer):
            count += 1
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)
            return

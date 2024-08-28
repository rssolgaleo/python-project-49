import random


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

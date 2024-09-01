import random


def calculator() -> str:
    a: int = random.randint(1, 100)
    b: int = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation: str = random.choice(operations)
    if operation == '+':
        print(f'Question: {a} + {b}')
        return str(a + b)
    if operation == '-':
        print(f'Question: {a} - {b}')
        return str(a - b)
    if operation == '*':
        print(f'Question: {a} * {b}')
        return str(a * b)

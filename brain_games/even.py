import random


def is_even() -> str:
    a: int = random.randint(1, 100)
    print(f'Question: {a}')
    return 'yes' if a % 2 == 0 else 'no'

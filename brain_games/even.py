import random


def is_even():
    a = random.randint(1, 100)
    print(f'Question: {a}')
    return 'yes' if a % 2 == 0 else 'no'

import random


def text():
    text: str = 'Find the greatest common divisor of given numbers.'
    return text


def gcd() -> str:
    a: int = random.randint(1, 100)
    b: int = random.randint(1, 100)
    print(f'Question: {a} {b}')
    while a != 0 and b != 0:
        if (a > b):
            a = a % b
        else:
            b = b % a
    return str(a + b)

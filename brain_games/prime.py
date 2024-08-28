import random


def is_prime():
    a = random.randint(1, 100)
    print(f"Question: {a}")
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            return 'no'
    return 'yes'

import prompt


def hi():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def reply() -> str:
    answer = input("Your answer: ")
    return answer


def correct():
    print('Correct!')
    return


def win(name):
    print(f'Congratulations, {name}!')
    return


def lose(name, answ, right):
    print(f"'{answ}' is wrong answer ;(. Correct answer was '{right}'.")
    print(f"Let's try again, {name}!")
    return

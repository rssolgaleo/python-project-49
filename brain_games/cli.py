import prompt


def hi():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def number_count():
    return 3


def reply():
    answer = input("Your answer: ")
    return answer


def check(answer, right):
    if answer == right:
        print('Correct!')
        return True
    return False


def win(name):
    print(f'Congratulations, {name}!')
    return


def lose(name, answ, right):
    print(f"'{answ}' is wrong answer ;(. Correct answer was '{right}'.")
    print(f"Let's try again, {name}!")
    return

from brain_games.cli import hi, win, lose, reply, correct


def progress_game(func, text):
    name = hi()
    cycle = 3
    count = 0

    print(text)

    for _ in range(cycle):

        answer = func()

        user_answer = str(reply())

        if answer == user_answer:
            count += 1
            correct()
            if count == cycle:
                win(name)
                return
        else:
            lose(name, user_answer, answer)
            return

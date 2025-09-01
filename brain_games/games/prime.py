import random

from brain_games.scripts.utils import ask_answer


def get_answer_and_right_answer(expression: str) -> tuple:
    answer = ask_answer()
    right_answer = get_right_answer(expression)
    return (answer, right_answer)


def get_question_msg() -> str:
    number = random.randint(0, 100)
    return f"{number}"


def get_right_answer(expression: str) -> str:
    number = int(expression)
    if number <= 1:
        return 'no'
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def get_msg_game_rules() -> str:
    return "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."

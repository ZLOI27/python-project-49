import random

from brain_games.scripts.utils import ask_answer


def get_answer_and_right_answer(number: int) -> tuple:
    answer = ask_answer()
    right_answer = 'yes' if is_even(number) else 'no'
    return (answer, right_answer)


def get_question_msg() -> int:
    return random.randint(0, 100)


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False
    

def get_msg_game_rules() -> str:
    return "Answer \"yes\" if the number is even, otherwise answer \"no\"."

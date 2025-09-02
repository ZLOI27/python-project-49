import random


def get_question_msg() -> str:
    return str(random.randint(0, 100))


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False
    

def get_right_answer(expression: str) -> str:
    return 'yes' if is_even(int(expression)) else 'no'


def get_msg_game_rules() -> str:
    return "Answer \"yes\" if the number is even, otherwise answer \"no\"."

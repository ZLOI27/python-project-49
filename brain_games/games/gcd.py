import random

from brain_games.scripts.utils import ask_answer


def get_answer_and_right_answer(expression: str) -> tuple:
    answer = ask_answer()
    right_answer = get_right_answer(expression)
    return (answer, right_answer)


def get_question_msg() -> str:
    left_num = random.randint(0, 100)
    right_num = random.randint(0, 100)
    return f"{left_num} {right_num}"


def get_right_answer(expression: str) -> str:
    left_num, right_num = expression.split()
    left_num = int(left_num)
    right_num = int(right_num)
    while right_num != 0:
        mod = left_num % right_num
        left_num = right_num
        right_num = mod
    return str(left_num)


def get_msg_game_rules() -> str:
    return "Find the greatest common divisor of given numbers."

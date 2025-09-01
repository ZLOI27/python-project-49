import random

from brain_games.scripts.utils import ask_answer


def get_answer_and_right_answer(expression: str) -> tuple:
    answer = ask_answer()
    right_answer = get_right_answer(expression)
    return (answer, right_answer)


def get_question_msg() -> str:
    left_num = random.randint(0, 100)
    right_num = random.randint(0, 100)
    binary_op = random.choice('+-*')
    return f"{left_num} {binary_op} {right_num}"


def get_right_answer(expression: str) -> str:
    left_num, bin_op, right_num = expression.split()
    match bin_op:
        case '+':
            return str(int(left_num) + int(right_num))
        case '-':
            return str(int(left_num) - int(right_num))
        case '*':
            return str(int(left_num) * int(right_num))


def get_msg_game_rules() -> str:
    return "What is the result of the expression?"

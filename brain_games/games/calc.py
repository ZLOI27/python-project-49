import random


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

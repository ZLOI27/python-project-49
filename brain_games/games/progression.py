import random

hidden_number: str


def get_question_msg() -> str:
    length = random.randint(5, 10)
    position = random.randint(0, length - 1)
    start_num = random.randint(0, 10)
    step = random.randint(1, 10)
    stop_num = start_num + step * length
    progression_lst = [str(num) for num in range(start_num, stop_num, step)]
    global hidden_number
    hidden_number = progression_lst[position]
    progression_lst[position] = '..'
    return ' '.join(progression_lst)


def get_right_answer(expression: str) -> str:
    return hidden_number


def get_msg_game_rules() -> str:
    return "What number is missing in the progression?"

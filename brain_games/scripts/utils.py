import prompt


def greet_and_ask_name() -> str:
    print("Welcome to the Brain Games!") 
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}! ")
    return name


def ask_answer() -> str:
    return prompt.string("Your answer: ")


def get_answer_and_right_answer(
    get_right_answer: callable, 
    expression: str
) -> tuple:
    answer = ask_answer()
    right_answer = get_right_answer(expression)
    return (answer, right_answer)

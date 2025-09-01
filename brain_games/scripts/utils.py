import prompt


def greet_and_ask_name() -> str:
    print("Welcome to the Brain Games!") 
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}! ")
    return name


def ask_answer() -> str:
    return prompt.string("Your answer: ")

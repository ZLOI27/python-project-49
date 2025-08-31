import prompt

GREETING: str = "Welcome to the Brain Games!"
QUESTION: str = "May I have your name? "


def greet_and_ask_name(msg_greeting=GREETING, msg_question=QUESTION) -> str:
    print(msg_greeting) 
    name = prompt.string(msg_question)
    print(f"Hello, {name}! ")
    return name


def ask_answer() -> str:
    return prompt.string("Your answer: ")

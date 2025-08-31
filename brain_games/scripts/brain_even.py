import random

import prompt

from brain_games.game_logic import is_even
from brain_games.utils import greet_and_ask_name


def main():
    name = greet_and_ask_name()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    for i in range(3):
        number = random.randint(0, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        right_answer = 'yes' if is_even(number) else 'no'
        if answer == right_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.\n"
                  f"Let\'s try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()

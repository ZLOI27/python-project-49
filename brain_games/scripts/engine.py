from brain_games.scripts.utils import (
    get_answer_and_right_answer,
    greet_and_ask_name,
)


def engine_run(game) -> None:
    name = greet_and_ask_name()
    print(game.get_msg_game_rules())
    for i in range(3):
        question_msg = game.get_question_msg()
        print(f"Question: {question_msg}")
        answer, right_answer = get_answer_and_right_answer(
            game.get_right_answer, 
            question_msg
        )
        if answer == right_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.\n"
                  f"Let\'s try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")

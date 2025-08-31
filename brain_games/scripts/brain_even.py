import prompt
import random


def main():
    print('Welcome to the Brain Games!')    
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}! "
          f"Answer \'yes\' if the number is even, otherwise answer \'no\'.")
    for i in range(3):
        number = random.randint(0, 100)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        right_answer = 'yes' if is_even(number) else 'no'
        if answer == right_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\n"
                  f"Let\'s try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    main()

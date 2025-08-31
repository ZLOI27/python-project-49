import prompt

from brain_games import cli


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(cli.welcome_user(name))


if __name__ == '__main__':
    main()

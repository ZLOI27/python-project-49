from brain_games.games import gcd
from brain_games.scripts import engine


def main() -> None:
    engine.engine_run(gcd)


if __name__ == '__main__':
    main()
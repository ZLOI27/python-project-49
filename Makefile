reinstall:
	uv build
	uv tool install --force dist/*.whl

install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games/scripts/brain_games.py
	uv run ruff check brain_games/scripts/brain_even.py
	uv run ruff check brain_games/scripts/brain_calc.py
	uv run ruff check brain_games/scripts/brain_gcd.py
	uv run ruff check brain_games/games/even.py
	uv run ruff check brain_games/games/calc.py
	uv run ruff check brain_games/games/gcd.py
	uv run ruff check brain_games/utils.py
	uv run ruff check brain_games/engine.py

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
	uv run ruff check brain_games/utils.py
	uv run ruff check brain_games/game_logic.py

reinstall:
	uv build
	uv tool install --force dist/*.whl
	uv sync

install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check brain_games

# Hello Django

## Setup

1. Install the following:

      - [uv](https://docs.astral.sh/uv/getting-started/installation/)
      - [Docker](https://www.docker.com/products/docker-desktop/)

2. Install dependencies

      ```bash
      uv sync
      ```

3. Copy .env

      ```bash
      cp .env.example .env
      ```

4. Execute Docker compose

      ```bash
      docker-compose up -d
      ```

5. Migrate to Database

      ```bash
      uv run manage.py migrate
      ```

## Development

- Run the server

```bash
uv run manage.py runserver
```

- Start a new app

```bash
uv run manage.py startapp foo_app
```

- Run static type checks with MyPy

```bash
uv run mypy .
```

- Run tests using Pytest

```bash
uv run pytest
```

- Check code style with Ruff

```bash
uv run ruff check
```

## Utilities

- Make migrations

```bash
un run manage.py makemigrations foo_app
```

- Check SQL command in migration file

```bash
uv run manage.py sqlmigrate polls 0001
```

- Check for any database problems

```bash
uv run manage.py check
```

- Run Python shell in Django

```bash
un run manage.py shell
```

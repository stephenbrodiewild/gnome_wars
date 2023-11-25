# gnome_wars

## Setup
First install [pipx](https://github.com/pypa/pipx#install-pipx)

For Ubuntu, this should work:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install poetry
poetry install
```

Assuming you're using VS-Code, enable format on save and configure it to use
the black formatter.

```bash
chmod +x pre-push
./pre-push
```

## Running
```bash
poetry run gnome-wars
```

## Tests
```bash
poetry run pytest
```

## Adding dependencies
Simply
```bash
poetry add [DEPENDENCY]
```

This will change the pyproject.toml and poetry.lock. Make sure you commit these!

## Logging
Looky [here](https://stackoverflow.com/questions/4673373/logging-within-pytest-tests) for configuring logging.
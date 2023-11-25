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

## Running
```bash
poetry run gnome-wars
```

## Tests
```bash
poetry run pytest
```
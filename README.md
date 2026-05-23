# Quote Keeper

A **tiny** Python command‑line tool that prints a random inspirational quote.

## Features
- 10 built‑in quotes
- One‑line command: `quote-keeper`
- CI pipeline that runs tests, linting and caches dependencies

## Installation
```bash
# Clone the repo
git clone https://github.com/your‑username/quote-keeper.git
cd quote-keeper

# Install dependencies (recommended inside a virtualenv)
python -m pip install -r requirements.txt
```

## Usage
```bash
python -m src.quote_keeper   # prints a random quote
```
Or, after adding the project’s `src` directory to your `PYTHONPATH` you can run the installed entry‑point:
```bash
python -m src.quote_keeper
```

## Development
The project ships with a GitHub Actions workflow that automatically runs on every push and pull request:
- **Tests** – executed with `pytest`
- **Lint** – executed with `flake8`
- **Dependency caching** – speeds up CI runs

Feel free to fork, add more quotes, or extend the CLI!

---
**License:** MIT (see `LICENSE`)

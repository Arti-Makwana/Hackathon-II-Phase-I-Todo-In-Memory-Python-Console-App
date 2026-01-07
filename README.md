# Agentic Todo CLI - Phase I
A command-line Todo application built using a spec-driven, agentic workflow.

## Features
- **Add Tasks**: Create tasks with titles and descriptions.
- **Persistent Storage**: All tasks are saved to `tasks.json`.
- **Modular Design**: Separates UI logic (`app.py`) from data management (`manager.py`).

## Tech Stack
- Python 3.13+
- UV (Dependency Management)
- JSON (Persistence)

## How to Run
1. Ensure you have `uv` installed.
2. Run `uv sync` to set up the environment.
3. Launch the app: `python src/app.py`
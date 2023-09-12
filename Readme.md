## Installing Dependencies

1. Install `poetry`:

```sh
pip install poetry
```

## Creating a Virtual Environment

1. Configure `poetry` to create virtual environments within the project directory:

```sh
poetry config virtualenvs.in-project true
```

2. Installl Venv for poetry

```sh
poetry install
```

3. Run Streamlit App using this command:

```sh
poetry run streamlit run  nesda_dashboard.py  
```
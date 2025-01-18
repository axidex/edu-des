FROM python:3.10-slim

RUN pip install poetry

WORKDIR /app

RUN apt-get update && apt-get install -y curl && apt-get clean

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install

COPY . /app/

CMD ["poetry", "run", "python", "main.py"]

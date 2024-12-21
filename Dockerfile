# Используем lightweight образ с Python
FROM python:3.10-slim

# Устанавливаем Poetry
RUN pip install poetry

# Создаем рабочую директорию
WORKDIR /app

RUN apt-get update && apt-get install -y curl && apt-get clean

# Копируем файлы проекта
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Копируем остальной код
COPY . /app/

# Указываем команду запуска
CMD ["poetry", "run", "python", "main.py"]

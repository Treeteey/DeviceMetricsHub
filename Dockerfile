FROM python:3.12-slim

WORKDIR /app

# Установка Poetry
RUN pip install poetry

# Копирование всего проекта
COPY . .

# Настройка Poetry
RUN poetry config virtualenvs.create false

# Установка зависимостей
RUN poetry install --no-interaction --no-ansi

# Запуск приложения
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 
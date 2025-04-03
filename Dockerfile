FROM python:3.12-slim

WORKDIR /app

# Копирование исходного кода
COPY . .

# Установка Poetry
RUN pip install --no-cache-dir poetry

# Настройка Poetry
RUN poetry config virtualenvs.create false
# RUN poetry config virtualenvs.create false && \
    # poetry config repositories.pypi https://mirrors.aliyun.com/pypi/simple/ && \
    # poetry config installer.max-retries 5 && \
    # poetry config installer.timeout 600

# Установка зависимостей проекта
RUN poetry install --without dev

# Запуск приложения
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"] 
# Device Stats Service

Сервис для учета и анализа данных, поступающих с устройств.

## Описание

Сервис предоставляет REST API для:
- Сбора статистики с устройств
- Анализа собранной статистики
- Управления пользователями и их устройствами

## Требования

- Python 3.8+
- Docker
- Docker Compose

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd device-stats-service
```

2. Создайте файл `.env` на основе `.env.example` и настройте переменные окружения.

3. Запустите сервис с помощью Docker Compose:
```bash
docker-compose up -d
```

Сервис будет доступен по адресу: http://localhost:8000

## API Endpoints

### Устройства
- `POST /api/v1/devices/` - Создание нового устройства
- `GET /api/v1/devices/{device_id}` - Получение информации об устройстве
- `POST /api/v1/devices/{device_id}/stats/` - Отправка статистики устройства
- `GET /api/v1/devices/{device_id}/stats/` - Получение статистики устройства
- `GET /api/v1/devices/{device_id}/stats/analysis/{field}` - Анализ статистики устройства

### Пользователи
- `POST /api/v1/users/` - Создание нового пользователя
- `GET /api/v1/users/{user_id}/devices/` - Получение списка устройств пользователя

## Нагрузочное тестирование

Для запуска нагрузочного тестирования:

```bash
docker-compose run locust
```

Откройте веб-интерфейс Locust по адресу: http://localhost:8089

## Технологии

- FastAPI - веб-фреймворк
- PostgreSQL - база данных
- SQLAlchemy - ORM
- Celery - асинхронные задачи
- Redis - брокер сообщений
- Locust - нагрузочное тестирование
- Docker - контейнеризация 
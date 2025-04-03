# Device Metrics Hub

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
git clone https://github.com/Treeteey/DeviceMetricsHub.git
cd DeviceMetricsHub
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

## Примеры запросов

### Linux/Mac (curl)

#### Создание устройства
```bash
curl -X POST "http://localhost:8000/api/v1/devices/" \
     -H "Content-Type: application/json" \
     -d '{"device_id": "device1", "user_id": 1}'
```

#### Получение информации об устройстве
```bash
curl "http://localhost:8000/api/v1/devices/device1"
```

#### Добавление статистики устройства
```bash
curl -X POST "http://localhost:8000/api/v1/devices/device1/stats/" \
     -H "Content-Type: application/json" \
     -d '{"x": 1.5, "y": 2.3, "z": 0.8}'
```

#### Получение статистики устройства
```bash
curl "http://localhost:8000/api/v1/devices/device1/stats/"
```

#### Получение статистики за период
```bash
curl "http://localhost:8000/api/v1/devices/device1/stats/?start_time=2024-03-20T00:00:00&end_time=2024-03-21T00:00:00"
```

#### Анализ статистики по полю
```bash
curl "http://localhost:8000/api/v1/devices/device1/stats/analysis/x"
```

#### Создание пользователя
```bash
curl -X POST "http://localhost:8000/api/v1/users/" \
     -H "Content-Type: application/json" \
     -d '{"username": "user1", "email": "user1@example.com"}'
```

#### Получение устройств пользователя
```bash
curl "http://localhost:8000/api/v1/users/1/devices/"
```

### Windows (PowerShell)

#### Создание устройства
```powershell
$body = @{
    device_id = "device1"
    user_id = 1
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/devices/" -Method Post -Body $body -ContentType "application/json"
```

#### Получение информации об устройстве
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/devices/device1" -Method Get
```

#### Добавление статистики устройства
```powershell
$body = @{
    x = 1.5
    y = 2.3
    z = 0.8
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/devices/device1/stats/" -Method Post -Body $body -ContentType "application/json"
```

#### Получение статистики устройства
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/devices/device1/stats/" -Method Get
```

#### Получение статистики за период
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/devices/device1/stats/?start_time=2024-03-20T00:00:00&end_time=2024-03-21T00:00:00" -Method Get
```

#### Анализ статистики по полю
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/devices/device1/stats/analysis/x" -Method Get
```

#### Создание пользователя
```powershell
$body = @{
    username = "user1"
    email = "user1@example.com"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/users/" -Method Post -Body $body -ContentType "application/json"
```

#### Получение устройств пользователя
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/users/1/devices/" -Method Get
```

## Документация API

После запуска сервера, документация API доступна по следующим URL:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Разработка

### Структура проекта

```
DeviceMetricsHub/
├── app/
│   ├── api/
│   │   └── device.py
│   ├── db/
│   │   └── database.py
│   ├── models/
│   │   └── device.py
│   ├── schemas/
│   │   └── device.py
│   ├── services/
│   │   └── device_service.py
│   ├── static/
│   │   └── index.html
│   └── main.py
├── tests/
├── .env
├── requirements.txt
└── README.md
```

### Запуск тестов

```bash
pytest
```

## Лицензия

MIT 
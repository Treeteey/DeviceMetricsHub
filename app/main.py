from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.device import router as device_router
from app.db.database import Base, engine

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Device Stats Service",
    description="Сервис для учета и анализа данных с устройств",
    version="1.0.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение статических файлов
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Подключение роутеров
app.include_router(device_router, prefix="/api/v1", tags=["devices"])

@app.get("/")
async def read_root():
    return FileResponse("app/static/index.html") 
from locust import HttpUser, task, between
import random
from datetime import datetime, timedelta

class DeviceStatsUser(HttpUser):
    wait_time = between(1, 5)
    
    def on_start(self):
        # Создание тестового устройства при запуске
        device_id = f"test_device_{random.randint(1, 1000)}"
        self.device_id = device_id
        self.client.post("/api/v1/devices/", json={"device_id": device_id})
    
    @task(3)
    def post_device_stats(self):
        # Отправка статистики устройства
        stats = {
            "x": random.uniform(-100, 100),
            "y": random.uniform(-100, 100),
            "z": random.uniform(-100, 100)
        }
        self.client.post(f"/api/v1/devices/{self.device_id}/stats/", json=stats)
    
    @task(1)
    def get_device_stats(self):
        # Получение статистики устройства
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=1)
        self.client.get(
            f"/api/v1/devices/{self.device_id}/stats/",
            params={
                "start_time": start_time.isoformat(),
                "end_time": end_time.isoformat()
            }
        )
    
    @task(1)
    def analyze_device_stats(self):
        # Анализ статистики устройства
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=1)
        field = random.choice(["x", "y", "z"])
        self.client.get(
            f"/api/v1/devices/{self.device_id}/stats/analysis/{field}",
            params={
                "start_time": start_time.isoformat(),
                "end_time": end_time.isoformat()
            }
        ) 
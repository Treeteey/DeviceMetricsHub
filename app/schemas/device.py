from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class DeviceStatsBase(BaseModel):
    x: float
    y: float
    z: float

class DeviceStatsCreate(DeviceStatsBase):
    pass

class DeviceStats(DeviceStatsBase):
    id: int
    device_id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class DeviceBase(BaseModel):
    device_id: str
    user_id: Optional[int] = None

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int
    created_at: datetime
    stats: List[DeviceStats] = []

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    devices: List[Device] = []

    class Config:
        from_attributes = True

class StatsAnalysis(BaseModel):
    min_value: float
    max_value: float
    count: int
    sum_value: float
    median: float 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta
from app.db.database import get_db
from app.schemas.device import (
    DeviceCreate,
    Device,
    DeviceStatsCreate,
    DeviceStats,
    UserCreate,
    User,
    StatsAnalysis
)
from app.models.device import Device, DeviceStats as DeviceStatsModel, User
from app.services.device_service import (
    create_device,
    get_device,
    create_device_stats,
    get_device_stats,
    analyze_stats,
    create_user,
    get_user_devices,
    get_all_devices,
    get_all_users
)

router = APIRouter()

@router.post("/devices/", response_model=Device)
def create_device_endpoint(device: DeviceCreate, db: Session = Depends(get_db)):
    return create_device(db, device)

@router.get("/devices/", response_model=List[Device])
def read_all_devices(db: Session = Depends(get_db)):
    return get_all_devices(db)

@router.get("/devices/all", response_model=List[Device])
def read_all_devices_alt(db: Session = Depends(get_db)):
    return get_all_devices(db)

@router.get("/devices/{device_id}", response_model=Device)
def read_device(device_id: str, db: Session = Depends(get_db)):
    db_device = get_device(db, device_id)
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return db_device

@router.post("/devices/{device_id}/stats/", response_model=DeviceStats)
def create_device_stats_endpoint(
    device_id: str,
    stats: DeviceStatsCreate,
    db: Session = Depends(get_db)
):
    device = get_device(db, device_id)
    if not device:
        raise HTTPException(status_code=404, detail=f"Device with id {device_id} not found")
    return create_device_stats(db, device_id, stats)

@router.get("/devices/{device_id}/stats/", response_model=List[DeviceStats])
def read_device_stats(
    device_id: str,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    return get_device_stats(db, device_id, start_time, end_time)

@router.get("/devices/{device_id}/stats/analysis/{field}", response_model=StatsAnalysis)
def analyze_device_stats(
    device_id: str,
    field: str,
    start_time: Optional[datetime] = None,
    end_time: Optional[datetime] = None,
    db: Session = Depends(get_db)
):
    stats = get_device_stats(db, device_id, start_time, end_time)
    if not stats:
        raise HTTPException(status_code=404, detail="No stats found for the given period")
    return analyze_stats(stats, field)

@router.post("/users/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users/{user_id}/devices/", response_model=List[Device])
def read_user_devices(user_id: int, db: Session = Depends(get_db)):
    return get_user_devices(db, user_id)

@router.get("/users/", response_model=List[User])
def read_all_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/stats/all", response_model=List[DeviceStats])
def read_all_stats(db: Session = Depends(get_db)):
    stats = db.query(DeviceStatsModel).join(Device).order_by(DeviceStatsModel.timestamp.asc()).all()
    # Преобразуем device_id в строковый идентификатор устройства
    for stat in stats:
        stat.device_id = stat.device.device_id
    return stats 
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from datetime import datetime, timedelta
import statistics
from app.models.device import Device, DeviceStats, User
from app.schemas.device import DeviceCreate, DeviceStatsCreate, UserCreate, StatsAnalysis
from fastapi import HTTPException

def create_device(db: Session, device: DeviceCreate) -> Device:
    if device.user_id is not None:
        user = db.query(User).filter(User.id == device.user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail=f"User with id {device.user_id} not found")
    
    db_device = Device(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def get_device(db: Session, device_id: str) -> Optional[Device]:
    return db.query(Device).filter(Device.device_id == device_id).first()

def create_device_stats(db: Session, device_id: str, stats: DeviceStatsCreate) -> DeviceStats:
    device = get_device(db, device_id)
    if not device:
        device = create_device(db, DeviceCreate(device_id=device_id))
    
    db_stats = DeviceStats(**stats.dict(), device_id=device.id)
    db.add(db_stats)
    db.commit()
    db.refresh(db_stats)
    return db_stats

def get_device_stats(db: Session, device_id: str, start_time: Optional[datetime] = None, end_time: Optional[datetime] = None) -> List[DeviceStats]:
    query = db.query(DeviceStats).join(Device).filter(Device.device_id == device_id)
    
    if start_time:
        query = query.filter(DeviceStats.timestamp >= start_time)
    if end_time:
        query = query.filter(DeviceStats.timestamp <= end_time)
    
    return query.all()

def analyze_stats(stats: List[DeviceStats], field: str) -> StatsAnalysis:
    values = [getattr(stat, field) for stat in stats]
    return StatsAnalysis(
        min_value=min(values),
        max_value=max(values),
        count=len(values),
        sum_value=sum(values),
        median=statistics.median(values)
    )

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_devices(db: Session, user_id: int) -> List[Device]:
    return db.query(Device).filter(Device.user_id == user_id).all() 
from sqlalchemy.orm import Session
from fastapi import HTTPException
import datetime

from . import models, schema


def create_petrol(db: Session, petrol: schema.PetrolCreate):
    db_item = models.Petrol(**petrol.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_petrol(db: Session, petrol_id: str):
    return db.query(models.Petrol).filter(models.Petrol.id == petrol_id).first()

def get_petrols(db: Session, skip: int = 0, limit = 50):
    return db.query(models.Petrol).offset(skip).limit(limit).all()

def update_petrol(petrol_id: str, db: Session, updated_petrol: schema.PetrolCreate):
    petrol_to_update = db.query(models.Petrol).filter(models.Petrol.id == petrol_id).first()
    petrol_to_update.usd_price_per_litre = updated_petrol.usd_price_per_litre
    petrol_to_update.usd_price_per_gallon = updated_petrol.usd_price_per_gallon
    petrol_to_update.eur_price_per_litre = updated_petrol.eur_price_per_litre
    petrol_to_update.eur_price_per_gallon = updated_petrol.eur_price_per_gallon
    petrol_to_update.country = updated_petrol.country
    petrol_to_update.updated_at = datetime.datetime.utcnow()
    db.commit()
    return petrol_to_update

def delete_petrol(petrol_id: str, db: Session):
    petrol_item = db.query(models.Petrol).filter(models.Petrol.id == petrol_id).first()
    if petrol_item is None:
        raise HTTPException(status_code=404, detail="Petrol value not found")
    db.delete(petrol_item)
    db.commit()
    return {"delete": True, "Item": petrol_item}

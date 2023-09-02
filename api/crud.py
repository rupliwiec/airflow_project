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


def create_weather(db: Session, weather: schema.WeatherCreate):
    db_item = models.Weather(**weather.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_weather(db: Session, weather_id: str):
    return db.query(models.Weather).filter(models.Weather.id == weather_id).first()

def get_weathers(db: Session, skip: int = 0, limit = 50):
    return db.query(models.Weather).offset(skip).limit(limit).all()

def update_weather(weather_id: str, db: Session, updated_weather: schema.WeatherCreate):
    weather_to_update = db.query(models.Weather).filter(models.Weather.id == weather_id).first()
    weather_to_update.temperature = updated_weather.temperature
    weather_to_update.temperature_unit = updated_weather.temperature_unit
    weather_to_update.wind = updated_weather.wind
    weather_to_update.wind_unit = updated_weather.wind_unit
    weather_to_update.visibility = updated_weather.visibility
    weather_to_update.visibility_unit = updated_weather.visibility_unit
    weather_to_update.humidity = updated_weather.humidity
    weather_to_update.humidity_unit = updated_weather.humidity_unit
    weather_to_update.clouds = updated_weather.clouds
    weather_to_update.clouds_unit = updated_weather.clouds_unit
    weather_to_update.cloud_base = updated_weather.cloud_base
    weather_to_update.cloud_base_unit = updated_weather.cloud_base_unit
    weather_to_update.country = updated_weather.country
    weather_to_update.updated_at = datetime.datetime.utcnow()
    db.commit()
    return weather_to_update

def delete_weather(weather_id: str, db: Session):
    weather_item = db.query(models.Weather).filter(models.Weather.id == weather_id).first()
    if weather_item is None:
        raise HTTPException(status_code=404, detail="Weather value not found")
    db.delete(weather_item)
    db.commit()
    return {"delete": True, "Item": weather_item}


def create_exchange_rate(db: Session, exchange: schema.ExchangeRateCreate):
    db_item = models.Weather(**exchange.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_exchange_rate(db: Session, exchange_rate_id: str):
    return db.query(models.ExchangeRate).filter(models.ExchangeRate.id == exchange_rate_id).first()

def get_exchange_rates(db: Session, skip: int = 0, limit = 50):
    return db.query(models.ExchangeRate).offset(skip).limit(limit).all()

def update_exchange_rate(exchange_rate_id: str, db: Session, updated_exchange_rate: schema.ExchangeRateCreate):
    exchange_rate_to_update = db.query(models.ExchangeRate).filter(models.ExchangeRate.id == exchange_rate_id).first()
    exchange_rate_to_update.usd_rate = updated_exchange_rate.usd_rate
    exchange_rate_to_update.euro_rate = updated_exchange_rate.euro_rate
    exchange_rate_to_update.country = updated_exchange_rate.country
    exchange_rate_to_update.updated_at = datetime.datetime.utcnow()
    db.commit()
    return exchange_rate_to_update

def delete_exchange_rate(exchange_rate_id: str, db: Session):
    exchange_rate_item = db.query(models.ExchangeRate).filter(models.ExchangeRate.id == exchange_rate_id).first()
    if exchange_rate_item is None:
        raise HTTPException(status_code=404, detail="ExchangeRate value not found")
    db.delete(exchange_rate_item)
    db.commit()
    return {"delete": True, "Item": exchange_rate_item}

def create_population(db: Session, population: schema.PopulationCreate):
    db_item = models.Population(**population.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_population(db: Session, population_id: str):
    return db.query(models.Population).filter(models.Population.id == population_id).first()

def get_populations(db: Session, skip: int = 0, limit = 50):
    return db.query(models.Population).offset(skip).limit(limit).all()

def update_population(db: Session, population_id: str, updated_population: schema.PopulationCreate):
    population_to_update = db.query(models.Population).filter(models.Population.id == population_id).first()
    population_to_update.total_population = updated_population.total_population
    population_to_update.country = updated_population.country
    population_to_update.updated_at = datetime.datetime.utcnow()
    db.commit()
    return population_to_update

def delete_population(db: Session, population_id: str):
    population_item = db.query(models.Population).filter(models.Population.id == population_id).first()
    if population_item is None:
        raise HTTPException(status_code=404, detail="Population value not found")
    db.delete(population_item)
    db.commit()
    return {"delete": True, "Item": population_item}
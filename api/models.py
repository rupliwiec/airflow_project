from .database import Base

from sqlalchemy import INTEGER, Column, String, Float, DateTime
import datetime

class Petrol(Base):
    __tablename__ = "petrol"

    id= Column(INTEGER, primary_key=True)
    usd_price_per_litre= Column(Float)
    usd_price_per_gallon= Column(Float)
    eur_price_per_litre= Column(Float)
    eur_price_per_gallon= Column(Float)
    country= Column(String(3))
    created_at= Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at= Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    __table_args__ = {'schema': 'api_data'}

class Weather(Base):
    __tablename__ = "weather"

    id = Column(INTEGER, primary_key=True)
    temperature = Column(Float)
    temperature_unit = Column(String)
    wind = Column(Float)
    wind_unit = Column(String)
    visibility = Column(Float, nullable=True)
    visibility_unit = Column(String, nullable=True)
    humidity = Column(Float, nullable=True)
    humidity_unit = Column(String, nullable=True)
    clouds = Column(Float)
    clouds_unit = Column(String)
    cloud_base = Column(Float)
    cloud_base_unit = Column(String)
    country = Column(String(3))
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    __table_args__ = {'schema': 'api_data'}


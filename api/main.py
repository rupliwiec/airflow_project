from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schema
from .database import sessionLocal1, engine

description = """
This API helps to collect information on
countries such as petrol prices, weather
and population
"""

app = FastAPI(
    title="Countries Info API",
    description=description
)

models.Base.metadata.create_all(bind=engine)

async def get_db():
    db = sessionLocal1()
    try:
        yield db
    except Exception as e:
        print(e)
    finally:
        db.close()

@app.post("/add_petrol/", response_model=schema.Petrol, tags=["petrol"])
def add_petrol(petrol: schema.PetrolCreate, db: Session = Depends(get_db)):
    return crud.create_petrol(db=db, petrol=petrol)

@app.get("/petrols/", response_model=list[schema.Petrol], tags=["petrol"])
def read_petrols(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    petrols = crud.get_petrols(db, skip=skip, limit=limit)
    return petrols

@app.get("/petrol/{petrol_id}", response_model=schema.Petrol, tags=["petrol"])
def read_petrol(petrol_id: int, db: Session = Depends(get_db)):
    db_petrol = crud.get_petrol(db=db, petrol_id=petrol_id)
    if db_petrol is None:
        raise HTTPException(status_code=404, detail="Petrol values not found")
    return db_petrol

@app.put("/update_petrol/{petrol_id}",response_model=schema.Petrol, tags=["petrol"])
def put_petrol(petrol_id: int, updated_petrol: schema.PetrolCreate, db: Session = Depends(get_db)):
    return crud.update_petrol(petrol_id=petrol_id, db=db, updated_petrol=updated_petrol)

@app.delete("/delete_petrol/{petrol_id}", tags=["petrol"])
def delete_petrol(petrol_id: int, db: Session = Depends(get_db)):
    return crud.delete_petrol(petrol_id=petrol_id, db=db)


@app.post("/add_weather/", response_model=schema.Weather, tags=["weather"])
def add_weather(weather: schema.WeatherCreate, db: Session = Depends(get_db)):
    return crud.create_weather(db=db, weather=weather)

@app.get("/weathers/", response_model=list[schema.Weather], tags=["weather"])
def read_weathers(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    weathers = crud.get_weathers(db, skip=skip, limit=limit)
    return weathers

@app.get("/weather/{weather_id}", response_model=schema.Weather, tags=["weather"])
def read_weather(weather_id: int, db: Session = Depends(get_db)):
    db_weather = crud.get_weather(db=db, weather_id=weather_id)
    if db_weather is None:
        raise HTTPException(status_code=404, detail="Weather values not found")
    return db_weather

@app.put("/update_weather/{weather_id}",response_model=schema.Weather, tags=["weather"])
def put_weather(weather_id: int, updated_weather: schema.WeatherCreate, db: Session = Depends(get_db)):
    return crud.update_weather(weather_id=weather_id, db=db, updated_weather=updated_weather)

@app.delete("/delete_weather/{weather_id}", tags=["weather"])
def delete_weather(weather_id: int, db: Session = Depends(get_db)):
    return crud.delete_weather(weather_id=weather_id, db=db)

@app.post("/add_exchange_rates/", response_model=schema.ExchangeRate, tags=["exchange rate"])
def add_exchange_rates(exchanges: schema.ExchangeRateCreate, db: Session = Depends(get_db)):
    return crud.create_exchange_rate(db=db, exchange=exchanges)

@app.get("/exchange_rates/", response_model=list[schema.ExchangeRate], tags=["exchange rate"])
def read_exchange_rates(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    exchanges = crud.get_exchange_rates(db, skip=skip, limit=limit)
    return exchanges

@app.get("/exchange_rate/{exchange_rate_id}", response_model=schema.ExchangeRate, tags=["exchange rate"])
def read_exchange_rate(exchange_rate_id: int, db: Session = Depends(get_db)):
    db_exchange_rate = crud.get_exchange_rate(db=db, exchange_rate_id=exchange_rate_id)
    if db_exchange_rate is None:
        raise HTTPException(status_code=404, detail="Exchange rate values not found")
    return db_exchange_rate

@app.put("/update_exchange_rate/{exchange_rate_id}",response_model=schema.ExchangeRate, tags=["exchange rate"])
def put_exchange_rate(exchange_rate_id: int, updated_exchange_rate: schema.ExchangeRateCreate, db: Session = Depends(get_db)):
    return crud.update_exchange_rate(exchange_rate_id=exchange_rate_id, db=db, updated_exchange_rate=updated_exchange_rate)

@app.delete("/delete_exchange_rate/{exchange_rate_id}", tags=["exchange rate"])
def delete_exchange_rate(exchange_rate_id: int, db: Session = Depends(get_db)):
    return crud.delete_exchange_rate(exchange_rate_id=exchange_rate_id, db=db)


@app.post("/add_population/", response_model=schema.Population, tags=["population"])
def add_population(population: schema.PopulationCreate, db: Session = Depends(get_db)):
    return crud.create_population(db=db, population=population)

@app.get("/populations/", response_model=list[schema.Population], tags=["population"])
def read_populations(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    populations = crud.get_populations(db, skip=skip, limit=limit)
    return populations

@app.get("/population/{population_id}", response_model=schema.Population, tags=["population"])
def population(population_id: int, db: Session = Depends(get_db)):
    db_population = crud.get_population(db=db, population_id=population_id)
    if db_population is None:
        raise HTTPException(status_code=404, detail="Population values not found")
    return db_population

@app.put("/update_population/{population_id}",response_model=schema.Population, tags=["population"])
def population(population_id: int, updated_population: schema.PopulationCreate, db: Session = Depends(get_db)):
    return crud.update_population(population_id=population_id, db=db, updated_population=updated_population)

@app.delete("/delete_population/{population_id}", tags=["population"])
def delete_population(population_id: int, db: Session = Depends(get_db)):
    return crud.delete_population(population_id=population_id, db=db)
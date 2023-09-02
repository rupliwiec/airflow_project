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

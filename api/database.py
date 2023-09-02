from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"postgresql://fastapi_user:fastapi_user@localhost/web_data"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

sessionLocal1 = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


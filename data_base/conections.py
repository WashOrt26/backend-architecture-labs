from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# physical destine of data
DATABASE_URL = "sqlite:///./data_system.db"

# the engine that manage the direct comunication with the disk file

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Sessions to inject/extract data from the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class to create the models
Base = declarative_base()

# physic schema of the database
class UserTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String) # store the hashed password instead of the plain text

# dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
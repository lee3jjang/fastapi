# %% Import
from sql_app.database import SessionLocal
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# %% Create DataBase
engine = create_engine('sqlite:///test.db', connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# %% Create Model
from sqlalchemy import Boolean, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
# %% Create All
Base.metadata.create_all(engine)
db = SessionLocal()
# %% Create User
db_user = User(email='lee3jjang', password='123236')
db.add(db_user)
db.commit()
# %%

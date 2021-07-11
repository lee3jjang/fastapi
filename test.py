# %% Import
from sqlalchemy.sql.schema import ForeignKey
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

    items = relationship('Item', back_populates='owner')

class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('user.id'))

    owner = relationship('User', back_populates='items')
# %% Create All
Base.metadata.create_all(engine)
db = SessionLocal()

# %% Create User
db_user = User(email='lee3sang', password='123236')
db.add(db_user)
db.commit()
db.refresh(db_user)

# %% Create Item
db_item = Item(title='speaker', description='food market', owner_id=1)
db.add(db_item)
db.commit()
db.refresh(db_item)

# %% Get User
# db.rollback()
# user = db.query(User).first()
item = db.query(Item).first()
item.owner.email
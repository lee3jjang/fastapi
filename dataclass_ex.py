from dataclasses import dataclass, asdict, astuple
from typing import Optional
from pydantic import BaseModel
import logging
logging.basicConfig(format=None, level=logging.INFO)
logger = logging.getLogger()

@dataclass
class Item:
    name: str
    price: float
    is_offer: Optional[bool] = None

class User(BaseModel):
    id: int
    name: str = 'Jane Doe'
    age: Optional[str] = None


item = Item('sangjin', 100)
logger.info(item)
logger.info(asdict(item))
logger.info(astuple(item))

user = User(id='123')
logger.info(user)
logger.info(user.id == 123)

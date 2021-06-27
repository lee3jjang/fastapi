from typing import Optional

import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger('root')

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# from fastapi.templating import Jinja2Templates
# templates = Jinja2Templates(directory='templates')

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {"items_id": item_id, "q": q}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    logger.info(f"{item.name} {item.price} {item.is_offer} {item_id}")
    return {"item_name": item.name, "item_id": item_id}

from typing import Optional

import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger('root')

from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse
app = FastAPI()

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory='templates')

class Item(BaseModel):
    name: str = Field(..., example='Foo')
    description: Optional[str] = Field(None, example='A very nice Item')
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)

@app.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {'item_id': item_id, 'item': item}
    return results

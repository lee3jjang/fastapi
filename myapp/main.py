from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='myapp/templates')

@app.get('/')
async def read_root():
    return {"Hello": "World"}

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get('/name/{id}', response_class=HTMLResponse)
async def read_name(request: Request, id: str):
    return templates.TemplateResponse('item.html', {'request': request, 'id': id})
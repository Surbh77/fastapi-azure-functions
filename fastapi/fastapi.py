from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

app = FastAPI()

@app.get("/read_data/{item_id}")
async def read_data(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

@app.post("/create_data/")
async def create_data(item_id: int, data: Item):

    return {"item_id": item_id, "data": data}

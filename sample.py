from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app= FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
@app.post("/add/{one},{two}")
async def add(one: int,two: int):
    return {
        f"addition of {one} and {two}": one + two
    }
@app.post("/data")
async def data(item: Item):
    return item

@app.post("/data1")
async def date1(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax =  item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
@app.put("/update/{item_id}")
async def update_id(item_id: int,item: Item):
    return {"item_id": item_id, **item.dict()}
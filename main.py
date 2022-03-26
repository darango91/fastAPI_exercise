from typing import Optional
from fastapi import FastAPI

from models.items import Item, Shoe

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/shoes/{shoe_id}")
def read_show(shoe_id: int, q: Optional[str] = None):
    return {"shoe_id": shoe_id, "q": q}

@app.put("/shoes/{shoe_id}")
def update_item(shoe_id: int, shoe: Shoe):
    return {
        "shoe_name": shoe.name,
        "shoe_id": shoe_id,
        "shoe_size": shoe.size
    }

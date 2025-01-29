"""
Minimal FastAPI application taken directly from the tutorial.
https://fastapi.tiangolo.com/
"""
import asyncio
import os
import random

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/foobar")
async def foobar():
    delayed = random.randint(1, 3)
    pid = os.getpid()
    await asyncio.sleep(delayed)
    return {"message": f"delayed reply from {pid} after {delayed} seconds", "pid": pid}


@app.get("/foobar-sync")
def foobar_sync():
    delayed = random.randint(1, 3)
    pid = os.getpid()
    return {"message": f"delayed reply from {pid} after {delayed} seconds", "pid": pid}
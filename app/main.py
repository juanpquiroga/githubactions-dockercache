from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    print("read_root 1")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    print("read_item 1")
    return {"item_id": item_id, "q": q}
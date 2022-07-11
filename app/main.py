from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    print("read_root")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    print("read_item")
    return {"item_id": item_id, "q": q}
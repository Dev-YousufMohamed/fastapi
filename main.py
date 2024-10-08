from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    from pytubefix import YouTube
    url = "https://www.youtube.com/watch?v=9Ipl9BP6rH4"
    return {"Hello": url}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


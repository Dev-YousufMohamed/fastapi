from typing import Union
from fastapi import FastAPI
from pytubefix import YouTube

app = FastAPI()


@app.get("/")
def read_root():
    youtubeObject = YouTube("https:/t/www.youtube.com/watch?v=9Ipl9BP6rH4")    
    return {"Hello": youtubeObject.streams.get_highest_resolution().url}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

    

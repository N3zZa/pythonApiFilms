from fastapi import FastAPI
from utils.actions import *
from utils.find import *
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/find")
async def find_item(text: str):
    # Ваш код для поиска
    result = main(text)
    return {"result": result}

@app.post("/get_link")
async def find_item(text: str):
    # Ваш код для поиска
    result = get_link(text)
    return {"result": result}
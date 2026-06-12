from fastapi import FastAPI

app = FastAPI()

items = []

@app.get("/")
def root():
    return {"message": "Welcome to the API!"}

@app.post("/items")
def creat_item(item: str):
    items.append(item)
    return item

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str: #auto conversion from fastapi
    item = items[item_id]
    return item



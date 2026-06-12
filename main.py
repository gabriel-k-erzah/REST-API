from fastapi import FastAPI, HTTPException


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
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")





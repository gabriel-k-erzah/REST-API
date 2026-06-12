"""

NOTE a look at REST API's:
REST APIS are built upon the theory that they are a representational
state transfer, and is a standard software architecture style,
that is industry known. they are all about communication between the client server.

The main benefits are, they are simple, standardised and high performance as
they support caching.

An overview of a REST API could be
End point -> Resource
Request -> Response

We use the acronym CRUD - (Create, Read, Update and Delete).
So in this case it's - Get, Post, Put and Delete

We can expect responses as JSON's and base further functionaliy off this principle
whether it's an ice cream creator or a list tracker.
"""

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

@app.get("/items")
def list_items(limit: int = 10):
    return items[0:limit]

@app.get("/items/{item_id}")
def get_item(item_id: int) -> str: #auto conversion from fastapi
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")





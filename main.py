from http.client import HTTPException
from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from typing import List
from models import Coffee, CoffeeUpdateRequest
app = FastAPI()

db: List[Coffee] = [
    Coffee(
        id = uuid4(),
        name = "Cappucino",
        size = "Extra Large",
        milk = True,
        price = 4.50,
        sugar = True
    ),
    Coffee(
        id = uuid4(),
        name = "Tea",
        size = "Small",
        milk = True,
        price = 1.10,
        sugar = False
    ),
        Coffee(
        name = "Americano",
        size = "Large",
        milk = True,
        price = 1.50,
    ),
        Coffee(
        name = "Espresso",
        size = "Extra Small",
        price = 0.90
    )
]

@app.get("/")
async def root():
    return {"message": "Hello to Fraser House Vending Machine!"}

@app.get("/coffees")
async def show_coffees():
    return db
@app.post("/coffees")
async def create_coffee(coffee: Coffee):
    db.append(coffee)
    return {"id": coffee.id}
@app.delete("/coffees/{coffee_id}")
async def delete_coffee(coffee_id: UUID):
    for coffee in db:
        if coffee.id == coffee_id:
            db.remove(coffee)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Coffee with id: {coffee_id}does not exist"
    )
@app.put("/coffee/{coffee_id}")
async def update_coffee(coffee_update: CoffeeUpdateRequest, coffee_id: UUID):
    for coffee in db:
        if coffee.id == coffee_id:
            if coffee_update.name is not None:
                coffee.name = coffee_update.name
            if coffee_update.size is not None:
                coffee.size = coffee_update.size
            if coffee_update.price is not None:
                coffee.price = coffee_update.price
            if coffee_update.milk is not None:
                coffee.milk = coffee_update.milk
            if coffee_update.sugar is not None:
                coffee.sugar = coffee_update.sugar
    raise HTTPException(
        status_code=404,
        detail=f"Coffee with id: {coffee_id} does not exists"
    )
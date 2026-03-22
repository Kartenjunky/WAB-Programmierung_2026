from fastapi import *
from pydantic import BaseModel
import time

app = FastAPI()

class Order(BaseModel):
    product: str
    quantity: int

@app.get("/")
def root():
    return {"message": "Mock API läuft"}

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    if customer_id == 1:
        return {
            "valid": True,
            "id": 1,
            "name": "Thomas Paul",
            "email": "paul@gmail.com"
        }
    elif customer_id == 2:
        return {
            "valid": False,
            "id": 2,
            "name": "Leon Maier",
            "email": "maier@gmail.com",
            "reason": "Kunde gesperrt"
        }
    raise HTTPException(status_code=404, detail="Customer nicht vorhanden")

@app.post("/orders")
def create_order(order: Order):
    return {
        "orderId": 4825,
        "status": "created",
        "product": order.product,
        "quantity": order.quantity
    }

@app.get("/error")
def error_case():
    raise HTTPException(status_code=500, detail="Internal mock server error")

@app.get("/slow")
def slow_response():
    time.sleep(5)
    return {"status": "delayed response"}
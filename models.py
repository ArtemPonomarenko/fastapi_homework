from typing import Optional
from uuid import UUID, uuid4
from xmlrpc.client import Boolean
from pydantic import BaseModel


class Coffee(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str = "Americano"
    size: str = "Medium"
    price: float = 1.20
    milk: Boolean = False
    sugar: Boolean = False
class CoffeeUpdateRequest(BaseModel):
    name: Optional[str]
    size: Optional[str]
    price: Optional[float]
    milk: Optional[Boolean]
    sugar: Optional[Boolean]
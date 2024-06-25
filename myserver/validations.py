from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str | None = None
    category: str | None = None
    price: float

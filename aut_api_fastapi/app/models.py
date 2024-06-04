from pydantic import BaseModel


class Product(BaseModel):
    """
    Pydantic model
    """

    id: int
    name: str
    price: float

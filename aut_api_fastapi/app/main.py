from typing import List
from fastapi import FastAPI, HTTPException

from app.models import Product

# run:  fastapi dev app\main.py

app = FastAPI()
products = [Product(id=1, name="product_1", price=100.00)]


@app.get("/", response_model=dict)
def read_root():
    """
    read root
    """
    return {"message": "Products API!"}


@app.get("/products", response_model=List[Product])
def get_products():
    """
    get all products
    """
    return products


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    """
    get product by id
    """
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", response_model=Product)
def create_product(product: Product):
    """
    create product
    """
    max_product_id = max(prod.id for prod in products)
    product.id = max_product_id + 1
    products.append(product)
    return product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    """
    update product
    """
    for index, product in enumerate(products):
        if product.id == product_id:
            updated_product.id = product_id
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int):
    """
    delete product
    """
    for index, product in enumerate(products):
        if product.id == product_id:
            return products.pop(index)
    raise HTTPException(status_code=404, detail="Product not found")

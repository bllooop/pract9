from fastapi import FastAPI, HTTPException
from app.product import Product

products: list[Product] = [
    Product(0, 'Apple', '45', '0'),
    Product(1, 'Fish', '210', '1')
]
app = FastAPI()


@app.get("/v1/products")
async def get_products():
    return products

@app.get("/v1/products/{name}")
async def get_products_by_name(name: str):
    output = [item for item in products if item.name == name]
    if len(output) > 0:
        return output[0]
    raise HTTPException(status_code=404, detail="Product not found")
 

from fastapi import FastAPI, HTTPException
from app.shop import Shop

shops: list[Shop] = [
    Shop(0, 'LocalFood', 'Moscow', '1'),
    Shop(1, 'Fruits', 'Saint-Petersburg', '1')
]
app = FastAPI()


@app.get("/v1/shops")
async def get_shops():
    return shops

@app.get("/v1/shops/{id}")
async def get_shops_by_id(id: int):
    output = [item for item in shops if item.id == id]
    if len(output) > 0:
        return output[0]
    raise HTTPException(status_code=404, detail="Shop not found")
 
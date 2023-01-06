from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import crud, models, schemas
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/v1/shops")
def create(details: schemas.CreateShop, db: Session = Depends(get_db)):
    to_create = models.Shop(
        name = details.name,
        location = details.location,
        productnum = details.productnum
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id":to_create.id
    }

@app.get("/v1/shops")
async def read_shopss(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    shops = crud.get_shops(db, skip=skip, limit=limit)
    return shops


@app.get("/v1/shops/{id}")
async def read_shops_by_id(id: int, db: Session = Depends(get_db)):
    result = crud.get_shops_by_id(db, id = id)
    if result is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    return result
 
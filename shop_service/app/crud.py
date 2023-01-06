from sqlalchemy.orm import Session

from . import models, schemas


def get_shops(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Shop).offset(skip).limit(limit).all()

def get_shops_by_id(db: Session, id: int, ):
    return db.query(models.Shop).filter(models.Shop.id == id).first()


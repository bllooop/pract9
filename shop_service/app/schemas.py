from pydantic import BaseModel


class ShopBase(BaseModel):
    name: str
    location: str
    productnum: int

class CreateShop(ShopBase):
    pass

class Shop(ShopBase):
    id: int

    class Config:
        orm_mode = True


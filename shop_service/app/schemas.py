from pydantic import BaseModel


class Shop(BaseModel):
    id: int
    name: str
    location: str
    productnum: int

    class Config:
        orm_mode = True

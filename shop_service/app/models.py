from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column

from .database import Base


class Shop(Base):
    __tablename__ = "shop"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    productnum = Column(Integer)



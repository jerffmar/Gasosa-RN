from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base

Model = declarative_base()

class Nota(Model):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True)
    cidade = Column(String(50))
    produto = Column(String(50))
    preco = Column(Float)
    data = Column(DateTime)

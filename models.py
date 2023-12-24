from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    size = Column(Integer, default=1)
    price = Column(Integer)
    
    stores = relationship("ProductStore", secondary="products_stores", back_populates="product")


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    capacity = Column(Integer, default=200)
    
    products = relationship("ProductStore", secondary="products_stores", back_populates="store")


class ProductStore(Base):
    __tablename__ = "products_stores"
    
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, ForeignKey("stores.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    count = Column(Integer)
    
    store = relationship("Store", back_populates="products")
    product = relationship("Product", back_populates="stores")

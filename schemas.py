from pydantic import BaseModel


# ---------- User

class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

# ---------- Product

class ProductBase(BaseModel):
    name: str
    size: int
    price: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

# ---------- Store

class StoreBase(BaseModel):
    address: str
    capacity: int


class StoreCreate(StoreBase):
    pass


class Store(StoreBase):
    id: int
    products: list[Product]

# ---------- Store

class ProductStoreBase(BaseModel):
    store: Store
    product: Product
    count: int


class ProductStoreCreate(ProductStoreBase):
    pass


class ProductStore(ProductStoreBase):
    pass

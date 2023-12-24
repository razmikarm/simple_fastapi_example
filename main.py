from utils import *
from test_data import *

from schemas import *
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.requests import Request

app = FastAPI()

@app.get('/')
def home():
    return {'msg': 'Hello world!'}

# /special-page/about
# /special-page/contact
# /special-page/career
@app.get('/special-page/{page}')
def special_page(page: SpecialPage):
    return {"page": page}

# ---------------------------- Users --------------------

@app.get('/users')
def users(offset: int = 0, limit: int = 2):
    return users_data[offset:offset + limit]

@app.post('/users')
def create_user(new_user: User):
    if users_data:
        new_user.id = users_data[-1].id + 1
    else:
        new_user.id = 1 
    users_data.append(new_user)
    return new_user

@app.get('/users/me')
def user():
    return users_data[5]

@app.get('/users/{user_id}')
def get_user(user_id: int, field: str | None = None):
    
    for curr_user in users_data:
        if curr_user.id == user_id:
            user = curr_user
            break
    else:
        return JSONResponse({'msg': 'User not found'}, 404)
    if field is not None and hasattr(user, field):
        return {field: getattr(user, field)}
    return user

@app.put('/users/{user_id}')
def user_put(user_id: int, new_user: User):

    for curr_user in users_data:
        if curr_user.id == user_id:
            user = curr_user
            break
    else:
        return JSONResponse({'msg': 'User not found'}, 404)

    for field, value in new_user:
        setattr(user, field, value)
    user.id = user_id    
    return user

# -------------------- Products -------------------------

@app.get('/products')
def products():
    return products_data

@app.post('/products')
def create_product(new_product: ProductCreate):
    if products_data:
        new_product.id = products_data[-1].id + 1
    else:
        new_product.id = 1
    products_data.append(new_product)
    return new_product

@app.get('/products/{product_id}')
def get_product(product_id: int):
    for product in products_data:
        if product.id == product_id:
            return product
    return JSONResponse({'msg': 'Product not found'}, status_code=404)

@app.put('/products/{product_id}')
def product_put(product_id: int, new_product: Product):
    for product in products_data:
        if product.id == product_id:
            break
    else:
        return JSONResponse({'msg': 'Product not found'}, status_code=404)

    for field, value in new_product:
        setattr(product, field, value)
    product.id = product_id
    return product

# -------------------- Stores -------------------------

@app.get('/stores')
def stores():
    return stores_data

@app.post('/stores')
def create_store(new_store: Store):
    
    products = new_store.products
    if products:
        total_count = 0
        for product_id, count in products.items():
            if not is_valid_product_id(product_id):
                return JSONResponse(
                    {"msg": f"Product with id {product_id} was not found"},
                    status_code=401
                )
            product = get_product(product_id)
            total_count += product.size * count
            if total_count > new_store.capacity:
                return JSONResponse(
                    {"msg": "Store capacity is not enough"}
                )
    
    if stores_data:
        new_store.id = stores_data[-1].id + 1
    else:
        new_store.id = 1
    stores_data.append(new_store)
    return new_store

@app.get('/stores/{store_id}')
def get_store(store_id: int):
    for store in stores_data:
        if store.id == store_id:
            return store
    return JSONResponse({'msg': 'Store not found'}, status_code=404)

@app.put('/stores/{store_id}')
def store_put(store_id: int, new_store: Store):
    
    products = new_store.products
    if products:
        total_count = 0
        for product_id, count in products.items():
            if not is_valid_product_id(product_id):
                return JSONResponse(
                    {"msg": f"Product with id {product_id} was not found"},
                    status_code=401
                )
            product = get_product(product_id)
            total_count += product.size * count
            if total_count > new_store.capacity:
                return JSONResponse(
                    {"msg": "Store capacity is not enough"}
                )
                
    for store in stores_data:
        if store.id == store_id:
            break
    else:
        return JSONResponse({'msg': 'Store not found'}, status_code=404)

    for field, value in new_store:
        setattr(store, field, value)
    store.id = store_id
    return store

@app.get('/stores/{store_id}/capacity')
def get_store(store_id: int):
    for store in stores_data:
        if store.id == store_id:
            break
    else:
        return JSONResponse({'msg': 'Store not found'}, status_code=404)
    
    used_space = 0
    for product_id, count in store.products.items():
        product = get_product(product_id)
        used_space += product.size * count
    return JSONResponse({
            "id": store.id,
            "free_space": store.capacity - used_space,
            "used_space": used_space,
            "total": store.capacity
        })
    
    

@app.get('/save')
def save():
    pass

@app.get('/restore')
def restore():
    pass

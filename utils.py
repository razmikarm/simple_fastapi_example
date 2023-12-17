from test_data import products_data

def is_valid_product_id(product_id):
    for product in products_data:
        if product.id == product_id:
            return True
    return False

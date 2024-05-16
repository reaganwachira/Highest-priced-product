def find_highest_priced_product(products):
    highest_priced_product = products[0]
    for product in products:
        if product['price'] > highest_priced_product['price']:
            highest_priced_product = product
    return highest_priced_product

# Example Usage:
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Smartphone", "price": 800},
    {"name": "Tablet", "price": 500},
    {"name": "Headphones", "price": 120},
]
result = find_highest_priced_product(products)
print(result)

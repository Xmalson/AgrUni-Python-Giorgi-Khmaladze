from functools import reduce

products = [
    ("Keyboard", 49.99, 3),
    ("Mouse", 19.99, 0),
    ("Monitor", 159.99, 2),
    ("USB Cable", 4.99, 10),
    ("Headphones", 89.99, 1)
]


available_products = list(filter(lambda item: item[2] > 0, products))
totals_per_product = list(map(lambda item: (item[0], item[1] * item[2]), available_products))
total_store_value = reduce(lambda acc, item: acc +item[1], totals_per_product, 0)

print("Available products:", available_products)
print("Totals per product:", totals_per_product)
print("Total store value:", total_store_value)

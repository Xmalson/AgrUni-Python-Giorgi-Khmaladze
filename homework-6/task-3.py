import json

def analyze_sales():
    max_single_quantity = 0
    customers_max_single = set()

    total_value_per_customer = {}
    total_quantity_per_product = {}

    total_purchase_value = 0
    total_purchase_quantity = 0
    purchase_count = 0

    with open("data.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            user, product, amount, price = line.split(",")
            amount = float(amount)
            price = float(price)

            purchase_value = amount * price

            # a)
            if amount > max_single_quantity:
                max_single_quantity = amount
                customers_max_single = {user}
            elif amount == max_single_quantity:
                customers_max_single.add(user)

            # b)
            total_value_per_customer[user] = (
                total_value_per_customer.get(user, 0) + purchase_value
            )

            # e)
            total_quantity_per_product[product] = (
                total_quantity_per_product.get(product, 0) + amount
            )

            # c, d)
            total_purchase_value += purchase_value
            total_purchase_quantity += amount
            purchase_count += 1

    # b)
    max_total_value = max(total_value_per_customer.values())
    customers_max_value = [
        user for user, value in total_value_per_customer.items()
        if value == max_total_value
    ]

    # e)
    max_product_quantity = max(total_quantity_per_product.values())
    most_sold_products = [
        product for product, qty in total_quantity_per_product.items()
        if qty == max_product_quantity
    ]

    stats = {
        "max_single_purchase_quantity": {
            "quantity": max_single_quantity,
            "customers": list(customers_max_single)
        },
        "max_total_purchase_value": {
            "value": max_total_value,
            "customers": customers_max_value
        },
        "average_purchase_value": total_purchase_value / purchase_count,
        "average_purchase_quantity": total_purchase_quantity / purchase_count,
        "most_sold_products": {
            "quantity": max_product_quantity,
            "products": most_sold_products
        }
    }

    with open("stats.json", "w") as json_file:
        json.dump(stats, json_file, indent=4)


analyze_sales()

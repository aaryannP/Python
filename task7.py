sales_data = [
    {"product": "Apple", "quantity": 10, "price": 0.5},
    {"product": "Banana", "quantity": 5, "price": 0.3},
    {"product": "Orange", "quantity": 8, "price": 0.6},
    {"product": "Apple", "quantity": 7, "price": 0.5},
    {"product": "Banana", "quantity": 3, "price": 0.3},
    {"product": "Orange", "quantity": 6, "price": 0.6}
]

# print("Sales Data:", sales_data)

# Total Sales per Product
total_sales = {}
for sale in sales_data:
    product = sale["product"]
    revenue = sale["quantity"] * sale["price"]
    if product in total_sales:
        total_sales[product] += revenue
    else:
        total_sales[product] = revenue
print("\nTotal Sales per Product:")
for product, revenue in total_sales.items():
    print(f"{product}: ${revenue:.2f}")

# Total Quantity Sold per Product
total_quantity = {}
for sale in sales_data:
    product = sale["product"]
    quantity = sale["quantity"]
    if product in total_quantity:
        total_quantity[product] += quantity
    else:
        total_quantity[product] = quantity
print("\nTotal Quantity Sold per Product:")
for product, quantity in total_quantity.items():
    print(f"{product}: {quantity} units")

# Identify the most Popular Product
most_popular_product = max(total_quantity, key=total_quantity.get)
print(f"\nMost Popular Product: {most_popular_product} ({total_quantity[most_popular_product]} units sold)")

# Find the product that generated the most revenue
most_revenue_product = max(total_sales, key=total_sales.get)
print(f"Product that generated the most revenue: {most_revenue_product} (${total_sales[most_revenue_product]:.2f})")
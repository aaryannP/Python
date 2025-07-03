PRODUCTS = [
    {"product": "Mobile", "Unit_sold": 20, "Unit_price": 75000},
    {"product": "Laptop", "Unit_sold": 28, "Unit_price": 105050},
    {"product": "Laptop", "Unit_sold": 45, "Unit_price": 150000},
    {"product": "Mobile", "Unit_sold": 10, "Unit_price": 50000},
    {"product": "Tab", "Unit_sold": 10, "Unit_price": 50000},
    {"product": "Tab", "Unit_sold": 5, "Unit_price": 30000},
]

revenue = {}
for item in PRODUCTS:
    product = item["product"]
    unit_sold = item["Unit_sold"]
    unit_price = item["Unit_price"]
    total_revenue = unit_sold * unit_price
    
    if product in revenue:
        revenue[product]["total_unit_sold"] += unit_sold
        revenue[product]["total_revenue"] += total_revenue
    else:
        revenue[product] = {
            "total_unit_sold": unit_sold,
            "total_revenue": total_revenue
        }

print("Product Wise Revenue:")
print("----------------------")
for product, data in revenue.items():
    print(f"{product}: Total Units Sold: {data['total_unit_sold']}, Total Revenue: Rs. {data['total_revenue']}")

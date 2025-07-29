# Fruit_manager.py
import json
import logging
import os

# Logger setup
logging.basicConfig(
    filename="Acesment.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

fruit_file = "fruit_stock.json"

def load_fruits():
    if not os.path.exists(fruit_file):
        return {}
    with open(fruit_file, "r") as f:
        return json.load(f)

def save_fruits(data):
    with open(fruit_file, "w") as f:
        json.dump(data, f, indent=4)

def add_fruit():
    fruits = load_fruits()
    name = input("Enter fruit name: ").strip().capitalize()
    if name in fruits:
        print("Fruit already exists. Try updating it instead.")
        return
    try:
        price = float(input("Enter fruit price(Per KG): "))
        quantity = int(input("Enter fruit quantity(In KG): "))
        fruits[name] = {"price": price, "quantity": quantity}
        save_fruits(fruits)
        logging.info(f"Added fruit: {name}, Price: {price}, Qty: {quantity}")
        print("Fruit added successfully.")
    except ValueError:
        print("Invalid input! Price and quantity must be numbers.")

def view_fruit():
    fruits = load_fruits()
    if not fruits:
        print("No fruits in stock.")
        return
    print("\n--- All Fruit Stocks ---")
    for fruit, details in fruits.items():
        print(f"{fruit}: ₹{details['price']} per unit, Qty: {details['quantity']}KG")
    print("------------------------")

def update_fruit():
    fruits = load_fruits()
    name = input("Enter fruit name to update: ").strip().capitalize()
    if name not in fruits:
        print("Fruit not found.")
        return
    try:
        price = float(input("Enter new price(Per KG): "))
        quantity = int(input("Enter new quantity(In KG): "))
        fruits[name]["price"] = price
        fruits[name]["quantity"] = quantity
        save_fruits(fruits)
        logging.info(f"Updated fruit: {name}, New Price: {price}, Qty: {quantity}KG")
        print("Fruit updated successfully.")
    except ValueError:
        print("Invalid input! Price and quantity must be numbers.")

# Customer.py
import logging
import json
import os
from Fruit_manager import view_fruit

fruit_file = "fruit_stock.json"

# Setup customer logger
logging.basicConfig(
    filename="customer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_fruits():
    if not os.path.exists(fruit_file):
        return {}
    with open(fruit_file, "r") as f:
        return json.load(f)

def save_fruits(data):
    with open(fruit_file, "w") as f:
        json.dump(data, f, indent=4)

def view_fruit():  # To reuse here in case manager isn't available
    fruits = load_fruits()
    if not fruits:
        print("No fruits in stock.")
        return
    print(55*" "+"--- Available Fruits ---")
    for fruit, details in fruits.items():
        print(f"{fruit}: ₹{details['price']} per unit, Qty: {details['quantity']}KG")
    print("------------------------")

def purchase_fruit():
    fruits = load_fruits()
    if not fruits:
        print("Stock is empty.")
        return

    while True:
        view_fruit()
        fruit_name = input("Enter fruit name to buy (or 'exit' to cancel): ").strip().capitalize()
        if fruit_name.lower() == 'exit':
            break

        if fruit_name not in fruits:
            print("Stock not available.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {fruit_name} to buy: "))
            available_qty = fruits[fruit_name]["quantity"]

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            if quantity > available_qty:
                print(f"Not enough stock. Only {available_qty}KG available.")
            else:
                # Update stock
                fruits[fruit_name]["quantity"] -= quantity
                save_fruits(fruits)

                total_cost = quantity * fruits[fruit_name]["price"]
                logging.info(f"Purchased {quantity}KG x {fruit_name} for ₹{total_cost}")
                print(f"You bought {quantity}KG {fruit_name}(s) for ₹{total_cost}")
        except ValueError:
            print("Invalid quantity. Please enter a number.")

def customer_menu():
    while True:
        print(55*" "+"\n--- Customer Menu ---")
        print(55*" "+"1. View Available Fruits")
        print(55*" "+"2. Buy Fruits")
        print(55*" "+"3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_fruit()
            logging.info("Customer viewed fruits.")
        elif choice == "2":
            purchase_fruit()
        elif choice == "3":
            print("Exiting customer menu.")
            break
        else:
            print("Invalid choice. Try again.")
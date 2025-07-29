# main.py
from Fruit_manager import add_fruit, view_fruit, update_fruit
from Customer import customer_menu

def manager_menu():
    while True:
        print(55*" "+"--- Fruit Manager Menu ---")
        print(55*" "+"1. Add Fruit")
        print(55*" "+"2. View Fruit")
        print(55*" "+"3. Update Fruit")
        print(55*" "+"4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_fruit()
        elif choice == "2":
            view_fruit()
        elif choice == "3":
            update_fruit()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter again.")

def main_menu():
    while True:
        print(55*" "+"==== Fruit Store Console ====")
        print(55*" "+"1. Manager")
        print(55*" "+"2. Customer")
        print(55*" "+"3. Exit")
        choice = input("Enter your role: ")

        if choice == "1":
            manager_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            print("Exiting Application.")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main_menu()

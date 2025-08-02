from Banker import Banker
from Customer import Customer

def main_menu():
    while True:
        print("\n--- Welcome to Python Bank ---")
        print("1. Banker")
        print("2. Customer")
        print("3. Exit")
        choice = input("Choose role: ")

        if choice == "1":
            banker = Banker()
            print("1. Register\n2. Login")
            op = input("Choose: ")
            if op == "1":
                banker.register()
            elif op == "2":
                if banker.login():
                    print("Banker login successful.")
                    while True:
                        print("\n1. View Customers\n2. Update\n3. Delete\n4. Logout")
                        act = input("Choose: ")
                        if act == "1":
                            banker.view_customers()
                        elif act == "2":
                            banker.update_customer()
                        elif act == "3":
                            banker.delete_customer()
                        elif act == "4":
                            break
            else:
                print("Invalid option.")
        
        elif choice == "2":
            customer = Customer()
            print("1. Register\n2. Login")
            op = input("Choose: ")
            if op == "1":
                customer.register()
            elif op == "2":
                user = customer.login()
                if user:
                    print("Customer login successful.")
                    user_id = user[0]
                    while True:
                        print("\n1. Deposit\n2. Withdraw\n3. View Balance\n4. Logout")
                        act = input("Choose: ")
                        if act == "1":
                            customer.deposit(user_id)
                        elif act == "2":
                            customer.withdraw(user_id)
                        elif act == "3":
                            customer.view_balance(user_id)
                        elif act == "4":
                            break
            else:
                print("Invalid option.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()

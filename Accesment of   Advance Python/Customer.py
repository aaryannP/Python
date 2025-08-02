from DB_Connect import connect_db
from Modules import CustomerModel

class Customer:

    def register(self):
        conn = connect_db()
        cur = conn.cursor()
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        try:
            cur.execute("INSERT INTO customers (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
            conn.commit()
            print("Registration successful.")
        except:
            print("Email already exists.")
        conn.close()

    def login(self):
        conn = connect_db()
        cur = conn.cursor()
        email = input("Email: ")
        password = input("Password: ")
        cur.execute("SELECT * FROM customers WHERE email=%s AND password=%s", (email, password))
        user = cur.fetchone()
        conn.close()
        return user

    def deposit(self, user_id):
        conn = connect_db()
        cur = conn.cursor()
        amt = float(input("Enter amount to deposit: "))
        cur.execute("UPDATE customers SET balance = balance + %s WHERE id = %s", (amt, user_id))
        conn.commit()
        print("Amount deposited.")
        conn.close()

    def withdraw(self, user_id):
        conn = connect_db()
        cur = conn.cursor()
        amt = float(input("Enter amount to withdraw: "))
        cur.execute("SELECT balance FROM customers WHERE id = %s", (user_id,))
        balance = cur.fetchone()[0]
        if amt > balance:
            print("Insufficient funds.")
        else:
            cur.execute("UPDATE customers SET balance = balance - %s WHERE id = %s", (amt, user_id))
            conn.commit()
            print("Withdrawal successful.")
        conn.close()

    def view_balance(self, user_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT balance FROM customers WHERE id = %s", (user_id,))
        balance = cur.fetchone()[0]
        print(f"Your balance is ₹{balance}")
        conn.close()

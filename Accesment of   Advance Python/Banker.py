from DB_Connect import connect_db

class Banker:

    def register(self):
        conn = connect_db()
        cur = conn.cursor()
        username = input("Enter new banker username: ")
        password = input("Enter password: ")
        try:
            cur.execute("INSERT INTO bankers (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
            print("Banker registered successfully.")
        except:
            print("Banker already exists or error occurred.")
        conn.close()

    def login(self):
        conn = connect_db()
        cur = conn.cursor()
        username = input("Username: ")
        password = input("Password: ")
        cur.execute("SELECT * FROM bankers WHERE username=%s AND password=%s", (username, password))
        user = cur.fetchone()
        conn.close()
        return user

    def view_customers(self):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")
        for row in cur.fetchall():
            print(row)
        conn.close()

    def update_customer(self):
        conn = connect_db()
        cur = conn.cursor()
        cid = input("Enter customer ID to update: ")
        name = input("New name: ")
        email = input("New email: ")
        cur.execute("UPDATE customers SET name=%s, email=%s WHERE id=%s", (name, email, cid))
        conn.commit()
        print("Customer updated.")
        conn.close()

    def delete_customer(self):
        conn = connect_db()
        cur = conn.cursor()
        cid = input("Enter customer ID to delete: ")
        confirm = input("Are you sure? (Y/N): ").lower()
        if confirm == 'y':
            cur.execute("DELETE FROM customers WHERE id=%s", (cid,))
            conn.commit()
            print("Customer deleted.")
        else:
            print("Deletion cancelled.")
        conn.close()

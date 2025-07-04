products = {} # main 
status = True 
menu = """ 
        press 1 for product manager
        press 2 for customer 
"""

while status:
    sub_dict = {} # child
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1: # for product manager
        product_name = input("Enter product : ").lower()       
        qty = int(input("Enter qty : "))
        price = int(input("Enter price : "))
        

        if product_name in products.keys():
            sub_dict["qty"] = qty + products[product_name]["qty"]
            sub_dict["price"] = price
        else:
            sub_dict["qty"] = qty
            sub_dict["price"] = price


        products[product_name] = sub_dict

        for k in products.keys():
            print(f"{k} Qty. {products[k]['qty']}  Price. {products[k]['price']} Rs.")


    elif choice == 2:  # for customer 
        total = 0
        status1 = True
        while status1:
            print("MENU")
            for k in products.keys():
                print(f"{k} {products[k]['price']} Rs.")
            
            product_name = input("Enter product which you want to buy : ").lower()
            qty = int(input("Enter no. of qty you want : "))
            if product_name not in products.keys() or products[product_name]['qty'] <= 0:
                print("Product not available!")
                continue
            if qty > products[product_name]['qty']:
                print(f"Only {products[product_name]['qty']} available, please enter a valid quantity.")
                continue
            
            price = products[product_name]['price'] * qty
            print(f"    price will be ::: {qty} X {products[product_name]['price']}Rs. =  {price} Rs")
            total += price
            
            more = input("do you want to add more product ?  press y for yes : ")
            if more.lower() != 'y':
                break
        
        print("\nINVOICE :")
        print("------------------")
        for k in products.keys():
            print(f"{k} Qty. {qty} X Rs. {products[k]['price']}  = Rs. {price}")
        print("----------------------------------")
        print(f"Total : Rs. {total}")

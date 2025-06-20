Name = input("Enter your name: ")
Gender = input("Enter your Gender 'M' or 'F': ")
Age = int(input("Enter your age: "))

Product = input("Enter product: ")
Gram = float(input("Enter product gram: "))
Gold_Price = 9837 # current gold price (1 grm)

Total_Gold_Rate = Gram * Gold_Price

Making_Charges_Per_Gram = 845

Total_Making_Charges = Gram * Making_Charges_Per_Gram
Total_Amount = Total_Gold_Rate + Total_Making_Charges
if Gender == "M" or "F":
    if Gender == "M": 
        if Age>0:  
            if Age > 65:
                if Total_Amount > 200000 and Total_Amount <= 300000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 20%")
                    print("Discount amount = ", Total_Amount * 0.20)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.20)) #wih discount
                elif Total_Amount > 300000 and Total_Amount <= 500000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 30%")
                    print("Discount amount = ", Total_Amount * 0.30)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.30)) #wih discount
                elif Total_Amount > 500000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 35%")
                    print("Discount amount = ", Total_Amount * 0.35)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.35)) #wih discount
                else:
                    print("You are not eligible for discount")
            elif Age <= 65 and Age >=0 :
                if Total_Amount > 200000 and Total_Amount <= 300000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 10%")
                    print("Discount amount = ", Total_Amount * 0.10)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.10)) #wih discount
                elif Total_Amount > 300000 and Total_Amount <= 500000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 20%")
                    print("Discount amount = ", Total_Amount * 0.20)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.20)) #wih discount
                elif Total_Amount > 500000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 25%")
                    print("Discount amount = ", Total_Amount * 0.25)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.25)) #wih discount
                else:
                    print("You are not eligible for discount")
            else:
                print("Please Enter Valid Age")
        else:
            print("Invalid age")
    else:
        if Age > 0:
            if Age > 65:
                if Total_Amount > 200000 and Total_Amount <= 300000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 25%")
                    print("Discount amount = ", Total_Amount * 0.25)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.25)) #wih discount
                elif Total_Amount > 300000 and Total_Amount <= 500000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 35%")
                    print("Discount amount = ", Total_Amount * 0.35)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.35)) #wih discount
                elif Total_Amount > 500000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 40%")
                    print("Discount amount = ", Total_Amount * 0.40)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.40)) #wih discount
                else:
                    print("You are not eligible for discount")
            elif Age <= 65 and Age >=0:
                if Total_Amount > 200000 and Total_Amount <= 300000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 15%")
                    print("Discount amount = ", Total_Amount * 0.15)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.15)) #wih discount
                elif Total_Amount > 300000 and Total_Amount <= 500000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 25%")
                    print("Discount amount = ", Total_Amount * 0.25)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.25)) #wih discount
                elif Total_Amount > 500000:
                    print("Total Amount = ", Total_Amount)
                    print("Discount = 30%")
                    print("Discount amount = ", Total_Amount * 0.30)
                    print("Total net amount = ",Total_Amount-(Total_Amount * 0.30)) #wih discount
                else:
                    print("You are not eligible for discount")
            else:
                print("Please Enter Valid Age.")  
        else:
            print("Invalid age")
else:
    print("Please Enter Valid Gender.")

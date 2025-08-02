try:
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a number : "))

    ans = num1/num2

except ZeroDivisionError:
    print("Cannot be enter zero")

else:
    print(ans)

finally:
    print("THANK YOU FOR USING THIS APPLICATION !!!")
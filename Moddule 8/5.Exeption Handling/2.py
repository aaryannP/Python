try:
    num1 = int(input("Enter a number = "))
    num2 = int(input("Enter a number = "))

    ans = num1/num2

    print(ans)
except ZeroDivisionError:
    print("Cannot Devide by Zero")
except ValueError:
    print("Enter numeric value only")
except:
    print("try after sometime!!!")
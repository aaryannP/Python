# Write a Python program to create a parameterized function that takes two arguments and prints their sum.

def addition(n1,n2):
    return n1 + n2

num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))

result = addition(num1,num2)
print("The sum of two numbers  : ",result)
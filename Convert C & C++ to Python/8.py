# Write a Python program to display the multiplication table of a given number using a for loop.


num = int(input("Enter a number to display its multiplication table: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")
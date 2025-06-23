# Write a Python program that accepts two integers from the user and performs
# arithmetic, relational, and logical operations on them. Display the results.

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))

# Arithmetic operations

print("Arithmetic Operations:")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)

# Relational operations

print("\nRelational Operations:")
print("Is num1 equal to num2?", num1 == num2)
print("Is num1 not equal to num2?", num1 != num2)
print("Is num1 greater than num2?", num1 > num2)
print("Is num1 less than num2?", num1 < num2)
print("Is num1 greater than or equal to num2?", num1 >= num2)
print("Is num1 less than or equal to num2?", num1 <= num2)

# Logical operations

print("\nLogical Operations:")
print("Is num1 greater than 10 and num2 less than 20?", num1 > 10 and num2 < 20)
print("Is num1 less than 10 or num2 greater than 20?", num1 < 10 or num2 > 20)
print("Is not (num1 equal to num2)?", not (num1 == num2))


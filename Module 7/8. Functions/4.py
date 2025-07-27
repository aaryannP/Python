# Write a Python program to create a lambda function with two expression.

# Lambda function with two expressions: sum and product
func = lambda x, y: (x + y, x * y)

result = func(5, 3)
print("Sum:", result[0])
print("Product:", result[1])
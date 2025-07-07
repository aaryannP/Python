#  Practical Example 3: Write a Python program to find a specific string in the list using a simple
# for loop and if condition.


list = ["apple", "banana", "cherry", "date", "elderberry"]

for i in list:
    if i == "cherry":
        print(f"Found the string: {i}")
        break
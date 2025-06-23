# Write a Python program that uses the break statement to stop printing numbers when it reaches 5. Modify the program to skip printing the number 3 using the continue statement.

print("Using for loop with break and continue:")
for i in range(1, 11):
    if i == 5: 
        break
    if i == 3:
        continue 
    print(i, end=' ')
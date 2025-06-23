# Write a Python program that takes a student’s marks as input and calculates the grade based on if-else conditions.


marks = int(input("Enter the marks = "))

if marks > 0 and marks < 100:
    if marks>=90:
        print("A++")
    elif marks>=80:
        print("A")
    elif marks>=70:
        print("B")
    elif marks>=60:
        print("C")
    else:
        print("D")
else:
    print("Invalid marks. Please enter a value between 0 and 100.")
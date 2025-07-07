# Practical Example 7: Write a Python program to calculate grades based on percentage using
# if-else ladder.


marks = int(input("Enter the marks = "))

if marks>=0 and marks<100:
    if marks>=80:
        print("A")
    elif marks>=70 and marks<80:
        print("B")
    elif marks>=60 and marks<70:
        print("C")
    elif marks>=50 and marks<60:
        print("E")
    else:
        print("Fail")
else:
    print("Enter valid marks.")
# Practical Example 8: Write a Python program to check if a person is eligible to donate blood
# using a nested if.

blood_pressure = input("Enter your blood pressure (systolic/diastolic): ")

systolic, diastolic = map(int, blood_pressure.split('/'))
if systolic < 180 and diastolic < 100:
    age = int(input("Enter your age: "))
    weight = int(input("Enter your weight in kg: "))
    
    if age >= 18 and weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood due to age or weight restrictions.")
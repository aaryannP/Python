# Write a Python program to create a class and access its properties using an object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object of the Person class
person1 = Person("Aryan", 19)
person2 = Person("Karma", 19)

# Access properties using the object
print("Name:", person1.name)
print("Age:", person1.age)
print("Name:", person2.name)
print("Age:", person2.age)
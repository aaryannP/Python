# Write a Python program to show single inheritance.

class Parent:
    def display(self):
        print("This is the Parent class.")

class Child(Parent):
    def display1(self):
        print("This is the Child class.")

c = Child()
c.display()
c.display1()
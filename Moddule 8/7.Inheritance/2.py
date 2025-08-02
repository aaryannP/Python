# Write a Python program to show multilevel inheritance. 

class grand_parent:
    def display(self):
        print("Hii This is Grand parent class.")
class parent(grand_parent):
    def display1(self):
        print("Hii This is parent class.")
class child(parent):
    def display2(self):
        print("Hii This is child class.")

c = child()
c.display()
c.display1()
c.display2()
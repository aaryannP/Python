# Write a Python program to show mupltiple inheritance. 

class father:
    def display(self):
        print("Hii This is father class")

class brother(father):
    def displayb(self):
        print("Hii This is brother class.")

class sister(father):
    def displays(self):
        print("Hii This is sister class.")

b = brother()
print("This is from brother class.")
b.display()
b.displayb()
print()
s = sister()
print("This is from sister class.")
s.display()
s.displays()
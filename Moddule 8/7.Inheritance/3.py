# Write a Python program to show mupltiple inheritance. 

class father:
    def displayf(self):
        print("Hii This is father class")

class mother:
    def displaym(self):
        print("Hii This is mother class.")

class child(father,mother):
    def displayc(self):
        print("Hii This is child class.")

c = child()
c.displayf()
c.displaym()
c.displayc()
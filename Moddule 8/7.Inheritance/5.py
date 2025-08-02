# Write a Python program to show hybrid inheritance. 

class father:
    def displayf(self):
        print("Hii This is father class")

class mother:
    def displaym(self):
        print("Hii This is mother class.")

class child(father,mother):
    def displayc(self):
        print("Hii This is child class.")

class child_son(child):
    def displaycs(self):
        print("Hii This is child_son class.")

class child_dauter(child):
    def displaycd(self):
        print("Hii This is child_dauter class.")

cs = child_son()
print("This is from child_son class.")
cs.displayf()
cs.displaym()
cs.displayc()
cs.displaycs()
print()
cd = child_dauter()
print("This is from child_dauter class.")
cd.displayf()
cd.displaym()
cd.displayc()
cd.displaycd()
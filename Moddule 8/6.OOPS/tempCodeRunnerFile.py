# Write a Python program to demonstrate the use of local and global variables in a class

# x = "I am a global variable"

# class Demo:
#     def show_variables(self):
#         y = "I am a local variable"
#         print("Global variable:", x)
#         print("Local variable:", y)

# d = Demo()
# d.show_variables()

x = 10

class semo:
    def local_variables(self):
        y = x + 10
        x = x + y

d = semo()
print("value of x : ",x)
print("value of y : ",y)
#  5) Write a Python program to read a file and print the data on the console. 

f = open("First.txt","r")

for i in f :
    print(i)

f.close()
# Write a Python program to open a file in write mode, write some text, and then close it.

f = open("first.txt","w")

f.write("Hello  This is first line")
f.write("\nHello  This is second line")

f.close()
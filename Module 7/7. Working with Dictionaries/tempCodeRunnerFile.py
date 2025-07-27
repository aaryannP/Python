# Write a Python program to separate keys and values from a dictionary using keys() and values() methods.

dictionary = {
    "id" : 1,
    "name" : "Aryan Parmar",
    "Subject" : "Python",
    "Hobby" : "Coding",
    "Age" : 19,
    "Birth Year" : 2006
}

for k, v in dictionary.items():
    print(f"{k} : {v}")
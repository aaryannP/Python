#  Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue
# statement. List1 = ['apple', 'banana', 'mango']


lsit1 = ['apple', 'banana', 'mango']

for i in lsit1:
    if i == 'banana':
        continue
    print(i)

# l2 = [i for i in list1 if i != 'banana']
# print(l2)
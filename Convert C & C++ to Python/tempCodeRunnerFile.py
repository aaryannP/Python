# Write a program that prints a right-angled triangle using stars(*) with a nested loop.

# row = int(input("Enter the number of rows for the triangle: "))
# spc = row-1
# for i in range(1, row + 1):
#     for k in range(spc):
#         print(" ")
#     for j in range(1, i + 1):
#         print("* ", end="")
#     spc -= 1
#     print()


row = int(input("Enter the row count = "))
spc = row - 1

for i in range(1, row + 1):
    for k in range(1, spc + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print("* ", end="")
    spc -= 1
    print()


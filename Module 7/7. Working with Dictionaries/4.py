# 18) Write a Python program to count how many times each character appears in a string.
text = input("Enter a string: ")
char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

for char, count in char_count.items():
    print(f"'{char}': {count}")

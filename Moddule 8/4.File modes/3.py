# 6) Write a Python program to check the current position of the file cursor using tell().

f = open("First.txt", 'a')
f.write("\nThis is Fifth Line\nThsis  is Sixth line.")
f.close()

# Open the file in read mode to demonstrate tell()
file_object_cursor_read = open("First.txt", 'r')

# Initial position
current_pos = file_object_cursor_read.tell()
print(f"Initial cursor position: {current_pos}")
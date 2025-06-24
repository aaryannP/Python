import random

print("Level 1: Guess the number between 1 and 100")
comp = random.randint(1, 100)

while True:
    user = int(input("Enter a number: "))
    if user > comp:
        print("Guess lower number")
    elif user < comp:
        print("Guess higher number")
    else:
        print(" RIGHT GUESS !!! You passed Level 1!")
        break  

print(" Level 2: Guess the number between 1 and 50")
print("You have 7 attempts to guess the number.")
comp1 = random.randint(1, 50)
level2 = False

for i in range(1, 8):
    user = int(input("Enter a number: "))
    if user > comp1:
        print("Guess lower number")
    elif user < comp1:
        print("Guess higher number")
    else:
        print(" RIGHT GUESS !!! You passed Level 2!")
        level2 = True
        break

if level2:
    print("Level 3: Guess the number between 1 and 50")
    print("You have 3 attempts to guess the number.")
    comp2 = random.randint(1, 50)

    for j in range(1, 4):
        user = int(input("Enter a number: "))
        if user > comp2:
            print("Guess lower number")
        elif user < comp2:
            print("Guess higher number")
        else:
            print(" RIGHT GUESS !!!")
            print(" CONGRATULATIONS! You passed all the levels!")
            break
    else:
        print(" You failed Level 3. Game Over.")
else:
    print(" You failed Level 2. Game Over.")
import random

numbers = []
while len(numbers) < 12:
    num = random.randint(1, 100)
    if num not in numbers:
        numbers.append(num)

player1 = numbers[:6]
player2 = numbers[6:]

while len(player1) > 0 and len(player2) > 0:
    guess = random.choice(numbers)
    print("Guess:", guess)
    if guess in player1:
        player1.remove(guess)
        numbers.remove(guess)
        print("Hit Player 1!")
    elif guess in player2:
        player2.remove(guess)
        numbers.remove(guess)
        print("Hit Player 2!")
    


if len(player1) == 0:
    print("Player 1 wins!")
elif len(player2) == 0:
    print("Player 2 wins!")

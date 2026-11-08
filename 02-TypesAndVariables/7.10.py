import random

computer = random.randint(1, 6)
you = int(input("Guess the number from 1 to 6: "))
print(f"You won: {you == computer}")

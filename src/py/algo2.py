
import random


def randomNumber():
    return random.randint(1, 100)


def playGame(n):
    g = 0
    c = 0

    while g != n:
        g = int(input("Guess a number between 1 and 100: "))
        c += 1
        if g > n:
            print("Too high! Try again.")
        elif g < n:
            print("Too low! Try again.")
        else:
            print("You guessed the number in", c, "tries.")

# CIT381-001 Spring 2022
# Author: Hai Hoang
# Created: Jan 25 2022
# Programming project-Python refresher: Guessing a random int

import random

randomNumber = random.randint(0, 1000)
guessCount = 0
#while loop call for input until guess is right at break line
guess = int(input("Guess a number: "))
while True:

    guessCount = guessCount + 1
    if guess > randomNumber:
        print("Guess is too high, try again")
    elif guess < randomNumber:
        print("Guess is too low, try again")
    else:
        print("You guessed correctly!")
        break
    guess = int(input("Next guess: "))
#evaluation
print("You needed to use %d number of guesses."%guessCount)
#with a binary search, the maximum guesses you need is only around 10
if guessCount == 1:
    print("You guessed really lucky")
elif guessCount < 5:
    print("You guessed really good")
elif guessCount <= 10:
    print("You guessed OK")
else:
    print("You performed poorly")
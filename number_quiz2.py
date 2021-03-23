"""
This is a guess the number game.
"""
import random

print('Hello. What is your name?')
name = input()

print(f'Well, {name}, I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)

for guessTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # This contition is for the correct guess.

if guess == secretNumber:
    print(f'Good job, {name}! You guessed my number in {str(guessTaken)} guesses.')
else:
    print(f'Nope, the number I was thinking of is {str(secretNumber)}.')
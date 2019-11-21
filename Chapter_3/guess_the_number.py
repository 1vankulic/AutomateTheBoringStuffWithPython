# I am thinking of a number between 1 and 20.
# Take a guess.
# 10
# Your guess is too low.
# Take a guess.
# 15
# Your guess is too low.
# Take a guess.
# 17
# Your guess is too high.
# Take a guess.
# 16
# Good job! You guessed my number in 4 guesses!

import random

answer = random.randint(1, 20)
print("I am thinking of a number between 1 and 20")

number_of_tries = 1

while True:
    print("Take a guess.")
    guess = int(input())
    if guess == answer:
        print(f"Good job! You guessed my number in {number_of_tries} guesses!")
        break
    elif guess > answer:
        print("Your guess is too high")
        number_of_tries += 1 
        continue
    elif guess < answer:
        print("Your guess is too low")
        number_of_tries += 1 
        continue









import random

number = random.randint(1, 10)
attempts = 0
max_attempts = 5

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10")
print("You have", max_attempts, "attempts")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed it in", attempts, "attempts.")
        break

if attempts == max_attempts and guess != number:
    print("Game Over! The correct number was:", number)

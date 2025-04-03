import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user to guess the number
guess = int(input("Guess a number between 1 and 10: "))

# Check if the guess is correct
if guess == secret_number:
    print("Congratulations! You guessed it right! 🎉")
else:
    print(f"Oops! The correct number was {secret_number}. Better luck next time!")

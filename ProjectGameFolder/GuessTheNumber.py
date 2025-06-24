import random # Import the random module to generate random numbers

secret_number = random.randint(1, 10) # Generate random numbers between 1 and 10
guess = 0 # Initial guess value is set to 0

print("Guess a number from 1 to 10") # Display instructions to the player

# Repeat until the guess is correct
while guess != secret_number:
	guess = int(input("Enter your guess: ")) # Ask the player to input a number
	if guess < secret_number:
	   print("Too small!") # If the guess is smaller than the secret number
	elif guess > secret_number:
	     print("Too big!") # If the guess is bigger than the secret number
	else:
	    print("You guessed it!")

print("Congratulations! You guessed right.") # If the guess is the same as the secret number

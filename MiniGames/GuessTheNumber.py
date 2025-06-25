import random
import time
import os

# Select game mode
print("Choose mode:")
print("1. Normal (1 - 100)")
print("2. Hard (1 - 1000)")
mode = input("Enter 1 or 2: ")

# Determine the number range based on mode
if mode == "2":
    number_to_guess = random.randint(1, 1000)
    max_number = 1000
else:
    number_to_guess = random.randint(1, 100)
    max_number = 100

# Game setup
guess = None
score = 100
lives = 5
start_time = time.time()
time_limit = 60  # seconds

# Load high score from file if it exists
highscore_file = "highscore.txt"
if os.path.exists(highscore_file):
    with open(highscore_file, "r") as file:
        highscore = int(file.read())
else:
    highscore = 0

# Display game instructions
print(f"\n🎯 Guess the number between 1 and {max_number}")
print(f"❤️ You have {lives} lives")
print(f"⏳ You have {time_limit} seconds to guess")
print("🏁 You start with 100 points")

# Main game loop
while guess != number_to_guess and lives > 0:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > time_limit:
        print("\n⏰ Time's up! You lost!")
        break

    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue

    if guess < number_to_guess:
        print("📉 Too low!")
        score -= 10
        lives -= 1
    elif guess > number_to_guess:
        print("📈 Too high!")
        score -= 10
        lives -= 1
    else:
        print(f"\n🎉 Correct! The number was {number_to_guess}")
        print(f"⭐ Your final score: {score}")
        if score > highscore:
            print("🏆 New high score!")
            with open(highscore_file, "w") as file:
                file.write(str(score))
        break

# If lives ran out and the number was not guessed
if guess != number_to_guess and lives == 0:
    print(f"\n💀 Out of lives. The number was {number_to_guess}")


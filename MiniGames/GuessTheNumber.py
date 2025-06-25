import random
import time
import os

# Select game mode
print("Select mode:")
print("1. Normal (1 - 100)")
print("2. Difficult (1 - 1000)")
mode = input("Enter 1 or 2: ")

if mode == "2": 
number_to_guess = random.randint(1, 1000) 
max_number = 1000
else: 
number_to_guess = random.randint(1, 100) 
max_number = 100

guess = None
score = 100
lives = 5
start_time = time.time()
time_limit = 60

# Read the highest score from the file
highscore_file = "highscore.txt"
if os.path.exists(highscore_file): 
with open(highscore_file, "r") as file:
highscore = int(file.read())
else:
highscore = 0

print(f"\n🎯 Guess a number from 1 to {max_number}")
print(f"❤️ You have {lives} lives")
print(f"⏳ You have {time_limit} seconds")
print("Your score starts at 100 points")

while guess != number_to_guess and lives > 0:
current_time = time.time()
elapsed_time = current_time - start_time

if elapsed_time > time_limit:
print("\n⏰ Time's up! You lose!")
break

try:
guess = int(input("Enter your guess: "))
except ValueError:
print("⚠️ Enter a number!")
continue

if guess < number_to_guess:
print("📉 Too small!")
score -= 10
lives -= 1
elif guess > number_to_guess:
print("📈 Too big!")
score -= 10
lives -= 1
else:
print(f"\n🎉 Congratulations! The number is {number_to_guess}")
print(f"⭐ Your final score: {score}")
if score > highscore:
print("🏆 You set a new high score!")
with open(highscore_file, "w") as file:
file.write(str(score))
break

if guess != number_to_guess and lives == 0:
print(f"\n💀 You're out of lives. The correct number is {number_to_guess}")

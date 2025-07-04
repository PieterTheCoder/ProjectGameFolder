player = {
    "name": input("Enter player name: "),
    "score": 0,
    "lives": 3
}

questions = [
    "Is Python a programming language? (yes/no): ",
    "Is 2 + 2 = 5? (yes/no): ",
    "Can you make games with Python? (yes/no): "
]

answers = ["yes", "no", "yes"]

for i in range(3):
    print("\nQuestion", i + 1)
    user_answer = input(questions[i]).lower()
    if user_answer == answers[i]:
        print("✅ Correct!")
        player["score"] += 10
    else:
        print("❌ Wrong!")
        player["lives"] -= 1

print("\n=== Final Result ===")
print("Name :", player["name"])
print("Score:", player["score"])
print("Lives left:", player["lives"])

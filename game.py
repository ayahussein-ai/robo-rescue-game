print("--- Robo-Rescue Game ---")

name = input("Enter your name: ")
print(f"Welcome, Hero: {name}\n")

score = 0

print("Stage 1: You have two paths to reach the fire.")
print("1. Fast Track (High battery consumption)")
print("2. Safe Track (Slow but safe)")
choice1 = input("Choose (1 or 2): ")

if choice1 == "1":
    score += 10
    print("-> You chose the fast track, you arrived quickly!\n")
else:
    score += 5
    print("-> You chose the safe track, you arrived calmly.\n")

print("Stage 2: A box obstacle appeared in your way!")
print("1. Use the crane to move it")
print("2. Use the laser to cut the box")
choice2 = input("Choose (1 or 2): ")

if choice2 == "1":
    score += 15
    print("-> Box moved successfully!\n")
else:
    score += 20
    print("-> Box cut quickly with laser!\n")

print("------------------------")
print(f"Engineer {name}'s Result")
print(f"Total Score: {score}")

if score >= 25:
    print("Winner! Excellent performance 🏆")
else:
    print("Good job, you finished the mission! 👍")
print("------------------------")

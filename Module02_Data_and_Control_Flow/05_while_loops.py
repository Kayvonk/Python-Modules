# 05_while_loops.py
# 🔁 Let's learn how to use 'while' loops!

# A while loop keeps running as long as a condition is True.

count = 1

while count <= 5:
    print(f"Count is: {count}")
    count += 1  # same as count = count + 1

# 🎯 Your turn:
# Write a while loop that asks the user to guess a secret number (between 1 and 10).
# Keep asking until they get it right!

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number (1-10): "))
    if guess != secret_number:
        print("Try again!")

print("🎉 You got it!")

# ✨ Bonus Challenge:
# Modify the loop to count how many guesses it took the user.

# ✅ Practice makes perfect!

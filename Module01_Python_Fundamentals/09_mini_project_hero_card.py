# 09_mini_project_hero_card.py
# 🦸 Hero Card Generator — Your First Python Project!

# 🎯 Goal:
# Ask the user for information about their superhero character,
# then print out a cool "hero card" using their answers.

# Step 1: Ask for info
hero_name = input("What is your superhero name? ")
power = input("What is your superpower? ")
age = input("How old is your hero? ")
symbol = input("Choose an emoji to represent your hero: ")

# Step 2: Print a blank line for spacing
print("\n--- YOUR HERO CARD ---")

# Step 3: Print the hero card
print(f"{symbol} Meet {hero_name}!")
print(f"💥 Power: {power}")
print(f"🎂 Age: {age}")
print(f"{hero_name} is ready to save the world! 🌍")

# 🧠 Bonus:
# Add a catchphrase or weakness
catchphrase = input("What is your hero’s catchphrase? ")
weakness = input("What is their weakness? ")

print(f"🗯️ Catchphrase: \"{catchphrase}\"")
print(f"⚠️ Weakness: {weakness}")

# ✅ You did it! Try running your program multiple times with different heroes.

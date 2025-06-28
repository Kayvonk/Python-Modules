# 02_comparison_operators.py
# 🔍 Let's compare values with Python!

# Comparison operators let you ask questions like:
# "Is this number bigger?", "Are these equal?", etc.

# 🧪 Examples:

print(5 > 3)      # True
print(10 < 1)     # False
print(7 == 7)     # True
print(8 != 6)     # True (means "not equal")
print(4 >= 4)     # True
print(3 <= 2)     # False

# 🧠 You can use these in if statements:

age = 15

if age >= 13:
    print("You’re a teenager!")
else:
    print("You’re not a teenager yet.")

# 🎯 Your turn:
# Ask the user for their score and print if they passed (60 or higher)

score = int(input("What was your score on the quiz? "))

if score >= 60:
    print("✅ You passed!")
else:
    print("❌ Try again next time!")

# ✨ Bonus Challenge:
# Ask the user for their height in inches and tell them if they’re tall enough
# to ride a rollercoaster (48 inches minimum)

height = int(input("How tall are you (in inches)? "))

if height >= 48:
    print("🎢 You can ride the rollercoaster!")
else:
    print("🚫 Sorry, you’re not tall enough yet.")

# ✅ Try changing the values and test different comparisons!

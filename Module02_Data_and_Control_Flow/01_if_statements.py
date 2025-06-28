# 01_if_statements.py
# 🧠 Let's make decisions using if statements!

# Python can run different code depending on conditions.
# Use `if`, `elif`, and `else` to control what happens.

# Example:
age = 12

if age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
else:
    print("You're an adult!")

# 🎯 Your turn:
# Ask the user how many hours they slept and respond with a message

hours = int(input("How many hours did you sleep last night? "))

if hours >= 8:
    print("Nice! You're well rested 😴")
elif hours >= 5:
    print("You might need a nap soon 🥱")
else:
    print("Yikes! Try to sleep more tonight 😬")

# 🧠 Challenge:
# Ask the user what temperature it is and print a message:
# - "It's hot!" if over 90
# - "It's nice out." if 60–90
# - "Brrr... it's cold!" if under 60

temp = int(input("What’s the temperature today (°F)? "))

if temp > 90:
    print("It's hot! ☀️")
elif temp >= 60:
    print("It's nice out. 🌤️")
else:
    print("Brrr... it's cold! ❄️")

# ✅ Try changing values and running your code again!

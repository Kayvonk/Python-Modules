# 06_string_concatenation.py
# 🧵 Let's combine text using strings!

# ➕ You can "add" strings together to make a longer message

greeting = "Hello"
name = "Jordan"

# Combine the two with a space
message = greeting + " " + name
print(message)

# 🧠 You can also include emojis or punctuation
print(name + " is coding in Python! 💻")

# 🔢 You can combine strings with numbers, but you must convert the number to a string
age = 13
print("I am " + str(age) + " years old.")

# ✨ Try this: store a favorite food and activity, and build a sentence

food = "sushi"
activity = "skateboarding"

print("I love eating " + food + " after " + activity + "! 🍣🛹")

# 🎯 Bonus: Use an f-string to make your code cleaner
print(f"{name} is {age} years old and loves {food}!")

# 🧠 Challenge:
# Ask the user for their favorite game and why they like it, then print a message.

game = input("What’s your favorite game? ")
reason = input("Why do you like it? ")

print(f"{game} is awesome because {reason}! 🎮")

# ✅ Run your code and try different answers!

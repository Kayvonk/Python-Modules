# 06_dictionary_basics.py
# 📦 Let's learn about dictionaries — labeled boxes for storing data!

# A dictionary stores key-value pairs, like a contact list.

# Example dictionary for a person
person = {
    "name": "Jamie",
    "age": 14,
    "favorite_color": "green"
}

# Print the whole dictionary
print(person)

# Access values by their keys
print(person["name"])
print(person["age"])

# Add a new key-value pair
person["hobby"] = "soccer"
print(person)

# 🎯 Your turn:
# Create a dictionary for your favorite game with keys: title, genre, and rating

game = {
    "title": "Minecraft",
    "genre": "Sandbox",
    "rating": 9.5
}

print(game)

# ✨ Bonus Challenge:
# Change the rating to a new number and print the updated dictionary

game["rating"] = 10
print(game)

# ✅ Try creating dictionaries for different things you like!

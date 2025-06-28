# 07_input_decision_game.py
# 🎮 Let's make a simple decision-based game!

print("Welcome to the Adventure Game!")
print("You find yourself at a fork in the road.")

# Ask the player which way to go
choice = input("Do you go left or right? ").lower()

if choice == "left":
    print("You meet a friendly dragon who shares treasure with you! 🐉💰")
elif choice == "right":
    print("You fall into a trap! Try again next time. 🕳️")
else:
    print("You stand still, unsure what to do. The adventure ends here.")

# ✨ Bonus Challenge:
# Add another question and make the game longer!

# ✅ Have fun trying different paths!

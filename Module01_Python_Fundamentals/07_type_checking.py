# 07_type_checking.py
# 🔍 What kind of data are you using?

# Every value in Python has a **type**: string, integer, float, boolean, etc.

# 🧪 Use the type() function to check what type a variable is

name = "Zoe"
age = 11
height = 4.9
is_student = True

print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student))# <class 'bool'>

# 🔄 Let's mix types and see what happens

print("Your age is " + str(age))  # Convert number to string

# ❌ What happens if you forget to convert?
# print("Your age is " + age)  # This will give an error!

# ✨ Ask the user for their age and tell them what type it is

user_age = input("How old are you? ")
print("You entered:", user_age)
print("Type of your input:", type(user_age))  # Always string!

# Convert it to a number
user_age_number = int(user_age)
print("Now it's a number:", user_age_number)
print("New type:", type(user_age_number))

# 🧠 Challenge:
# Ask the user to enter any number, then double it

user_number = input("Enter a number: ")
number = float(user_number)  # Supports decimals too!
print("Double your number is:", number * 2)

# ✅ Tip: Always check your types when mixing strings and numbers!

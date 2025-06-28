# 05_basic_math.py
# ➕ Let's do some math with Python!

# Python can do all the basic math operations just like a calculator.

# ➗ Try some simple calculations
print(5 + 3)     # addition
print(10 - 4)    # subtraction
print(6 * 2)     # multiplication
print(8 / 2)     # division

# 🧠 You can also store numbers in variables
num1 = 7
num2 = 3

# ➕ Add them together
print(num1 + num2)

# ✖️ Multiply them
print(num1 * num2)

# 🔢 Do more math with parentheses
result = (num1 + num2) * 2
print(result)

# 🔍 Bonus: Try using exponentiation and modulus
print(2 ** 3)  # 2 to the power of 3 = 8
print(10 % 3)  # 10 divided by 3 leaves a remainder of 1

# 🧮 Challenge:
# Ask the user for two numbers, then add them together and print the result.

num_a = input("Enter a number: ")
num_b = input("Enter another number: ")

# input() gives us strings, so we need to convert to integers
sum_total = int(num_a) + int(num_b)

print(f"The sum of {num_a} and {num_b} is {sum_total}!")

# ✅ Try changing numbers and playing with different math operations!

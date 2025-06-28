# 09_module_review.py
# 📚 Review time! Let's test your knowledge of data and control flow.

# Question 1: What does this print?
print(5 > 3)  # True or False?

# Question 2: What will the output be?
x = 10
if x < 5:
    print("Less than 5")
else:
    print("5 or more")

# Question 3: What is the value of the third item in this list?
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[2])

# Question 4: What does this code print?
count = 1
while count <= 3:
    print(count)
    count += 1

# Question 5: What type of data is this?
person = {"name": "Sam", "age": 15}
print(type(person))

# Bonus: Write a short if statement that prints "Hello!" if a number is even, and "Bye!" if odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Hello!")
else:
    print("Bye!")

# ✅ Great job reviewing!

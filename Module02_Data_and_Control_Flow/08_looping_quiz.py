# 08_looping_quiz.py
# ❓ Let's create a quiz that repeats until you get the right answer!

# The answer to the question
correct_answer = "python"

# Initialize user's answer
user_answer = ""

while user_answer.lower() != correct_answer:
    user_answer = input("What programming language are we learning? ")
    if user_answer.lower() != correct_answer:
        print("Nope, try again!")
    else:
        print("Correct! Great job! 🎉")

# ✨ Bonus Challenge:
# Add more questions or give hints after wrong answers.

# ✅ Practice makes perfect!

# Chip Rater
# Author: Tim
# 1 Nov 2023

# Interview people about their perception
# of how delicious chips are based on a set of questions. 
# In the end we'll give an aggregate score
# Greet the user
print("Please answer these questions after eating the chipps")

# Create a list of all of the chips
questions = [
    "How crispy is the chip on a scale from 1 - 5? 5 crispiest and most amazing sounding and 1 means it sounds like nothing and leaves you unsatisfied", 
    "How would you rate the chip out of 5? 5 is the the best and most delicious and 1 is horrible and I would rather eat dirt", 
    "How would you rate the packaging out of 5? 5 is that you would pay just for the packaging and 1 is that you're questioning how it was even packaged"
]

final_score = 0


# Ask the questins to the user
for question in questions:
    print(question)

    # stor their responses
    rating = int(input().strip(",?.! "))
    final_score += rating

# Do some math
average_score = final_score / len(questions)


# Presenty the result to the user 
print(f"average score of this chip is: {average_score:.2f}/ 5")
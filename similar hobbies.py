# Similarity score
# Author: Tim
# Nove 14 2023

print("Please enter in your hobbies seperates by spaces")
Hobby1 = input("Person 1:").lower().split()
Hobby2 = input("Person 2:").lower().split()

similarity_score = 0

for Hobby in Hobby1:
    if Hobby in Hobby2:
        similarity_score += 1

print(f"Here is your score {similarity_score} score!")
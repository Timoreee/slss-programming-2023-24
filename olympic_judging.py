# Olympic Judge 
# Author Tim
# 1 Nov 20

# Get scores from 5 judges
scores = []
for i in range(5):
    score = float(input(f"Enter Judge {i + 1}'s score (0-10): "))
    scores.append(score)

# Calculate and display the average score
end_score = sum(scores) / 5
print(f"The average score is: {end_score:.1f}")





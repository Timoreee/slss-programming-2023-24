# Comparing Similarity Scores
# Author: Tim
# 8 Nov 2023

# Create 2 lists that represent the movies
# that people like
Tims_favourite_movies = [ 
    "Pacific Rim",
    "Avengers Infinity War",
    "Lilo and Stitch",
    "The little prince",
    "Iron Man"
]

Ethans_favourite_movies = [
    "How's Moving castle",
    "Cowboy Bebop",
    "Pacific Rim"
    "Siper man, into the spiderverse"
]
# Calculate scores between 2 people

# Initialize the similarity score

similarity_score = 0

#Iterate through all movies in the first list
for movie in Tims_favourite_movies:
    if movie in Ethans_favourite_movies:
        similarity_score += 1


# For each item in the list
    # 
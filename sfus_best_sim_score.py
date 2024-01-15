# SFU's Best
# Author: Tim
# Nov 10 2023

# Load data from .csv file
# Read it in a meaningful way
# Link our similarity score algo to the data

# Open the file
with open("./data.csv") as f:
# Read the first line of code
    # read the first line of data

    f.readline()

# create a "profile" for someone that shows their favourite places at SFU
profile = [
    "Bubble World",
    "Chef Hung",
    "Uncle Fati's",
    "Guadalupe (MBC)",
    "Steve's Poke Bar"
]

# Initialize our top similarity score and their name 
bot_sim_score = 0
bot_sim_name = ""
with open("./data.csv") as f:
    # Throw away header line
    header = f.readline()



    # for every data line of data in the file (string)
    for line in f:
        # convert the line of data into a list
        current_likes = line.split(",")

    # initialize the CURRENT similarity score
    # Store the current user's name
    current_sim_score = 0
    current_name = current_likes[1]
        # for everyy item in our PROFILE
    for item in profile:
            if item in current_likes:
                current_sim_score += 1
         # sim score algo
    # print out the current sim_score
    print(f"{current_name} - Score: {current_sim_score}")

    # if the cur score is < top sim score
    if current_sim_score < bot_sim_score:
        # update the top sim score and the name
        bot_sim_score = current_sim_score
        bot_sim_name = current_name

print("🎖️🎖️🎖️🎖️LEAST SIMILAR PERSON!🎖️🎖️🎖️🎖️")
print(f"{bot_sim_name} - Score: {bot_sim_score}")

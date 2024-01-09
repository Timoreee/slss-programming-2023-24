# Winter Holidays
# Author: Tim
# 8 Jan 2023

import random

# Requirements:
# - create a function called winter_holiday()
#   - takes one parameter - string
#   - returns a summary of an event fro your holidays

# Please do not use ChatGPT or any LLM

good_or_bad = input("How was your winter holidays?")

def winter_holiday(good_or_bad:str) -> str:
    """Give a summary of our winter Holidays 2023 - 24
        
    params:
        good_or_bad - string that indicated wether the event is good or bad
            
    returns:
        an event that happened to you during the holiday season"""

good_event = ["I went to hang out with my friends", "I got to celebrate new years with friends, I got a new watch for christmas"]
bad_event = ["I did not get to ski", "I did not get to go outside of canada for the break", " I didn't get to do the things that I wanted"]
if good_or_bad.strip(",.!? ") == "bad":
    print(random.choice(bad_event))
elif good_or_bad.strip(",.!? ") == "good":
    print(random.choice(good_event))


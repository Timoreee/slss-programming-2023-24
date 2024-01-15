# Parent Bot
# Author: Tim
# 24 November 2023

questions_score = 0
print(" This is your dad and I'm just checking to see if you are doing okay")
eat = input("Did you eat?").strip(",.!? ").lower
if eat == "yes":
    questions_score += 1

study = input("Did you study?").strip(",.!? ").lower
if study == "yes":
    questions_score += 1

laundry = input("Did you do your laundry?").strip(",.!? ").lower
if laundry == "yes":
    questions_score += 1

grandma = input("Did you call grandma?").strip(",.!? ").lower
if grandma == "yes":
    questions_score += 1

if questions_score == 0:
    print("I'm coming over")
elif questions_score == 1 or 2:
    print("OK")
elif questions_score >= 3:
    print("Good!")

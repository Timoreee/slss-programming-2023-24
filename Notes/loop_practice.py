# Loop Practice
# Author: Time
# Date: 10 Oct 2023

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games"]

# Do something for each thing in the list
# print it out in a pretty way
# e.g.
#
#     * hot wheels
#       ---
#
#     * lego
#       ---
#       etc.
#
# print(f"* {grocery[0]})
# print(f" ----")
#
#
#

for item in groceries:
    print(f"* {item}")
    print(f"---")

# using the above methose, create the thing below:
# *
# **
# ***
# ****
# *****
# *****
# ******
# *******
# ********
# *********
# **********

pyramid = ["*", "**", "***", "****", "*****", "******", "*******", "********", "*********"]

for item in pyramid:
    print(f"* {item}")

# Problem:
# Create a New years count down that is automated
# Requriements:
# Starts at 10
# Counts down by one second
# Instead of [rinting 0 it prints out happy new year!]
#e.g.
# 10
# 9
# 8
# 7
# 6
# etc
import time
countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "🎉🎇Happy New Year 🎆🎉"]

for item in countdown:
    print(f"* {item}")
    time.sleep (1)













---
tags:
  - recommendation-systems
  - programming-level-2
  - algorithms
---
# Recommendation Systems

## Popularity and Likes

This type of paradigm makes a suggestion based on how many people lie the thing
One prime example of this is the like button (heart) in instagram. When you click that heart, instagram records it, and based on information it has on you, it might suggest that someone else that is similar to you.

We created the Favourite Bubble Tea service which is based on the "Popularity/Likes" paradigm of recommendation systems


# N-Point Rating Systems
N-Point rating systems are used by many services but one that nearly everyone is familiar with is Amazon's main purchasing service.

This paradigm is where user rate a product out of a certain number.

## Similarity Scores

Amazon, and Netflix, and Meta all use similarity scores to help drive users to their platform.

Example: Amazon
Ubial likes ["nintendo switch", "usb charger", "4k blu ray movies"]
Ben Ubial likes["nintendo switch", "usb charger", "lego"]
Fido likes["lego", "chew toys", "dog food"]

Similarity score between Ubial and Ben Ubial: 2
Similarity score between Ubial and Fido: 0
Similarity score between Ben Ubial and Fido: 1
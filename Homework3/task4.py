import random

color_of_card = random.randint(1, 4)

if color_of_card == 1:
    color_of_card = "Club"
elif color_of_card == 2:
    color_of_card = "Diamond"
elif color_of_card == 3:
    color_of_card = "Heart"
else:
    color_of_card = "Spade"

random_number_of_card = random.randint(1, 13)

if random_number_of_card == 1:
    number_of_card = "Ace"
elif random_number_of_card == 11:
    number_of_card = "Jack"
elif random_number_of_card == 12:
    number_of_card = "Queen"
elif random_number_of_card == 13:
    number_of_card = "King"
else:
    number_of_card = random_number_of_card

print(f"you have {number_of_card} of {color_of_card}!!! ")
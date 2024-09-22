from random import randint

number_of_players = int(input("How many players are playing ? "))


for i in range(0, number_of_players):
        
        first_dice = randint(1, 6)

        second_dice = randint(1, 6)

        print(first_dice, second_dice)

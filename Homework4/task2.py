from random import randint

num = int(input("Enter Number: (0 - 30) - "))

if num <= 0 or num >= 30:
    print("Invalid Input")
    exit(1)

for i in range (0, num):
    print(randint(1, 1000))
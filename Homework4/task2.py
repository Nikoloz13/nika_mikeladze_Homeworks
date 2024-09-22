from random import randint

num = int(input("Enter Number: (0 - 30) - "))

if num <= 0 or num >= 30:
    print("Invalid Input")
    exit(1)

max_num = 0

for i in range (0, num):
    random_num = randint(1, 1000)
    print(random_num)

    if random_num > max_num:
        max_num = random_num

print("The maximum number is:", max_num)        
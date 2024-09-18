first_num = float(input("Enter First Number - "))
second_num = float(input("Enter Second Number - "))

natural_num = first_num % second_num == 0

if first_num >= 0 and second_num >= 0:
    if natural_num:
        print(f"The first number is a multiple of the second number! The result is - {first_num / second_num} ")
    else:
        print("The first number is not a multiple of the second number!  ")    
else:
    print("first or second num is negative number, or both of them are negatives. Invalid Input!!! ") 
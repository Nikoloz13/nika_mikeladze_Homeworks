from math import log, log2 

num = int(input("Enter a number from 1 to 10: "))
half = int(num / 2)

if(num > 0 and num <= 10):
    if(num == 1):
        print('1' * 2)
    elif(log2(num).is_integer() and num / 2 != 1):
        print('2' * int(log2(num)))
    elif(log(num,3).is_integer() and num / 3 != 1):
        print('3' * int(log(num,3)))
    elif(num % 2 == 0):
        print('2' + str(half))
    else:
        print(str(num) + '1')
else:
    print("invalid input")





num = int(input("Enter the number from 1-999: "))

if 0 < num < 1000:
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")    
else:
    print("Invalid Input!!! ")
                
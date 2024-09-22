num = int(input("Enter Any Number Between (0 - 20) "))

if num < 0 or num > 20:
    print("Invalid Input")
    exit(1)
else:
    if num == 0:
        print(0)
    elif num == 1:
        print(1)
    else:
        a, b = 0, 1
        
    for _ in range(2, num + 1):
        a, b = b, a + b


print(f"{num} : {b}")

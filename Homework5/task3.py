natural_num = int(input("Enter any Positive Integer (0 - 19): "))

if natural_num < 0 or natural_num >= 20:
    print("Invalid Input!!!")
    exit(1)

count = 0

a, b = 0, 1    
    
while count <= natural_num:
    print(a, end= " ")
    a, b = b, a + b
    count += 1

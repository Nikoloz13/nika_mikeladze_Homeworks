natural_num = int(input("Enter any positive Integer (0 - 49): "))

if natural_num <= 0 or natural_num >= 50:
    print("Invalid Input!!!")
    exit(1)

print(" " * natural_num + "*")

i = 0 


while i < natural_num:
    print(" " * (natural_num - i - 1), end = "")
    print("/" * (i + 1) + "|" + "\\" * (i + 1))
    i += 1

print(" " * natural_num + "|")
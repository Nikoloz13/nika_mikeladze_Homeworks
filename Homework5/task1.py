natural_num = int(input("Enter any Natural Number (0 - 50): "))

if natural_num <= 0 or natural_num >= 50:
    print("Invalid Input")
    exit(1)
else:
    i = 1
    while i <= natural_num:
        count = 0
        print(f"{i} - ", end= "")
        seperator = 1
        while seperator <= i:
            if i % seperator == 0:
                print(seperator, end = " ")
                count += 1
            if count == 3:
                break
            seperator += 1
        print()
        i += 1        
        
i = 1

while i <= 9:
    j = 1
    while j <= i:
        multiple = i * j
        print(f"{j} * {i} = {multiple}", end="  " )
        j += 1
    print()    
    i += 1
car_speed = int(input("Enter your car speed in km/h: "))

if car_speed > 0 and car_speed < 30:
    print("Your car is SLOW!!! ")
elif car_speed > 120:
    print("Your car is very FAST!!! ")
elif car_speed > 60 and car_speed < 120:
    print("Your car is FAST!!! ")
elif car_speed > 30 and car_speed < 60:
    print("Your car is MODERATE!!! ")
else:
    print("Unknown Speed!!! ")     
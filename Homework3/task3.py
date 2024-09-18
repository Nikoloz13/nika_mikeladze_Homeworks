import datetime

year_of_birthday = int(input("Enter The year you were born: "))
month_of_birthday = int(input("Enter The month you were born (as an integer): "))
day_of_birthday = int(input("Enter The day you were born: "))


birth_date = datetime.date(year_of_birthday, month_of_birthday, day_of_birthday)

day_of_week = birth_date.strftime("%A")
    
print(f"You were born on a {day_of_week}.")
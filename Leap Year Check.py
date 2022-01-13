print("Enter the year to check if it is a leap year")

year = int(input("> "))

def leap_year():

    if (year % 400 == 0 or year % 100 != 0) and (year % 4 == 0):
        print(year, "is a leap year!")

    else:
        print(year, "is not a leap year")

leap_year()
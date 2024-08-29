def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return "LEAP"
    else:
        return "COMMON"

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    print(is_leap_year(year))
    
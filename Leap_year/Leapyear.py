Month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    #  True = For Leap Year

    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


"""for year in range(2000,2020):
    print(year,is_leap(year))"""


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return ' Invalid Month'
    if month == 2 and is_leap(year):
        return 29

    return Month_days[2]


A = int(input("Enter year : "))
B = int(input("Enter month (1-12)"))

print(days_in_month(A, B))

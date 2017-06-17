def numberOfDaysInAYear(year):
    days = 0
    isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if isLeapYear:
        days = 366
    else:
        days = 365
    return days

days = 0

for i in range(2010,2020):
    days += numberOfDaysInAYear(i)
print(days)

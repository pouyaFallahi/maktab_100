import datetime as dt
import calendar

def calculator_leap_years(start, end):
    count = 0
    for i in range(start.year, end.year + 1):
        if calendar.isleap(i):
            count +=1
    return count


first = input('pleas enter firs date:')
second = input('pleas enter firs date:')

first = dt.datetime.strptime(first, '%Y/%m/%d-%H:%M:%S')
second = dt.datetime.strptime(second, '%Y/%m/%d-%H:%M:%S')
difference = abs(first-second)

leap_year = calculator_leap_years(first, second)

print(difference.total_seconds())
print(leap_year)
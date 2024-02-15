def get_days_in_month(*, year: int, month: int) -> int:
    if month in [9, 4, 6, 11]:
        return 30
    elif month == 2 and year % 4 == 0 and year % 400 != 0:
        return 29
    elif month == 2:
        return 28
    else:
        return 31


num_sundays_on_1sts = 0
year = 1900
month = 1
day = 1
while year < 2001:
    if day == 1 and year >= 1901:
        num_sundays_on_1sts += 1
    days_in_month = get_days_in_month(year=year, month=month)
    day += 7
    if day >= days_in_month + 1:
        day -= days_in_month
        month += 1
    if month > 12:
        month -= 12
        year += 1
print(num_sundays_on_1sts)

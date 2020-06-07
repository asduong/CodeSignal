import math
def centuryFromYear(year):
    if year % 100 == 0:
        return year/100
    elif year % 100 != 0:
        year = year / 100
        return math.ceil(year)


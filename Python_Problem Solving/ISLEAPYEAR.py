"""
To determine whether a year is a leap year, follow these steps: 
1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
4. The year is a leap year (it has 366 days). The method isLeapYear needs to return true.
5. The year is not a leap year (it has 365 days). The method isLeapYear needs to return false.
"""

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            leap = True
        elif year % 400 == 0:
            leap = True
    else:
        leap = False
        
    return leap

print(is_leap(1992))
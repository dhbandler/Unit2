#Daniel Bandler
#1/5/18
#ageCalculator.py Calculates one's age

from datetime import date

year=int(input("What year were you born in? "))



month=int(input("What month were you born in? "))



day=int(input("What day of the month were you born on? "))


tentage=date.today().year-year

if month < date.today().month:
    print(tentage)
elif month == date.today().month and day <= date.today().day:
    print(tentage)
else:
    print(tentage-1)
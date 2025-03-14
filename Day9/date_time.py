import datetime

# my_hour = datetime.time(hour=8, minute=0, second=0, microsecond=0)
my_hour = datetime.time(17,35, 50, 1500)
print(type(my_hour))
print(my_hour)
print(my_hour.hour)

my_day = datetime.date(2025, 10, 25)
print(my_day)
print(my_day.year)
print(my_day.ctime())
print(my_day.today())

from datetime import datetime

my_date = datetime(2020, 10, 25, 22, 10, 15, 626340)
print(my_date)

my_date = my_date.replace(year=2020, month=12, day=31)
print(my_date)

birth = datetime(1996, 7, 31)
death = datetime(2025, 6, 19)
life = death - birth
print(life.days)

wake = datetime(2022, 10, 5, 7, 30)
sleep = datetime(2022, 10, 5, 23, 45)
vigil = sleep - wake
print(vigil.seconds)

minutes = 
print(minutes)

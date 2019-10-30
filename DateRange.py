
from datetime import datetime
from datetime import timedelta

d1 = datetime.strptime('2019-02-20','%Y-%m-%d')
d2 = datetime.strptime('2019-02-28','%Y-%m-%d')
day_dif = abs((d2 - d1).days)
if day_dif > 0 :
    for i in range(day_dif+1):
        print(d1.date() + timedelta(days=i))
import calendar
import datetime

DATE_FORMAT = "%Y%m%d"

today = datetime.datetime.strptime("20191031",DATE_FORMAT)
# last_saturday = today - datetime.timedelta(days=5)
# print(today.weekday())
# print(last_monday)
offset = (today.weekday() - 5) % 7
last_saturday = today - datetime.timedelta(days=offset)
last_sunday = last_saturday.date()- datetime.timedelta(days=6)

# last_sunday = last_saturday.strftime(DATE_FORMAT) - datetime.datetime(days=7)

print(last_sunday.strftime(DATE_FORMAT))
print(last_saturday.strftime(DATE_FORMAT))
# print(last_sunday.strftime(DATE_FORMAT))

start_date = datetime.datetime.strptime("20160912",DATE_FORMAT)
end_date = datetime.datetime.strptime("20191030",DATE_FORMAT)

print(start_date)
print(end_date)

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

month_diff = int(diff_month(end_date,start_date))

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month+1, day=1) - datetime.timedelta(days=1)

for x in range(month_diff+1):
    print(last_day_of_month(add_months(start_date,x)))
def previous_week(today):
    pass
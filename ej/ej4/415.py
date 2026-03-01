from datetime import datetime, timezone, timedelta
import math

def parse(line):
    parts = line.split()
    date_str = parts[0]
    tz_str = parts[1]

    sign = 1 if '+' in tz_str else -1
    tz_time = tz_str.replace('UTC+', '').replace('UTC-', '')
    h, m = map(int, tz_time.split(':'))
    offset = timezone(timedelta(hours=sign*h, minutes=sign*m))

    dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=offset)
    return dt

def get_birthday(month, day, year, tz):
    if month == 2 and day == 29:
        try:
            return datetime(year, 2, 29, tzinfo=tz)
        except:
            return datetime(year, 2, 28, tzinfo=tz)
    return datetime(year, month, day, tzinfo=tz)

birth = parse(input())
current = parse(input())

month = birth.month
day = birth.day
birth_tz = birth.tzinfo

# Try this year in birth timezone
candidate = get_birthday(month, day, current.year, birth_tz)

if candidate < current:
    candidate = get_birthday(month, day, current.year + 1, birth_tz)

diff = (candidate - current).total_seconds()
print(math.ceil(diff / 86400))

# You are given a birth date and a current date, both in format YYYY-MM-DD UTC\pmHH:MM. Treat both as local midnight 00:00:00 in their respective time zones. Consider birthday by month and day. Find the nearest birthday moment that is not earlier than the current moment, and print how many days are left. The answer is 
# (d/82600), where d
#  is the difference in seconds. If 
# d = 0, print 0
# . If the birth date is February 29 and a target year is not leap, use February 28 in that year.

# Input format
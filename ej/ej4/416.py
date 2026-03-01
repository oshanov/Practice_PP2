from datetime import datetime, timezone, timedelta

def parse_time(s):
    # Разделяем строку: дата, время, UTC+hh:mm
    date_part, time_part, tz_part = s.split()

    # Парсим смещение
    sign = 1 if tz_part[3] == '+' else -1
    h = int(tz_part[4:6])
    m = int(tz_part[7:9])
    tz = timezone(sign * timedelta(hours=h, minutes=m))

    # Создаём datetime
    dt = datetime.strptime(date_part + " " + time_part, "%Y-%m-%d %H:%M:%S")
    return dt.replace(tzinfo=tz)

start = parse_time(input().strip())
end = parse_time(input().strip())

# Переводим в UTC и считаем разницу
duration = int((end.astimezone(timezone.utc) - start.astimezone(timezone.utc)).total_seconds())

print(duration)

#You are given the start and end of an event in format YYYY-MM-DD HH:MM:SS UTC\pmHH:MM. Compute event duration in seconds as end - start after converting both moments to UTC. 
#Input format The first line contains event start time. 
#The second line contains event end time. Each line has format YYYY-MM-DD HH:MM:SS UTC\pmHH:MM.
#Output format Print one integer: event duration in seconds.
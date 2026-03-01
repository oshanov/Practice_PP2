from datetime import datetime, timezone, timedelta

# Читаем даты из ввода
date1_str = input().strip()  # Например: "2025-01-01 UTC+00:00"
date2_str = input().strip()  # Например: "2025-01-02 UTC+00:00"

def parse_datetime(dt_str):
    # Разделяем на дату и часовой пояс
    date_part, tz_part = dt_str.split()
    
    # Разбираем часовой пояс
    sign = 1 if tz_part[3] == '+' else -1
    hours_offset = int(tz_part[4:6])
    minutes_offset = int(tz_part[7:9])
    tzinfo = timezone(timedelta(hours=sign*hours_offset, minutes=sign*minutes_offset))
    
    # Создаем datetime с timezone
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    dt = dt.replace(tzinfo=tzinfo)
    return dt

dt1 = parse_datetime(date1_str)
dt2 = parse_datetime(date2_str)

# Переводим обе даты в UTC
dt1_utc = dt1.astimezone(timezone.utc)
dt2_utc = dt2.astimezone(timezone.utc)

# Разница в секундах
delta_seconds = abs((dt2_utc - dt1_utc).total_seconds())

# Полные дни
full_days = int(delta_seconds // 86400)
print(full_days)

#You are given two date-time moments in the format YYYY-MM-DD UTC\pmHH:MM. Each date is interpreted as local midnight 00:00:00 in its own time zone. Compute the absolute difference between the two moments in full days.
#day 16 - 30 Day challenge: Date and Time
from datetime import datetime

now = datetime.now()
print(now)

t_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t_time)

date_str = '23 February, 2024'
date_str_obj = datetime.strptime(date_str, "%d %B, %Y")
print(date_str_obj)

new_year = datetime(year=2024,month=1,day=1)
time_diff = now-new_year
print(time_diff)

jan_one = datetime(year=1970,month=1,day=1)
large_time_diff = now - jan_one
print(large_time_diff)
from datetime import time 
from datetime import datetime

# 17:30:00
home = time(17, 30, 00)
print(home)

# 1997-08-14 06:32:13
birth = datetime(1997, 8, 14, 6, 32, 13) 
print(birth)

# year, month, day, hour, min, sec, ms
# 2023-07-20 15:13:07.413117
now = datetime.now()
print(now)

# For further techniques, especially how to detract units of time from a datetime, see:
# https://www.pythoncheatsheet.org/modules/datetime-module
from datetime import datetime, time, date
import random
print("I will give you a random date and time.")
time_seconds=random.randint(0,60)
time_hours=random.randint(0,24)
time_random=print("the random time is: ",time_hours,":",time_seconds)
date_day=random.randint(0,31)
date_month=random.randint(0,12)
date_year=random.randint(0,2026)
time_random=print("The random date is in terms of day/month/year is : ",date_day,"/",date_month,"/",date_year)
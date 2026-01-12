import random
# Sleep Format 2026-1-01 020:51:00;2026-1-02 07:51:00
# This imports in UTC so to get to MTN we have to shift times 7 hours forward therefore day 1 and 2 start on the subsequent days
# 5:00 UTC is really 22:00 MTN and 13:00 UTC is really 06:00
day1 = int(input("What day to start generating? 1, 2, 3 etc."))
month = int(input("What month would you like? 1, 2, 3"))
year = int(input("What year would you like? 1, 2, 3"))
day2 = day1 + 1
day1text = ""
day2text = ""
days_per_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
days_in_month = days_per_month[month - 1]


for x in range(0,days_in_month - day1):
    rand_hour1 = random.randint(3, 5)
    rand_hour2 = random.randint(13, 16)
    rand_minute1 = random.randint(10, 59)
    rand_minute2 = random.randint(10, 59)
    rand_second1 = random.randint(10, 59)
    rand_second2 = random.randint(10, 59)
    rand_hour1_text = "0" + str(rand_hour1)
    if day1 < 10:
        day1text = "0" + str(day1)
    else:
        day1text = str(day1)
    if day2 < 10:
        day2text = "0" + str(day2)
    else:
        day2text = str(day2)
    print(f"{year}-{month}-{day1text} {rand_hour1_text}:{rand_minute1}:{rand_second1};{year}-{month}-{day2text} {rand_hour2}:{rand_minute2}:{rand_second2}")
    day1 += 1
    day2 += 1
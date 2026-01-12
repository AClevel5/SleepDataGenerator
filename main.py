# Sleep Format 2026-1-01 020:51:00;2026-1-02 07:51:00
# This imports in UTC so to get to MTN we have to shift times 7 hours forward therefore day 1 and 2 start on the subsequent days
# 5:00 UTC is really 22:00 MTN and 13:00 UTC is really 06:00
day1 = 2
day2 = 3
day1text = ""
day2text = ""
# Set this to days in the month
days_in_month = 31
month = "01"
year = "2026"

for x in range(0,days_in_month - 1):
    if day1 < 10:
        day1text = "0" + str(day1)
    else:
        day1text = str(day1)
    if day2 < 10:
        day2text = "0" + str(day2)
    else:
        day2text = str(day2)
    print(f"{year}-{month}-{day1text} 05:00:00;{year}-{month}-{day2text} 13:00:00")
    day1 += 1
    day2 += 1
SECS_PER_DAY = 60 * 60 * 24
secs_per_day_count = 0
secs = 0
mins = 0
hrs = 0
while secs_per_day_count < SECS_PER_DAY:
    if secs == 60:
        mins += 1


        
        secs = 0
    if mins == 60:
        hrs+=1
        mins = 0
    if hrs == 12:
        hrs = 0
    if secs == mins == (hrs * 5):
        if secs_per_day_count < SECS_PER_DAY/2:
            print(f"{hrs} : {mins} : {secs}")
        else:
            print(f"{hrs + 12} : {mins} : {secs}")
    secs+=1
    secs_per_day_count +=1
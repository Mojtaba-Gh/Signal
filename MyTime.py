import time

def GetTime():
    Now = time.asctime()
    Now = Now.split(' ')
    hour = Now[3].split(':')[0]
    minute = Now[3].split(':')[1]
    return int(hour), int(minute)

def TimeDifrence(hour1, min1, hour2, min2):
    minute = 0
    if hour1 == hour2:
        minute = max(min1, min2) - min(min1, min2)
    elif hour1 > hour2:
        minute += 60 - min2
        minute += min1
        minute += (hour1 - hour2 - 1) * 60
    else:
        minute += 60 - min1
        minute += min2
        minute += (hour2 - hour1 - 1) * 60

    return minute

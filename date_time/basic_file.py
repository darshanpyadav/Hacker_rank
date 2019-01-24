import calendar

m, d, y = map(int, input().split())

print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())



from datetime import datetime as dt


fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) -
                   dt.strptime(input(), fmt)).total_seconds())))
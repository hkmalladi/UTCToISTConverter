import time
import datetime
import pytz

def convert_datetime_timezone(dt, tz1, tz2):
    tz1 = pytz.timezone(tz1)
    tz2 = pytz.timezone(tz2)

    dt = datetime.datetime.strptime(dt,"%Y%m%d%H%M%S.%f")
    dt = tz1.localize(dt)
    dt = dt.astimezone(tz2)
    dt = dt.strftime("%Y%m%d%H%M%S.%f")

    return dt

f = open('UTCList.txt','r')
lines = f.readlines()

for i in range(0,len(lines)):
  if len(lines[i]) > 0:
    floatLine = '{:.2f}'.format(float(lines[i]))
    lines[i] = str(floatLine)
    lines[i] = lines[i].rstrip()
    UTCDate = float(lines[i])
    t = convert_datetime_timezone(lines[i], "UTC", "Asia/Kolkata")
    print t

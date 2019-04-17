#!/usr/bin/env pyhont3
# -*- coding: utf-8 -*-

from datetime import datetime
now = datetime.now()
print(now)
print(type(now))
dt = datetime(2018, 8, 28, 12, 59)
print(dt)
print(now.timestamp())
ts = now.timestamp()
print(datetime.fromtimestamp(ts))
print(datetime.utcfromtimestamp(ts))

cday = datetime.strptime('2018-07-29  18:29:33', '%Y-%m-%d %H:%M:%S')
print(cday)
print(now.strftime('%a, %b %d %H:%M:%S'))

from datetime import timedelta
print(now)
print(now+timedelta(hours = 10, days = 2, minutes = 20))

from datetime import timezone

#创建时区UTC+8:00
tz_utc8 = timezone(timedelta(hours = 8))
now = datetime.now()
print(now)
dt = now.replace(tzinfo = tz_utc8)
print(dt)
tz_utc10 = timezone(timedelta(hours = -10))
dt = now.replace(tzinfo = tz_utc10)
print(dt)

utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print(bj_dt)
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9)))
print(tokyo_dt)
newyork_td = utc_dt.astimezone(timezone(timedelta(hours = -5)))
print(newyork_td)
newyork_td2 = bj_dt.astimezone(timezone(timedelta(hours = -5)))
print(newyork_td2)

import re
from datetime import datetime, timedelta, timezone

def to_timestamp(dt_str, tz_str):
	dt_regular = r'^\d{1,4}-\d{1,2}-\d{1,2}\s+\d{1,2}:\d{1,2}:\d{1,2}$'
	m = re.match(dt_regular, dt_str)
	if not m:
		raise ValueError('datetime format is not right') 	
	dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	tz_m = re.match(r'UTC(\+|\-)(\d{1,2}):(\d{1,2})', tz_str)
	if tz_m:
		print(tz_m.groups())
		sig = tz_m.group(1)
		hour = int(tz_m.group(2))
		min = int(tz_m.group(3))
		if sig == '+':
			tz = timezone(timedelta(hours = hour, minutes = min))
			return dt.replace(tzinfo = tz).timestamp()
		elif sig == '-':
			tz = timezone(timedelta(hours = -hour, minutes = -min))
			return dt.replace(tzinfo = tz).timestamp()
		else:
			raise ValueError('UTC ZONE format is not right')
	else:
		raise ValueError('UTC ZONE format is not right')


#测试
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0
to_timestamp('2015-5-31 16:10:30', 'UTC-09:20')
print('ok')








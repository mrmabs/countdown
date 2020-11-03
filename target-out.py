#!/usr/bin/python3
#
# non-curses version suitable for command-line or irc

import datetime, time, sys, select, pytz
from tzlocal import get_localzone

#format = "{days} days {hours:02d}:{minutes:02d}:{seconds:02d}"
format = "{days} days {hours:02d}:{minutes:02d}"

local = get_localzone()
nyc = pytz.timezone("America/New_York")
florida = pytz.timezone("US/Eastern")
cal = pytz.timezone("America/Los_Angeles")
alaska = pytz.timezone("America/Anchorage")

firstOpen   = nyc.localize(datetime.datetime(2020,11,3,6,0))
firstClosed = florida.localize(datetime.datetime(2020,11,3,19,0))
lastClosed  = alaska.localize(datetime.datetime(2020,11,3,20,0))

def strfdelta(tdelta, fmt):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)

def timestr(delta, name):
    return name + strfdelta(delta, format)

timenow = datetime.datetime.now()
print(timestr(firstOpen   - local.localize(timenow), "First Open:   "))
print(timestr(firstClosed - local.localize(timenow), "First Closed: "))
print(timestr(lastClosed  - local.localize(timenow), "Last Closed:  "))
print("Local time: " + local.localize(timenow).strftime("%H:%M"))
print("EST time:   " + datetime.datetime.now(nyc).strftime("%H:%M"))
print("PST time:   " + datetime.datetime.now(cal).strftime("%H:%M"))
print("AKST time:  " + datetime.datetime.now(alaska).strftime("%H:%M"))


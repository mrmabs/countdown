#!/usr/bin/python3
#

import datetime, time, curses, sys, select, pytz
from tzlocal import get_localzone

#format = "{days} days {hours:02d}:{minutes:02d}:{seconds:02d}"
format = "{days} days {hours:02d}:{minutes:02d}"

screen = curses.initscr()
screen.clear()

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

while True:
    timenow = datetime.datetime.now()
    screen.addstr(2, 5, timestr(firstOpen   - local.localize(timenow), "First Open:   "))
    screen.addstr(4, 5, timestr(firstClosed - local.localize(timenow), "First Closed: "))
    screen.addstr(6, 5, timestr(lastClosed  - local.localize(timenow), "Last Closed:  "))
    screen.addstr(8, 5,  "Local time: " + local.localize(timenow).strftime("%H:%M"))
    screen.addstr(10, 5, "EST time:   " + datetime.datetime.now(nyc).strftime("%H:%M"))
    screen.addstr(12, 5, "PST time:   " + datetime.datetime.now(cal).strftime("%H:%M"))
    screen.addstr(14, 5, "AKST time:  " + datetime.datetime.now(alaska).strftime("%H:%M"))
    screen.addstr(16, 0, "")
    screen.refresh()

    curses.napms(2000)

    if select.select([sys.stdin,],[],[],0.0)[0]:
        break

curses.endwin()

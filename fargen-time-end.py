#!/usr/bin/env python

import argparse, time
from datetime import datetime, timedelta
from dateutil.parser import parse

mysql_date_format_str="%Y-%m-%d %H:%M"
# Format var now
now = time.strftime(mysql_date_format_str)

parser = argparse.ArgumentParser(description='Set end of existing time instance.')
parser.add_argument('rowids', metavar="N", type=int, nargs=1,
	help='specify id of instance to complete')
parser.add_argument('-e','--end',
	help='specify end time of instance')

args = parser.parse_args()
if args.end:
    # Format user input
    strp_end = parse(args.end).replace(second=0, microsecond=0)
    args.end = strp_end.strftime(mysql_date_format_str)
else:
    args.end = now

t = (args.end, args.rowids[0],)

# DATABASE STUFF

import sqlite3
conn = sqlite3.connect('/home/chrisfargen/.fargen/time.sqlite')

c = conn.cursor()

# Insert a row of data
c.execute("UPDATE instance SET end = ? WHERE rowid = ?", t)

if c.rowcount:
    print "[INFO] ",args.rowids[0],"marked as done at",args.end,".",c.rowcount,"row(s) affected."

# Save (commit) the changes
conn.commit()

conn.close()

# source: http://docs.python.org/2/library/sqlite3.html

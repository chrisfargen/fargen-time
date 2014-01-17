#!/usr/bin/env python

import argparse, time
from datetime import datetime, timedelta
from dateutil.parser import parse

mysql_date_format_str="%Y-%m-%d %H:%M"
now = time.strftime(mysql_date_format_str)

parser = argparse.ArgumentParser(description='Set end of given time instance to now.')
parser.add_argument('rowids', metavar="N", type=int, nargs=1,
	help='specify id of instance to complete')

args = parser.parse_args()
# if args.start:
#     strp_start = parse(args.start).replace(second=0, microsecond=0)
#     args.start = strp_start.strftime(mysql_date_format_str)
#     #print "s: ",args.start
#     #print "s2:",strp_start
# if args.end:
#     strp_end = parse(args.end).replace(second=0, microsecond=0)
#     args.end = strp_end.strftime(mysql_date_format_str)
#     #print "e: ",args.end
#     #print "e2:",strp_end
# #if args.message:
#     #print "m: ",args.message
# #if args.instantaneous:
#     #print "i: ",args.instantaneous
# 
# if args.start and args.end:
#     #print "[INFO] START and END are specified"
#     if strp_start < strp_end:
# 	print "[INFO] Duration:", str(strp_end - strp_start)
# 	if args.instantaneous:
# 	    print "[ERR!] Option INSTANTANEOUS included"
# 	    exit(1)
# 	#else:
# 	    #print "[INFO] Option INSTANTANEOUS included"
#     elif strp_start == strp_end:
# 	#print "[INFO] Instance has no duration"
# 	if not args.instantaneous:
# 	    print "[ERR!] Option INSTANTANEOUS not included"
# 	    exit(1)
# 	#else:
# 	    #print "[INFO] Option INSTANTANEOUS included"
#     elif strp_start > strp_end:
# 	print "[ERR!] START is later than END"
# 	exit(1)
# elif args.start and not args.end:
#     #print "[INFO] No END specified"
#     if args.instantaneous:
# 	print "[INFO] Setting END to START by option INSTANTANEOUS"
# 	args.end = args.start
#     else:
# 	print "[INFO] No option INSTANTANEOUS supplied; assuming incomplete"
# elif args.end and not args.start:
#     #print "[INFO] No START specified"
#     if args.instantaneous:
# 	print "[INFO] Setting START to END by option INSTANTANEOUS"
# 	args.start = args.end
#     #else:
# 	print "[INFO] No option INSTANTANEOUS supplied; assuming incomplete"
# elif not args.start and not args.end:
#     print "[INFO] START and END not set;"
#     if args.instantaneous:
# 	print "[INFO] Option INSTANTANEOUS supplied; assuming current time"
# 	args.start = now
# 	args.end = now
#     else:
# 	print "[ERR!] Option INSTANTANEOUS not supplied"
# 	exit(1)
# 
# DATABASE STUFF

import sqlite3
conn = sqlite3.connect('/home/chrisfargen/.fargen/time.sqlite')

c = conn.cursor()

t = (str(now),args.rowids[0],)

# Insert a row of data
c.execute("UPDATE instance SET end = ? WHERE rowid = ?", t)

if c.rowcount:
    print "TIME:",args.rowids[0],"marked as done at",now,".",c.rowcount,"row(s) affected."

# Save (commit) the changes
conn.commit()

conn.close()

# source: http://docs.python.org/2/library/sqlite3.html

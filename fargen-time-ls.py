#!/usr/bin/env python

import argparse, time
from datetime import datetime, timedelta
from dateutil.parser import parse

mysql_date_format_str="%Y-%m-%d %H:%M"
now = time.strftime(mysql_date_format_str)

parser = argparse.ArgumentParser(description='Query time instance.')
parser.add_argument('-a', '--after',
	help='query for start and end dates after given date')
parser.add_argument('-b', '--before',
	help='query for start and end dates before given date')
parser.add_argument('keywords', metavar='KEYWORD', nargs='*',
	help='query for given keywords')
parser.add_argument('-n', '--null',
	dest='null',
	action='store_true',
	default=False,
	help='query for NULL messages')


args = parser.parse_args()
# if args.start:
#     strp_start = parse(args.start).replace(second=0, microsecond=0)
#     args.start = strp_start.strftime(mysql_date_format_str)
#     print "s: ",args.start
#     print "s2:",strp_start
# if args.end:
#     strp_end = parse(args.end).replace(second=0, microsecond=0)
#     args.end = strp_end.strftime(mysql_date_format_str)
#     print "e: ",args.end
#     print "e2:",strp_end
# if args.message:
#     print "m: ",args.message
# if args.instantaneous:
#     print "i: ",args.instantaneous
# 
# if args.start and args.end:
#     print "[INFO] START and END are specified"
#     if strp_start < strp_end:
# 	print "[INFO] Instance has duration", str(strp_end - strp_start)
# 	if args.instantaneous:
# 	    print "--> [ERR!] Option INSTANTANEOUS included"
# 	    exit(1)
# 	else:
# 	    print "--> [INFO] Option INSTANTANEOUS included"
#     elif strp_start == strp_end:
# 	print "[INFO] Instance has no duration"
# 	if args.instantaneous:
# 	    print "--> [INFO] Option INSTANTANEOUS included"
# 	else:
# 	    print "--> [ERR!] Option INSTANTANEOUS not included"
# 	    exit(1)
#     elif strp_start > strp_end:
# 	print "[ERR!] START is later than END"
# 	exit(1)
# elif args.start and not args.end:
#     print "[INFO] No END specified"
#     if args.instantaneous:
# 	print "--> [INFO] Setting END to START by option INSTANTANEOUS"
# 	args.end = args.start
#     else:
# 	print "--> [INFO] No option INSTANTANEOUS supplied; assuming incomplete"
# elif args.end and not args.start:
#     print "[INFO] No START specified"
#     if args.instantaneous:
# 	print "--> [INFO] Setting START to END by option INSTANTANEOUS"
# 	args.start = args.end
#     else:
# 	print "--> [INFO] No option INSTANTANEOUS supplied; assuming incomplete"
# elif not args.start and not args.end:
#     print "[INFO] START and END not set;"
#     if args.instantaneous:
# 	print "--> [INFO] Option INSTANTANEOUS supplied; assuming current time"
# 	args.start = now
# 	args.end = now
#     else:
# 	print "--> [ERR!] Option INSTANTANEOUS not supplied"
# 	exit(1)

# DATABASE STUFF

import sqlite3
conn = sqlite3.connect('/home/chrisfargen/.fargen/time.sqlite')

conn.row_factory = sqlite3.Row
c = conn.cursor()

tlist = []

for word in args.keywords:
    tlist.append("%" + word + "%")

tlist.append('%')


if args.null:
    subquery = 'message IS NULL'
    t = ()
elif not args.null:
    subquery = str( 'message LIKE ? AND ' * len(tlist) )[:-5]
    t = tuple(tlist)

query = 'SELECT rowid, start, end, round( cast( ( strftime("%s",end)-strftime("%s",start) ) AS real )/60/60, 2) AS duration, message FROM instance WHERE ' + subquery
c.execute(query, t)

sep = " "
for row in c.fetchall():
    print str(row['rowid']).rjust(4,"0"), sep, row['start'], sep, row['end'], sep, str(row['duration']).ljust(4,"0"), sep, row['message']

conn.close()

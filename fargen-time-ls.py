#!/usr/bin/env python

import argparse, time
from datetime import date, datetime, timedelta
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

default_date = (datetime.now() - timedelta(days=1)).strftime(mysql_date_format_str)
subquery_date = 'AND start > "' + default_date + '"'

args = parser.parse_args()
if args.after:
    strp_after = parse(args.after).replace(second=0, microsecond=0)
    args.after = strp_after.strftime(mysql_date_format_str)
    subquery_after = '(start > "' + args.after + '" or end > "' + args.after + '")'
    subquery_date = 'AND ' + subquery_after
    # print 'a: ',args.after
    # print 'a2:',strp_after
    print 'Displaying events after ', strp_after
if args.before:
    strp_before = parse(args.before).replace(second=0, microsecond=0)
    args.before = strp_before.strftime(mysql_date_format_str)
    subquery_before = '(start < "' + args.before + '" or end < "' + args.before + '")'
    subquery_date = 'AND ' + subquery_before
    # print 'b: ',args.before
    # print 'b2:',strp_before
    print 'Displaying events before', strp_before
if args.after and args.before:
    subquery_date = 'AND ' + subquery_after + ' AND ' + subquery_before
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
    subquery_message = 'message IS NULL'
    t = ()
elif not args.null:
    subquery_message = str( 'message LIKE ? AND ' * len(tlist) )[:-5]
    t = tuple(tlist)

subquery_orderby = "ORDER BY start DESC"

query = 'SELECT * FROM ( SELECT rowid, start, end, round( cast( ( strftime("%s",end)-strftime("%s",start) ) AS real )/60/60, 2) AS duration, message FROM instance WHERE ' + subquery_message + ' ' + subquery_date + ' ' + subquery_orderby + ' ) sub ORDER BY start ASC'
c.execute(query, t)

sep = ' '
total_duration = 0

for row in c.fetchall():
    print str(row['rowid']).rjust(4,' '), sep, row['start'], sep, row['end'], sep, str(row['duration']).ljust(4,'0'), sep, row['message']
    if row['duration'] != None:
	total_duration = total_duration + float(row['duration'])

print "Total: ", str(total_duration)

conn.close()

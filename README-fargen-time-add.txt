Usage:

# long version
fargen-time-add --start "2013-12-25 04:00" --end "2013-12-25 13:00" --message "I enjoyed this time." --project "socialize"

# short version
fargen-time-add -s "2013-12-25 04:00" -e "2013-12-25 13:00" -m "I enjoyed this time." -p "socialize"

# inline project
fargen-time-add --start "2013-12-25 04:00" -e "2013-12-25 13:00" -m "I enjoyed this time. +socialize"

# incomplete, possibly ongoing
fargen-time-add --start "2013-12-25 04:00"
fargen-time-add --end "2013-12-25 04:00"

# complete, instantaneous
fargen-time-add --start "2013-12-25 04:00" --instantaneous
fargen-time-add --end "2013-12-25 04:00" --instantaneous

# complete, instantaneous, short version
fargen-time-add -s "2013-12-25 04:00" -i

----------------------------------------------------------------

	START	END	INSTANTANEOUS	result
----------------------------------------------------------------
	yes	yes	yes		invalid

	yes	yes	no		if END is later than START, valid

	yes	no	yes		valid; set END to START

	yes	no	no		valid, incomplete

	no	yes	yes		valid; set START to END

	no	yes	no		valid, incomplete

	no	no	yes		set START and END to now

	no	no	no		set START and END to now




## Pseudocode

Parse command for valid arguments
    If > 0 invalid arguments
	Exit: time instance includes invalid arguments
Check logic of given arguments
    If START and END are defined
	If END - START < 0
	    Exit: time instance has negative duration
	If END - START > 0 and INSTANTANEOUS is True
	    Exit: time instance has contradicting arguments
	    

2.  If only one timestamp provided, assume instantaneous
3.  If no timestamp provided, assume current timestamp
4.  If only one date provided, assume other date

- [x] if START is defined and END is defined and START is earlier than END, then instance is of duration
- [x] if START is defined and END is defined and START is equal to END, then instance is instantaneous
- [x] if START is defined and END is defined and START is later than END, then instance is invalid
- [x] if START is defined and END is not defined and INSTANTANEOUS is True, instance is instantaneous
- [x] if START is not defined and END is defined and INSTANTANEOUS is True, instance is instantaneous
- [x] if START is not defined and END is not defined, then instance is instantaneous and END is set to time of execute

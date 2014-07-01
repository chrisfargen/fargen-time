Assumptions:

- User may wish to record instance with duration
- User may wish to record instance with no duration
- User may wish to record instance with incomplete details, perhaps to be amended at a later time
- User may wish to record instance with a message
- User may wish to record instance with no message


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

Config settings:

- AMBIGUITY_HANDLING={off,assume_unknown,assume_now}
- 

Rules:

1.  A valid command requires a prespecified minimum of options
    a.  If AMBIGUITY_HANDLING is "off", options must be sufficient to ascertain both START date and END date
    b.  If AMBIGUITY_HANDLING is not "off", options must be sufficient to ascertain either START date or END date
2.  A valid command requires valid values for all of its supplied options and no non-supplied options
    a.  Format of supplied value must match format expected
    b.  START date must precede END date
    c.  Options must be anticipated
3.  A valid command cannot contain contradictory options

----------------------------------------------------------------

	START	END	INSTANTANEOUS	value
----------------------------------------------------------------
	yes	yes	yes		invalid if START is not equal to END (rule #3)

	yes	yes	no		invalid if START is invalid (rule #2a);
	                                invalid if END is invalid (rule #2a);
	                                invalid if END > START (rule #2b);

	yes	no	yes		invalid if START is invalid (rule #2a)

	yes	no	no		invalid if START is invalid (rule #2a);
	                                invalid if AMBIGUITY_HANDLING is "off" (rule #1a)

	no	yes	yes		invalid if END is invalid (rule #2a)

	no	yes	no		invalid if END is invalid (rule #2a);
	                                invalid if AMBIGUITY_HANDLING is "off" (rule #1a)

	no	no	yes		set START and END to now

	no	no	no		invalid (rule #1)




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

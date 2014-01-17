Usage:

# Complete, long version
fargen-time-edit 203 --start "2013-12-25 04:00" --end "2013-12-25 13:00" --message "I enjoyed this time." --project "socialize"

# Complete, short version
fargen-time-edit 203 -s "2013-12-25 04:00" -e "2013-12-25 13:00" -m "I enjoyed this time." -p "socialize"

# Complete, inline project
fargen-time-edit 203 -s "2013-12-25 04:00" -e "2013-12-25 13:00" -m "I enjoyed this time. +socialize"

# Begun, in progress
fargen-time-edit 203 -s "2013-12-25 04:00"

# Complete, instantaneous
fargen-time-edit 203 -e "2013-12-25 13:00" -m "Feed the turtles."

--------------------------------

- [ ] if ID is defined...
    - [ ] if START is defined and END is defined and START is earlier than END, then instance is of duration
    - [ ] if START is defined and END is defined and START is equal to END, then instance is instantaneous
    - [ ] if START is defined and END is defined and START is later than END, then instance is invalid
    - [ ] if START is defined and END is not defined, then instance is in progress
    - [ ] if START is not defined and END is defined, then instance is instantaneous
    - [ ] if START is not defined and END is not defined, then instance is instantaneous and END is set to time of execute

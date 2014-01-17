Usage:


fargen-time-list --after "2013-12-25" --before "2013-12-27"

fargen-time-list --instantaneous

fargen-time-list --ongoing

fargen-time-list "something"

--------------------------------

- [ ] if AFTER is defined and AFTER is a valid date, then option is valid
    - search for queries with START or END after date AFTER, inclusive
- [ ] if BEFORE is defined and BEFORE is a valid date, then option is valid
    - search for queries with START or END before date BEFORE, inclusive
- [ ] if INSTANTANEOUS is True, then option is valid
    - search for queries with START date equal to None
- [ ] if ONGOING is True, then option is valid
    - search for queries with END date equal to None


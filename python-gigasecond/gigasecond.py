from datetime import timedelta

# A gigasecond is one billion (10**9) seconds.

# Program counts 10**9 sec from birthdate

# get birthday -> birthday = datetime(YYYY,MM,DD [,HH,MM,SS])
# calculate 10**9 sec in YYYY, MM, SS
# add gigasecond to birthday -> datetime(YYYY,MM,DD,HH,MM,SS) -> timedelta?
# return gigasecond date

def add_gigasecond(your_birthday):
    delta = timedelta(
        seconds=10**9
    )
    your_gigasecond = your_birthday + delta
    return your_gigasecond

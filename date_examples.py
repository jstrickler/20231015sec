from datetime import date, datetime
from dateutil.parser import parse

event1 = datetime(2023, 10, 16, 16, 29, 8)

print(f"event1: {event1}")

event2 = datetime.now()  # right now!
print(f"event2: {event2}")

elapsed = event1 - event2

print(f"elapsed: {elapsed}")

text_date = "Aug 1 2014"
d = parse(text_date)
print(f"d: {d}")


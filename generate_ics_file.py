from datetime import datetime

from ics import Calendar, Event

# Create a calendar instance
calendar = Calendar()

# List of holiday names and dates in 2025
holidays = [
    ("New Year's Day", datetime(2025, 1, 1)),
    ("Martin Luther King Day", datetime(2025, 1, 20)),
    ("Memorial Day", datetime(2025, 5, 26)),
    ("Independence Day", datetime(2025, 7, 4)),
    ("Labor Day", datetime(2025, 9, 1)),
    ("Thanksgiving Day", datetime(2025, 11, 27)),
    ("Christmas Day", datetime(2025, 12, 25)),
]

# Create an all-day event for each holiday
for holiday_name, holiday_date in holidays:
    event = Event()
    event.name = holiday_name
    event.begin = holiday_date.strftime("%Y-%m-%d")
    event.make_all_day()  # Set as an all-day event
    event.description = holiday_name
    calendar.events.add(event)

# Write to an .ics file
with open("Holidays.ics", "w") as f:
    f.write(str(calendar))

print("ICS file created as 'Holidays.ics'")

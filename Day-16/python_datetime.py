# Python provides the built-in datetime module to handle dates, times, and time intervals.

from datetime import datetime, date, time, timedelta

# 1. Getting datetime Information
# You can retrieve specific components like year, month, day, hour, minute, etc.,
# from the current datetime object.

now = datetime.now()
print("Current datetime:", now)
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Timestamp: number of seconds elapsed since January 1, 1970 (UTC)
print("Timestamp:", now.timestamp())


# 2. Formatting Date Output Using strftime
# The strftime() method converts date and time objects to strings based on format codes.

time_string = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted time:", time_string)


# 3. String to Time Using strptime
# The strptime() method creates a datetime object from a given string representation.

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Parsed date object:", date_object)


# 4. Using date from datetime
# The date class allows you to create custom dates or pull today's date info.

today = date.today()
print("Today's date:", today)
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


# 5. Time Objects to Represent Time
# The time class represents local time independent of any particular day.

default_time = time()
print("Default time:", default_time)

custom_time = time(hour=10, minute=30, second=50)
print("Custom time:", custom_time)


# 6. Difference Between Two Points in Time (timedelta)
# Subtracting two date or datetime objects returns a timedelta object representing the difference.

new_year = datetime(year=2027, month=1, day=1)
time_left_for_newyear = new_year - datetime.now()
print("Time left for New Year:", time_left_for_newyear)

# You can also define custom timedeltas to calculate future/past dates or intervals
delta = timedelta(weeks=2, days=3, hours=5)
print("Custom timedelta interval:", delta)
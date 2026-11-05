from datetime import datetime, date, time, timedelta

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module

now = datetime.now()
print("Current day:", now.day)
print("Current month:", now.month)
print("Current year:", now.year)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current timestamp:", now.timestamp())


# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S"

formatted_current_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted current date:", formatted_current_date)


# 3. Today is 5 December, 2019. Change this time string to time.

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Date string changed to datetime object:", date_object)


# 4. Calculate the time difference between now and new year.

current_time = datetime.now()
new_year = datetime(current_time.year + 1, 1, 1)
time_difference = new_year - current_time
print("Time difference between now and New Year:", time_difference)


# 5. Calculate the time difference between 1 January 1970 and now.

epoch = datetime(1970, 1, 1)
time_since_epoch = current_time - epoch
print("Time difference between 1 January 1970 and now:", time_since_epoch)


# 6. Think, what can you use the datetime module for? Examples:
# - Time series analysis
# - To get a timestamp of any activities in an application
# - Adding posts on a blog
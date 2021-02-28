import sys
from datetime import datetime
from datetime import timedelta

# Try the code below and revise it to the current time
for line in sys.stdin:

     data = line.strip().split("\t")
     if len(data) == 6:
         date, time, store, item, cost, payment = data

     print("{0}\t{1}".format(item, cost))

# 2. Add the timedelta to the datetime and subtract 60 seconds and add 2 years.

# Get current datetime
my_time = datetime.now()

# Delta
my_delta = timedelta(seconds=-60, days=365*2)

# Combine and Print
print(my_time + my_delta)

# 3. Create a timedelta object representing 100 days, 10 hours, and 13 minutes
d = timedelta(days=100, hours=10, minutes=13)
print(d)

# 4. Write a function that takes two arguments (feet and inches) with this time object

class my_datetime:

    # Class that accepts feet, inches, and returns both with a datetime object

    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        self.time = datetime.now()

    def myfunc(self):
        print(("Feet: {0}, Inches: {1}, Time Created: {2}").format(self.feet, self.inches, self.time))



new_object = my_datetime(10, 11)
print(new_object.myfunc())


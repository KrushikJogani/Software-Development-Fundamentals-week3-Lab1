# Example 1: Current time of a timezone using pytz module

import pytz
from datetime import datetime

timezone = pytz.timezone("Pacific/Auckland")  # setting the timezone
current_time = datetime.now(timezone)  # getting current time
print("Current Time:", current_time)
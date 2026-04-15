# Example 10: Parking Meter - charges $4/hr for first 3 hrs then $2/hr after

print("Kia Ora, this is a parking meter")  # welcome message

ParkTime = 4   # setting park time to 4 hours
rate1 = 4      # rate for first 3 hours
rate2 = 2      # rate after 3 hours

if ParkTime <= 3:                                       # if parked 3 hours or less
    cost = ParkTime * rate1
else:                                                   # if parked more than 3 hours
    cost = (3 * rate1) + ((ParkTime - 3) * rate2)

print(f"Parking charge for {ParkTime} hours: ${cost}")  # showing total cost
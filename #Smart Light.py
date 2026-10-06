
from datetime import datetime

on_time = "1:00 pm"
off_time = "12:30 am"

light = False

current_time = datetime.now().strftime("%I:%M %p")

print("Current time:", current_time)

if current_time == on_time:
    light = True

if current_time == off_time:
    light = False

if light:
    print("💡 LIGHT ON")
else:
    print("🌑 LIGHT OFF")

#Notes.md

##Adding to time:
Start time at zero        --> total_time = timedelta(seconds=0)
Add some time to total    --> time_total.seconds + int(some_value)

## GPX Update rules
Each point appears to vary between 2 and 3 seconds **per update**.
This means there will be a new updated set of GPS at maximum
every **3 seconds**, and a **minimum of 2**.
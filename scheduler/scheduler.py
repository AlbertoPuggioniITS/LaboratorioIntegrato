import datetime as dt
from scheduler import Scheduler
from scheduler.trigger import Monday, Tuesday

# this is the callback function
# main function to run
def foo(): 
    print("foo")

schedule = Scheduler()

# run every 10 minutes
schedule.cyclic(dt.timedelta(minutes=10), foo)

# run every minute at 15 seconds
schedule.minutely(dt.time(second=15), foo)

# run every hour at 30 minutes, 15 seconds
schedule.hourly(dt.time(minute=30, second=15), foo)

# run every day at 16:30
schedule.daily(dt.time(hour=16, minute=30), foo)

# run every monday
schedule.weekly(Monday(), foo)

# run every monday at 16:30
schedule.weekly(Monday(dt.time(hour=16, minute=30)), foo)

# run ONCE in 10 minutes
schedule.once(dt.timedelta(minutes=10), foo)

# run ONCE on Tuesday
schedule.once(Tuesday(), foo)

# run ONCE on custom date
schedule.once(dt.datetime(year=2022, month=2, day=15, minute=45), foo)
# convert to seconds given a HH-MM-SS time
#return the ammount of seconds as an integer
def time_complete_to_seconds(time_complete):
    hours   = time_complete[0]
    minutes = time_complete[1]
    seconds = time_complete[2]

    seconds = seconds + (minutes*60) + (hours * 3600)

    return seconds

#convert to hh-mm-ss format the given seconds argument
#returns a [hh, mm, ss] vector mod 60
def seconds_to_time_complete(secs):

    seconds = (secs % 60)
    minutes = (secs / 60)
    hours = (secs / 3600)
    minutes = minutes % 60

    return [hours, minutes, seconds]


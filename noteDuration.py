import random

# random time between 250-1000 milliseconds

def duration(length):

    time = 0

    # random time between 250-1000 milliseconds
    # randomDuration = random.randint(250, 1000)

    if length == 'eighth':
        time = 250
    if length == 'quarter':
        time = 500
    if length == 'half':
        time = 1000
    if length == 'whole':
        time = 2000
    if length == 'random':
        time = random.randint(250, 1000)

    return time

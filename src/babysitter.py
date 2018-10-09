import datetime

START_TIME = datetime.time(hour=17,minute=0)
STOP_TIME = datetime.time(hour=4,minute=0)

class babysitter():
    def __init__(self):
        self.startTime = START_TIME
        self.stopTime = STOP_TIME

    def getTimeSpan(self):
        return 11

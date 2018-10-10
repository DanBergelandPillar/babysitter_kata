import datetime

START_TIME = datetime.time(hour=17,minute=0)
STOP_TIME = datetime.time(hour=4,minute=0)
HOURS = ['5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm', '12pm', '1am', '2am','3am', '4am']

class Babysitter():
    def __init__(self, start = 0, end = 0):
        self.end_time_int = 0
        self.start_time_int = 0
        self.set_start_time(start)
        self.set_end_time(end)

    def set_start_time(self, start):
        if(start in HOURS):
            self.start_time_int = HOURS.index(start)
        else:
            self.start_time_int = 0
        self.validate_times()
    
    def set_end_time(self, end):
        if(end in HOURS):
            self.end_time_int = HOURS.index(end)
        else:
            self.end_time_int = 11
        self.validate_times()

    def validate_times(self):
        if(self.end_time_int < self.start_time_int):
            self.end_time_int = self.start_time_int

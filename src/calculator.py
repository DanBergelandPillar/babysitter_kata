import constants
import babysitter

class Rate():
    def __init__(self, start_int, end_int, pay_rate):
        self.start_int = start_int
        self.end_int = end_int
        self.pay_rate = pay_rate


def calculate(start_time, end_time, family):
    total_pay = 0
    sitter = babysitter.Babysitter(start_time, end_time)
    for rate in family:
        #get hours within rate
        if(sitter.start_time_int <= rate.start_int and sitter.end_time_int >= rate.end_int):
            total_pay += (rate.end_int - rate.start_int) * rate.pay_rate
        #add to total
    return total_pay


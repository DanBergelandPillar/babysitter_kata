import constants
import babysitter

def calculate(start_time, end_time, family):
    total_pay = 0
    sitter = babysitter.Babysitter(start_time, end_time)
    for rate in family:
        #get hours within rate
        if(sitter.start_time_int <= rate.start_time_int and sitter.end_time_int >= rate.end_time_int):
            total_pay += (rate.end_time_int - rate.start_time_int) * rate.pay_rate
        #add to total
    return total_pay


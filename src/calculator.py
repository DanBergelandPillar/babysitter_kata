import constants
import babysitter

def calculate(start_time, end_time, family):
    total_pay = 0
    sitter = babysitter.Babysitter(start_time, end_time)
    for rate in family:
        hours = babysitter.unionHoursOfRateAndSitterTime(sitter, rate)
        total_pay += rate.pay_rate * hours
    return total_pay

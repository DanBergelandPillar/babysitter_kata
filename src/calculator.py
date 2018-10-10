import constants
import babysitter

def unionHoursOfRateAndSitterTime(sitter, rate):
    overlap_start = 0
    overlap_end = babysitter.HOURS.index('4am')
    #find start time in range, break out if no overlap
    if(sitter.start_time_int <= rate.start_time_int):
        overlap_start = rate.start_time_int
    elif(sitter.start_time_int < rate.end_time_int):
        overlap_start = sitter.start_time_int
    else:
        return 0
    #find stop time in range, break out if no overlap
    if(sitter.end_time_int >= rate.end_time_int):
        overlap_end = rate.end_time_int
    elif(sitter.end_time_int > rate.start_time_int):
        overlap_end = sitter.end_time_int
    else:
        return 0
    return overlap_end - overlap_start

def calculate(start_time, end_time, family):
    total_pay = 0
    sitter = babysitter.Babysitter(start_time, end_time)
    for rate in family:
        hours = unionHoursOfRateAndSitterTime(sitter, rate)
        total_pay += rate.pay_rate * hours
    return total_pay


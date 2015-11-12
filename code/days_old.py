# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def leapYear(year):
    if year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def daysByMonth(month1, day1, month2, day2, is_leap):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    daysOfMonthsLeap = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ['ene','feb','mar','apr','may','jun','jul','ago','sep','oct','nov','dic']
    if month1 == month2:
        return day2 - day1
    else:
        sumDays = day2
        month = month2 - 1
        while month >= month1:
            if is_leap:
                sumDays = sumDays + daysOfMonthsLeap[month - 1]
            else:
                sumDays = sumDays + daysOfMonths[month - 1]
            month = month - 1
        sumDays = sumDays - day1
        return sumDays   



def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    if year1 == year2:
        is_leap = leapYear(year2)
        return daysByMonth(month1, day1, month2, day2, is_leap)
    else:
        is_leap = leapYear(year2)
        sumDays = daysByMonth(1,1,month2,day2,is_leap)
        year = year2 - 1
        while year >= year1:
            is_leap = leapYear(year)
            sumDays = sumDays + 366 if is_leap else sumDays + 365
            year = year - 1
        is_leap = leapYear(year1)
        sumDays = sumDays - daysByMonth(1,1,month1,day1,is_leap)
        return sumDays


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()


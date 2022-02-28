#Pay Challenge - USED BOOK AND SOLUTION HAD A HARD TIME WITH THIS WILL REDO AT A LATER DATE.
#Nick Fernandes

#Constants
fOVER_TIME_HOURS = 40.0
f_DOUBLE_TIME_HOURS = 60.00

#inputs
fHours = float(input("How many hours did you work this week?: "))
fHourly = float(input("What is your hourly rate?: "))

fHalfTimeHours= 0.00
fDoubleTimeHours = 0.00

# determine OT and DT
#check for <40 hours
if fHours > fOVER_TIME_HOURS:

    #check for dt hours
    if fHours > f_DOUBLE_TIME_HOURS:
        fDoubleTimeHours = fHours - f_DOUBLE_TIME_HOURS
        fHours = fHours - fDoubleTimeHours

    #check time and half hours
    if fHours > fHalfTimeHours:
        fHalfTimeHours - fOVER_TIME_HOURS
        fHours -= fHalfTimeHours

#Calculate
fRegularPay = fHours * fHourly
fHalfTimePay = fHalfTimeHours * (1.5 * fHourly)
fDoubleTimePay = fDoubleTimeHours * (2 * fHourly)
fTotalPay = fRegularPay + fDoubleTimePay + fHalfTimePay

#Output

print("Regular Pay is: $", format(fRegularPay, '.2f'))
print("Time and Half Pay is: $", format(fHalfTimePay, '.2f'))
print("Double Time Pay is: $", format(fDoubleTimePay, '.2f'))
print("Total Pay is: $", format(fTotalPay, '.2f'))
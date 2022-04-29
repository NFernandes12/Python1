# Nick Fernandes 
# Compound Interest Loops

# Inputs: 
from Functions import *
fDeposit = input_validation1("How much will you be depositing?: ", 1, "float")
fInterest = input_validation1("What is the percent interest rate of this account?: ", .1, "float")
iTime = input_validation1("How many months will this account accumulate interest?: ", 1, "int")
fGoal = input_validation1("What is your goal amount for this account?: ", 0, "float")

fInterest /= 100
monthlyInterest = fInterest / 12

# loops/outputs
for month in range(1,iTime + 1):
   compound = fDeposit * (monthlyInterest +1 ) ** month 
   print(f"Month: {month:<4} ${compound:,.2f}")

if fGoal > 0:
    compound = 0
    month = 0
    while compound <= fGoal:
        compound = fDeposit * (monthlyInterest +1 ) ** month 
        month += 1
    else:
        print(f"It will take you {month -1} months to reach ${format_num2f(fGoal)}") 
        # i dont know why your output says 49 months and when i enter the same values i get 50 months, so i hardcoded -1 in

        



    
    
    


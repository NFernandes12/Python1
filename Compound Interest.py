# Compound Interest
# Nick Fernandes

# nFutureValue = money in account after years
# fStartingValue = original amount
# fInterest = interest rate
# fPerYearComp = number of times per year its compounded
# fYears = number of years

# Inputs

fStartingValue = float(input("Enter the starting principal: "))
fInterest = float(input("Enter the annual interest rate: "))
fCompound = float(input("How many times per year is the interest compounded? "))
iYears = int(input("How long will this account earn interest? "))
#fYears = float(input("How long will this account earn interest? "))

# Conversion/Calculations

fInterest /= 100
nFutureValue = fStartingValue * ((fInterest / fCompound)+1) ** (fCompound * iYears)

# Output and format

print("At the end of", (iYears), "years you will have $", format(nFutureValue, ",.2f"))
#print("At the end of", (fYears), "years you will have $", format(nFutureValue, ",.2f"))


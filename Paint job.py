# Nick Fernandes
#Paint Job Calculator 

from Functions import *
# fSquareFt = input_validation("What is the square footage of the area?: ", 1 , "float")
# fPaintPrice = input_validation("What is the cost of paint per gallon?: ", 1 , "float")
# fFtPerGal = input_validation("How much feet do you get per gallon of paint?: ", 1 , "float")
# fHoursPerGal = input_validation("How many labor hours per gallon?: ", 1 , "float")
# fLaborCosts = input_validation("How much does the labor cost per hour?: ", 1 , "float")
# sState = input("In which state is this job being performed?: ")
# sLastName = input("What is the last name for this order?: ")
fPaintPrice = 26.75
fHoursPerGal = 8
fLaborCosts = 35
fSquareFt = 550
fFtPerGal = 112
totalGal = getGallonsOfPaint(fSquareFt,fFtPerGal)
print(totalGal)

totalLaborHours = getLaborHours(fHoursPerGal,totalGal)
print(totalLaborHours)

totalLaborCost = getLaborCost(fLaborCosts,totalLaborHours)
print(totalLaborCost)

totalPaintCost = getPaintCost(totalGal,fPaintPrice)
print(totalPaintCost)

# Every 112 sq ft = 1 gal. paint + 8 hrs labor
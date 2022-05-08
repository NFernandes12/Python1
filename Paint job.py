# Nick Fernandes
#Paint Job Estimator
from Functions import *

def main():
    fSquareFt = input_validation("What is the square footage of the area?: ", 1 , "float")
    fPaintPrice = input_validation("What is the cost of paint per gallon?: ", 1 , "float")
    fFtPerGal = input_validation("How much feet do you get per gallon of paint?: ", 1 , "float")
    fHoursPerGal = input_validation("How many labor hours per gallon?: ", 1 , "float")
    fLaborCosts = input_validation("How much does the labor cost per hour?: ", 1 , "float")
    sState = input("In which state is this job being performed?: ").lower()
    sLastName = input("What is the last name for this order?: ")
    totalCost = 0

    totalGal = getGallonsOfPaint(fSquareFt,fFtPerGal)
    totalLaborHours = getLaborHours(fHoursPerGal,totalGal)
    totalLaborCost = getLaborCost(fLaborCosts,totalLaborHours)
    totalPaintCost = getPaintCost(totalGal,fPaintPrice)
    fTax = getSalesTax(sState)
    
    print(f"{showCostEstimate(totalGal,totalLaborHours,totalPaintCost,totalLaborCost,fTax,totalCost,sLastName)}")

main()









    # fPaintPrice = 26.75
    # fHoursPerGal = 8
    # fLaborCosts = 35
    # fSquareFt = 550
    # fFtPerGal = 112
    # totalCost = 0
    # sState = "ri".lower()
    # sLastName = "Candido"
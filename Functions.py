# Nick Fernandes
# Most of my functions compiled. 
import math

def format_num2f(num):
    newNum = format(num,',.2f')
    return newNum

# def format_dollar():
#     return '${:,.2f}'


def input_validation(prompt,min,datatype):
    amount = min -1
    while amount < min:
        try:
            if datatype == "float":
                amount = float(input(prompt))
            else: 
                amount = int(input(prompt))
            if amount < min:    
                print(f"Please enter a number greater or equal to {min}")
        except ValueError:
            print("Please only enter numerical data!")
    return amount 


def getGallonsOfPaint(fFtPerGal,fSquareFt):
   gallons = fFtPerGal / fSquareFt
   return math.ceil(gallons)

def getLaborHours(LaborHoursPerGal,totalGallons):
  totalLaborHours = LaborHoursPerGal * totalGallons
  return float(totalLaborHours)

def getLaborCost(laborCost,laborHours):
    totalLaborCost = laborCost * laborHours 
    return float(totalLaborCost)

def getPaintCost(totalGal,paintPrice):
    totalPaintCost = totalGal * paintPrice
    return float(totalPaintCost)


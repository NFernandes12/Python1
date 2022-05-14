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

def getSalesTax(sState):
    if sState == "ct" or "connecticut" :
       fTax = .06
    elif sState == "ma" or "massachusetts":
        fTax = .0625
    elif sState == "me" or "maine":
        fTax = .085
    elif sState == "nh" or "new hampshire":
        fTax = 0
    elif sState == "ri" or "rhode island":
        fTax = .07
    elif sState == "vt" or "vermont":
        fTax = .06
    else:
        fTax = 0
    return fTax
    
def showCostEstimate(totalGal,totalLaborHours,totalPaintCost,totalLaborCost,fTax,totalCost,sLastName):
    taxAdd = (totalLaborCost + totalPaintCost) * fTax
    totalCost = totalLaborCost + totalPaintCost + taxAdd
    print(f"Gallons of paint: {totalGal}\nHours of labor: {totalLaborHours}\nPaint Charges: ${totalPaintCost:,.2f}\
        \nLabor Charges: ${totalLaborCost:,.2f}\nTax: ${taxAdd:,.2f}\nTotal Cost: ${totalCost:,.2f}\
        \nFile: {sLastName}_PaintJobOutput.txt was created.") 
        
    outfile = open(f"{sLastName}_PaintJobOutput.txt", 'w')
    outfile.write(f"Gallons of paint: {totalGal}\nHours of labor: {totalLaborHours}\nPaint Charges: ${totalPaintCost:,.2f}\
        \nLabor Charges: ${totalLaborCost:,.2f}\nTax: ${taxAdd:,.2f}\nTotal Cost: ${totalCost:,.2f}")
    outfile.close


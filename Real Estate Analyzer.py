# Real Estate Analyzer
# Nick Fernandes
from FunctionsList import *
#main program 
def main():
    lstSalePrice = []
    
    fSalesPrice = input_validation("Enter property sales value: ",1,"float")
    lstSalePrice.append(fSalesPrice)
    
    #loop for list values
    while True:
            sResponse = input("Enter another value? Y or N: ").lower() 
            if sResponse == "y":
                fSalesPrice = input_validation("Enter property sales value: ",1,"float")
                lstSalePrice.append(fSalesPrice)
            elif sResponse == "n":
                break
            else:
                print("That is not a Y or N")
        
    lstSalePrice.sort()
    propertyNumber = 1
    
    #loop for displaying property's
    for value in lstSalePrice:
        print(f"Property {propertyNumber}: ${value:,.2f}")
        propertyNumber += 1

    #declaration for list values/math
    minValue = lstSalePrice[0]
    maxValue = lstSalePrice[-1]
    totalValue = sum(lstSalePrice)
    avgValue = totalValue / len(lstSalePrice)
    commValue = totalValue * .03 
    
    #output
    print(f"Minimum: ${minValue:,.2f}\nMaximum: ${maxValue:,.2f}\nTotal: ${totalValue:,.2f}\
        \nAverage: ${avgValue:,.2f}\nMedian: ${getMedian(lstSalePrice):,.2f}\nCommisson: ${commValue:,.2f}\n")
main()
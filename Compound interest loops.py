# Nick Fernandes 
# Compound Interest Loops

# Inputs: 

fDeposit = float(input("How much will you be depositing?: "))
fInterest = float(input("What is the interest rate this account has?: "))

while True:
    try:
        fTime = int(input("How many months will this account accumulate interest?: "))
    except ValueError:
            print("Please keep it to whole numbers!")
            continue
    else:
        break
# Nick Fernandes
# Most of my functions compiled. 

def format_num2f(num):
    newNum = format(num,',.2f')
    return newNum

# def format_dollar():
#     return '${:,.2f}'


def input_validation1(prompt,min,datatype):
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

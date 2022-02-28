# Moose County Fair
# Nick Fernandes

# Inputs
sName = input("What is your name?: ")
iAge = int(input("How old are you?: "))

# If else
if iAge <= 5:
    sFinding = "$0"
elif 6 <= iAge <= 12:
    sFinding = "$4.00"
elif 13 <= iAge <= 18:
    sFinding = "$5.00"
elif 19 <= iAge <= 22:
    sFinding = "$6.00"
elif 23 <= iAge <= 64:
    sFinding = "$8.50"
else:
    sFinding = "$6.00"

# Output

print(sName + ", It will cost", sFinding, "to enter the fair.")

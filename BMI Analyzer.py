""" CANDIDO'S FEEDBACK

Consider rewritting your code as follows that works and requires less typing and is more EFFICIENT and you output only once with ONE print() function

if fBMI <= 18.50:
    sFinding = "Underweight"
elif fBMI <= 24.90:
    sFinding = "Normal"
elif fBMI <= 29.90:
    sFinding = "Overweight"
else:
    sFinding = "Obese"

# Print out the sFinding only ONCE:

print(sName, ", your calculated BMI is ", format(fBMI, ',.2f'), "Find is:", sFinding)

Since the conversion factors are always the SAME make them constants:

Remember named constants need to be in ALL UPPERCASE. Such as fMETERS_CONVERSION = 39.36"""

#Nick Fernandes
#BMI Analyzer

#Inputs / Outputs & Loops - Getting information from the user

import time
print("Hello! I'm Nick and we will be analyzing your BMI.")
time.sleep(1)

sName = input("First things first, what is your name?: ")
print("Nice to meet you", sName + ", let's figure out your BMI.  ")
time.sleep(1)

while True:
    try:
        iHeight = int(input("In inches, how tall are you?: "))
    except ValueError:
        print("Please enter a whole number! ")
        continue
    else:
        break

print("Great! Now how much do you weigh? Don't worry I won't tell anyone!")
time.sleep(2)

while True:
    try:
        iWeight = int(input("Enter your weight in LBS: "))
    except ValueError:
        print("Please enter a whole number! ")
        continue
    else:
        break

#Conversions/Calculations

fMeterHeight = iHeight / 39.36
fKiloWeight = iWeight / 2.2
fBMI = fKiloWeight / (fMeterHeight ** 2)

#Final Outputs

if (fBMI <= 18.5):
    print(sName + ", your BMI is", format(fBMI, ".2f") + ". Try to eat more throughout the day you are underweight.")

elif (fBMI >= 18.51 and fBMI <= 24.9):
    print(sName + ", your BMI is", format(fBMI, ".2f") + ". This is normal, keep doing what you are doing!")

elif (fBMI >= 24.91 and fBMI <= 29.9):
    print(sName + ", your BMI is", format(fBMI, ".2f") + ". Try to watch what you eat you are overweight.")

else:
    print(sName + ", your BMI is", format(fBMI, ".2f") + ". You should consult your doctor you are obese.")








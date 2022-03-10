# Grade Analyzer 
# Nick Fernandes 

# Inputs & a loop because why not :)

import time

title = """

██████  ██████   ██████  ███████         ██████         ██████   ██████   ██████ ██   ██ ███████ ██ 
██   ██ ██   ██ ██    ██ ██             ██              ██   ██ ██    ██ ██      ██  ██  ██      ██ 
██████  ██████  ██    ██ █████          ██              ██████  ██    ██ ██      █████   ███████ ██ 
██      ██   ██ ██    ██ ██             ██              ██   ██ ██    ██ ██      ██  ██       ██    
██      ██   ██  ██████  ██      ██      ██████         ██   ██  ██████   ██████ ██   ██ ███████ ██ 
                                                                                                     """
print(title)

sName = input("What is your name?: ") 
print("I will now need to collect 4 test scores from you,", sName)

time.sleep(1)

while True:
    try:
        iScore1 = int(input("Enter the first test score: "))
        iScore2 = int(input("Enter the second test score: "))
        iScore3 = int(input("Enter the third test score:  "))
        iScore4 = int(input("Enter the fourth test score: "))
    except ValueError:
        print("Please enter whole numbers only!")
        continue    
    if iScore1 < 0 or iScore2 < 0 or iScore3 < 0 or iScore4 < 0:
        print("Scores must be greater than zero!")
        time.sleep(1)
        raise SystemExit
    else:
        break

# Score dropping and Averaging 

fAverage = 0

sDropResult = input("Would you like to drop the lowest score Y or N?: ").lower()

if sDropResult != "y" and sDropResult != "n":
    print("Only Y/N are accepted inputs!")  
    time.sleep(1)
    raise SystemExit

if sDropResult == "y":
    testAmount = 3
    
    if iScore1 < iScore2 and iScore1 < iScore3 and iScore1 < iScore4:
        lowScore = iScore1
        
    elif iScore2 < iScore3 and iScore2 < iScore4:
        lowScore = iScore2
        
    elif iScore3 < iScore4:
        lowScore = iScore3
    
    else:
        lowScore = iScore4
        
    fAverage = ((iScore1 + iScore2 + iScore3 + iScore4) - lowScore) / 3

if sDropResult == "n":
    testAmount = 4
    
    fAverage = (iScore1 + iScore2 + iScore3 + iScore4) / 4
  
# Grade assaignments

sLetterGrade = ""    

if fAverage >= 97.0:
    sLetterGrade = "A+"
elif fAverage >= 94.0 and fAverage <= 96.9:
    sLetterGrade = "A"
elif fAverage >= 90.0 and fAverage <= 93.9:
    sLetterGrade = "A-"
elif fAverage >= 87.0 and fAverage <= 89.9:
    sLetterGrade = "B+"
elif fAverage >= 84.0 and fAverage <= 86.9:
    sLetterGrade = "B"
elif fAverage >= 80.0 and fAverage <= 83.9:
    sLetterGrade = "B-"
elif fAverage >= 77.0 and fAverage <= 79.9:
    sLetterGrade = "C+"
elif fAverage >= 74.0 and fAverage <= 76.9:
    sLetterGrade = "C"
elif fAverage >= 70.0 and fAverage <= 73.9:
    sLetterGrade = "C-"
elif fAverage >= 67.0 and fAverage <= 69.9:
    sLetterGrade = "D+"
elif fAverage >= 64.0 and fAverage <= 66.9:
    sLetterGrade = "D"
elif fAverage >= 60.0 and fAverage <= 63.9:
    sLetterGrade = "D-"
else:
    sLetterGrade = "F"

# Output     

print(f"{sName}, your {testAmount} test average is {format(fAverage, '.1f')} with a letter grade of {sLetterGrade}")   
         

#Certification Exam
#Nick Fernandes

""" Original attempt, not efficent. 
iScore = int(input("Enter your test score: "))

if iScore == 100:
    sResault = "Perfect Score!"
elif iScore >= 90:
    sResault = "Pass"
elif iScore < 90:
    sResault = "Retake Exam"

print(sResault)"""

#Revison

iScore = int(input("Enter test score: "))

if iScore >= 90:
    print("Pass")
    if iScore == 100:
        print("Perfect Score!")
else:
    print("Retake Exam")




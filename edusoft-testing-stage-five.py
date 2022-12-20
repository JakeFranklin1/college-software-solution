import operator
import random
import csv
import fileinput
from datetime import date, datetime
operatorDict = {"+":operator.add,
                "-":operator.sub,
                "*":operator.mul,
                "/":operator.floordiv}

def main():
    num1 = 0
    studentPath = '/Users/jake/College/college-software-solution/student.csv'
    resultPath = '/Users/jake/College/college-software-solution/result.csv'
    login = input("Enter your login: ")
    with open(studentPath, 'r') as studentData:
        csv_reader = csv.DictReader(studentData)
        for row in csv_reader:
            if login in row["LoginName"]:
                print(row)
                bestResult = int(row["BestResult"])
                name = (''.join([row['FirstName'] + ' ' + row['LastName']]))
                print("Welcome", name)
            # level = int(row["Level"])
                if int(row["Level"]) == 1:
                    level = 1
                    num2 = 10
                elif int(row["Level"]) == 2:
                    level = 2
                    num2 = 100
                elif int(row["Level"]) == 3:
                    level = 3
                    num1 = -100
                    num2 = 100
    with open(resultPath, 'r') as resultData:
        csv_reader = csv.DictReader(resultData)
        for row in csv_reader:
            if login == row['UserName']:
                lastResult = row['PreviousResult']
    print("Your last result was:",lastResult,"\nAnd your best result was:", bestResult)
    userChoice = input("\nWould you like to move to the test? (y/n): ").upper()
    if userChoice == "Y": 
        mathsTest(login = login,level = level,num1 = num1,num2 = num2,bestResult = bestResult)
    elif userChoice == "N":
        quit()
            
# login,level,num1,num2,bestResult
def mathsTest(**student):
    print(student)
    print("Level of test:",student["level"],"\n")
    question = 0
    correctAnswer = 0
    wrongAnswer = 0
    while question != 10:
        question += 1
        operator = random.choice(["-", "+", "*", "/"])
        a = random.randrange(student["num1"],student["num2"],1)
        b = random.randrange(student["num1"],student["num2"],1)
        if b == 0 and operator == "/":
            operatorNoDiv = random.choice(["+", "-", "*"])
            result = operatorDict[operatorNoDiv](a, b)
            while result < 0 and student['level'] != 3:
                a = random.randrange(student["num1"],student["num2"], 1)
                b = random.randrange(student["num1"],student["num2"], 1)
                print("Generating new numbers:", a, operatorNoDiv, b) # Testing
                result = operatorDict[operatorNoDiv](a, b)
            print("Question number: %d" % question)
            print(a, operatorNoDiv, b)
            print("Answer =",result) # testing
            answer = int(input("\nPlease Answer the Question: "))
        else:
            result = operatorDict[operator](a, b)
            while result < 0 and student["level"] != 3:
                a = random.randrange(student["num1"],student["num2"], 1)
                b = random.randrange(student["num1"],student["num2"], 1)
                print("Generating new numbers:", a, operator, b) # Testing
                result = operatorDict[operator](a, b)
            print("Question number: %d" % question)
            print(a, operator, b)
            print("Answer =",result) # Testing
            answer = int(input("\nPlease Answer the Question: "))
        if answer == result:
            print("\nCorrect! The answer was", result,"\n")
            correctAnswer += 1
        elif answer != result:
            print("\nWrong! The answer was", result,"\n")
            wrongAnswer += 1
    if question == 10:
        print("Your correct answers were:",correctAnswer, "and you got",wrongAnswer,"incorrect")
        storeResults(student['login'], wrongAnswer, student['bestResult'])
    
def storeResults(login, wrongAnswer, bestResult):
    result = 10 - wrongAnswer
    currentDate = date.today()
    time = datetime.now()
    studentRecords = open('/Users/jake/College/college-software-solution/result.csv', 'a')
    line = ("\n" + login + "," + str(result) + "," + 
            currentDate.strftime("%d-%m-%Y") + "," + 
            time.strftime("%H:%M:%S"))
    print("Details added to database:",
        login + " " + str(result) + " " + 
        currentDate.strftime("%d-%m-%Y") + " " + 
        time.strftime("%H:%M:%S"))
    studentRecords.write(line)
    studentRecords.close()
    if result > bestResult:
        updateBestResult(login, result)
    else:
        print("\nUnfortunately, you didn't get a new personal best.")

def updateBestResult(login, result):
    with fileinput.input(files=('/Users/jake/College/college-software-solution/student.csv'), inplace=True, mode='r') as studentFile:
        reader = csv.DictReader(studentFile)
        print(",".join(reader.fieldnames))  # print back the headers
        for row in reader:
            best = int(row["BestResult"])
            if row["LoginName"] == login and result > best:
                row["BestResult"] = str(result)
            print(",".join([row["LoginName"], row["FirstName"], row["LastName"], row["Level"], row["Code"], row["BestResult"]]))
    studentFile.close()
    print("\nNew personal best! Your result has been updated.")
    
main()
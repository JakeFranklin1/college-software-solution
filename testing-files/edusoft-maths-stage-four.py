import operator
import random
import csv
from datetime import date, datetime
operatorDict = {"+":operator.add,
                "-":operator.sub,
                "*":operator.mul,
                "/":operator.floordiv}

def main():
    studentList = []
    filepath = 'student.csv'
    File = open(filepath)
    Reader = csv.reader(File)
    Data = list(Reader)
    login = input("Enter your login: ")
    for x in list(range(0, len(Data))):
        if login == Data[x][0]:
            print("\nUser Found:",Data[x][1], Data[x][2])
            studentList.append(Data[x])
            level = int(Data[x][3])
            num1 = 0
            if level == 1:
                num2 = 10
            elif level == 2:
                num2 = 100
            elif level == 3:
                num1 = -100
                num2 = 100
    studentResults = []
    resultPath = 'result.csv'
    resultFile = open(resultPath)
    resultReader = csv.reader(resultFile)
    resultData = list(resultReader)
    for row in list(range(0, len(resultData))):
        if login == resultData[row][0]:
            studentResults.append(int(resultData[row][1]))
            lastResult = resultData[row][1]
    print("Your last result was:",lastResult,"\nAnd your best result was:", max(studentResults))
    userChoice = input("\nWould you like to move to the test? (y/n): ").upper()
    if userChoice == "Y": 
        mathsTest(login,level,num1,num2)
    elif userChoice == "N":
        quit()
            

def mathsTest(login,level,num1,num2):
    print("Level of test:",level,"\n")
    question = 0
    correctAnswer = 0
    wrongAnswer = 0
    while question != 10:
        question += 1
        operator = random.choice(["-", "+", "*", "/"])
        a = random.randrange(num1,num2,1)
        b = random.randrange(num1,num2,1)
        if b == 0 and operator == "/":
            operatorNoDiv = random.choice(["+", "-", "*"])
            result = operatorDict[operatorNoDiv](a, b)
            while result < 0 and level != 3:
                a = random.randrange(num1, num2, 1)
                b = random.randrange(num1, num2, 1)
                print("Generating new numbers:", a, operatorNoDiv, b) # Testing
                result = operatorDict[operatorNoDiv](a, b)
            print("Question number: %d" % question)
            print(a, operatorNoDiv, b)
            print("Answer =",result) # testing
            answer = int(input("\nPlease Answer the Question: "))
        else:
            result = operatorDict[operator](a, b)
            while result < 0 and level != 3:
                a = random.randrange(num1, num2, 1)
                b = random.randrange(num1, num2, 1)
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
        updateScore(login, wrongAnswer)
    
def updateScore(login, wrongAnswer):
    result = 10 - wrongAnswer
    # studentList = []
    bestScore = open("student.csv","a")
    Reader = csv.reader(bestScore)
    Data = list(Reader)
    for x in list(range(0, len(Data))):
        if login == Data[x][0]:
            print(Data[x][5])
    currentDate = date.today()
    time = datetime.now()
    studentRecords = open('result.csv', 'a')
    line = ("\n" + login + "," + str(result) + "," + 
            currentDate.strftime("%d-%m-%Y") + "," + 
            time.strftime("%H:%M:%S"))
    print("Details added to database:",login + " " + str(result) + " " + 
        currentDate.strftime("%d-%m-%Y") + " " + 
        time.strftime("%H:%M:%S"))
    studentRecords.write(line)
    studentRecords.close()

main()
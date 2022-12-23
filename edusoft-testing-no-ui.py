import operator
import random
import csv
import fileinput
from datetime import date, datetime
from time import time

operatorDict = {"+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.floordiv}


def main():
    teacherOrStudent = input("Are you a teacher or a student? ").lower()
    teacherValidate() if teacherOrStudent == 'teacher' else student()


def student():

    num1 = 0
    studentPath = 'student.csv'
    resultPath = 'result.csv'
    login = input("Enter your student login: ")
    with open(studentPath, 'r') as studentData:
        csv_reader = csv.DictReader(studentData)
        for row in csv_reader:
            if login == row["UserName"]:
                print(row)  # testing
                bestResult = int(row["BestResult"])
                name = (''.join([row['FirstName'] + ' ' + row['LastName']]))
                print("Welcome", name)

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
                pass
        if bestResult == 0:
            print("It's your first time playing! Good luck.")
        else:
            print("Your last result was:", row['PreviousResult'],
                  "\nAnd your best result was:", bestResult)

    userChoice = input("\nWould you like to move to the test? (y/n): ").upper()

    if userChoice != "Y":
        quit()
    mathsTest(login=login, level=level, num1=num1,
              num2=num2, bestResult=bestResult)


def mathsTest(**student):

    print("Level of test:", student["level"], "\n")
    question = 0
    wrongAnswer = 0
    dupeCount = 0
    prevQuestions = []
    while question != 10:

        question += 1
        startTime = time()
        print("Question number: %d" % question)

        a, operator, b, result = calculate(
            student, operatorDict)

        currentQuestion = (str(a) + ' ' + str(operator) + ' ' + str(b))
        while currentQuestion in prevQuestions:
            print('dupe detected', a, operator, b)
            dupeCount += 1
            a, operator, b, result = calculate(
                student, operatorDict)
            currentQuestion = (str(a) + ' ' + str(operator) + ' ' + str(b))

        print(f"Question = {a} {operator} {b}")
        print(f"Answer = {result}")  # testing

        try:
            answer = int(input("\nPlease Answer the Question: "))
            # answer = result # testing
        except:
            answer = None
            print("Incorrect input, please only use numbers")
        elapsedTime = time() - startTime
        if answer == result:
            print(
                f"\nCorrect! the answer was {result} and it took you {elapsedTime:.2f} seconds.\n")
        elif answer != result:
            print("\nWrong! The answer was", result, "\n")
            wrongAnswer += 1
        store = (str(a) + ' ' + str(operator) + ' ' + str(b))
        prevQuestions.append(store)
        print(prevQuestions)

    if question == 10:
        print("Your correct answers were:", (10 - wrongAnswer),
              "and you got", wrongAnswer, "incorrect")
        storeResults(student['login'], wrongAnswer, student['bestResult'])
    print("dupe questions avoided:", dupeCount)


def calculate(student, operatorDict):
    try:
        operator = random.choice(["/", "+", "-", "*"])
        a = random.randrange(student["num1"], student["num2"], 1)
        b = random.randrange(student["num1"], student["num2"], 1)
        result = operatorDict[operator](a, b)
        if student["level"] != 3:
            while result < 0 or b > a and operator == "/":
                # print("inside first while: ", a, operator, b, result)
                operator = random.choice(["/", "+", "-", "*"])
                a = random.randrange(student["num1"], student["num2"], 1)
                b = random.randrange(student["num1"], student["num2"], 1)
                # print("Generating new numbers:", a, operator, b)  # Testing
                result = operatorDict[operator](a, b)
    except ZeroDivisionError:
        print("Zero division inside calculate function ",
              a, operator, b)  # testing
        a = random.randrange(student["num1"], student["num2"], 1)
        b = random.randrange(student["num1"], student["num2"], 1)
        operatorNoDiv = random.choice(["+", "-", "*"])
        result = operatorDict[operatorNoDiv](a, b)
        while student["level"] != 3 and result < 0:
            # print("Validating inside if statement", a, operator,b) # testing
            operatorNoDiv = random.choice(["+", "-", "*"])
            a = random.randrange(student["num1"], student["num2"], 1)
            b = random.randrange(student["num1"], student["num2"], 1)
            result = operatorDict[operatorNoDiv](a, b)
        return a, operatorNoDiv, b, result
    return a, operator, b, result


def storeResults(login, wrongAnswer, bestResult):
    result = 10 - wrongAnswer
    currentDate = date.today()
    time = datetime.now()
    studentRecords = open(
        'result.csv', 'a')

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
    elif result == int(bestResult):
        print("Tied personal best!")
    else:
        print("\nUnfortunately, you didn't get a new personal best.")


def updateBestResult(login, result):
    editFiles("UserName", login, "BestResult", result)
    print("New Personal best! Congratulations, your file has been updated.")


def teacherValidate():
    path = "teacherDetails.csv"
    login = input("Please enter your username: ")
    password = input("Please enter your password: ")
    with open(path, 'r') as data:
        csv_reader = csv.DictReader(data)
        for row in csv_reader:
            if login == row["User"] and password == row["Password"]:
                print(row)  # testing
                name = (''.join([row['First'] + ' ' + row['Last']]))
                print("Welcome", name)
            else:
                print("Incorrect username or password, please try again.")
                teacherValidate()  # testing, will replace
    data.close()
    teacher()


def teacher():
    print("Teacher Menu \n"
          "1. Add a student\n"
          "2. Delete a student\n"
          "3. Check a student's progress\n"
          "4. Change a student's course code\n"
          "5. Quit the program")
    menu = input("Please choose from the menu above. ")
    if menu == '1':
        teacherAdd()
    elif menu == '2':
        teacherDel()
    elif menu == '3':
        checkProgress()
    elif menu == '4':
        changeCode()
    elif menu == '5':
        quit()
    else:
        print("Error")
        teacher()


def teacherAdd():
    newData = open(
        'student.csv', 'a')
    UserName = str(input("Enter the students username: "))
    FirstName = str(input("Enter the students first name: "))
    LastName = str(input("Enter the students last name: "))
    Level = str(input("Enter the students level: "))
    Code = str(input("Enter the students course code: "))
    BestResult = "0"
    line = ("\n" + UserName + "," + FirstName + "," + LastName +
            "," + Level + "," + Code + "," + BestResult)
    newData.write(line)
    newData.close()
    teacherReturn()


def teacherDel():
    updatedlist = []
    with open("student.csv", newline="") as f:
        reader = csv.reader(f)
        username = input(
            "Enter the username of the user you wish to remove from file: ")
        for row in reader:
            if row[0] != username:
                updatedlist.append(row)
        print(updatedlist)
    with open("student.csv", "w", newline="") as f:
        Writer = csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")
        f.close()
        teacherReturn()


def checkProgress():
    storePrevResults = []
    count = 0
    studentName = input("Enter the name of the student you wish to check: ")
    with open('result.csv', 'r') as studentProgress:
        csv_reader = csv.DictReader(studentProgress)
        for row in csv_reader:
            if studentName in row["UserName"]:
                count += 1
                previousResults = row["PreviousResult"]
                storePrevResults.append(int(previousResults))
        total = sum(storePrevResults)
        averageScore = total / count
        bestResult = max(storePrevResults)
        print(
            f"The average score of {studentName} is {averageScore:.2f}, their previous result was {previousResults} and this students best score so far was {bestResult}.")
        teacherReturn()


def changeCode():
    moveStudent = input(
        "Enter the name of the student you wish to move to a different course: ")
    updateCode = input("Enter the new course code: ")
    editFiles("FirstName", moveStudent, "Code", updateCode)
    teacherReturn()


def editFiles(storedUser, login, old, new):
    with fileinput.input(files=('student.csv'),
                         inplace=True, mode='r') as studentFile:
        reader = csv.DictReader(studentFile)
        print(",".join(reader.fieldnames))  # print back the headers
        for row in reader:
            if row[storedUser] == login:
                row[old] = str(new)
            print(",".join([row["UserName"], row["FirstName"],
                  row["LastName"], row["Level"], row["Code"], row["BestResult"]]))
    studentFile.close()
    print("updated")  # testing


def teacherReturn():
    returnToMenu = input(
        "Would you like to return to the teacher menu? (Y/N): ").upper()
    if returnToMenu == "Y":
        teacher()
    elif returnToMenu == "N":
        quit()
    else:
        print("Input error, try again.")


main()

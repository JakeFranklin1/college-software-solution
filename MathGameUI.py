from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import csv
import fileinput
from datetime import date, datetime
from time import time
import operator

operatorDict = {"+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.floordiv}
studentPath = '/Users/jake/College/college-software-solution/student.csv'
resultPath = '/Users/jake/College/college-software-solution/result.csv'
question = 0

num1 = 0

# Designing window for registration


def studentLogin():
    global register_screen
    global username
    global password
    global username_entry
    global password_entry

    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_label = Label(register_screen, text="Username")
    username_label.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Login", width=10,
           height=1, command=mathGameUI).pack()


# Designing window for login

def teacherLogin():
    global login_screen
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry

    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10,
           height=1, command=login_verify).pack()


def login_verify():
    username1 = "jp66"
    password1 = "1234"
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    if username1 == "jp66" and password1 == "1234":
        login_success()


def login_success():
    global login_success_screen
    global tab1, tab2, tab3, tab4, tab5
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("680x500")
    Label(login_success_screen, text="Login Success").pack()

    tabControl = ttk.Notebook(login_success_screen)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)

    tabControl.add(tab1, text='Teacher DashBoard')
    tabControl.add(tab2, text='Add Student')
    tabControl.add(tab3, text='Remove Student')
    tabControl.add(tab4, text='Check Student')
    tabControl.pack(expand=1, fill="both")
    tabControl.bind('<<NotebookTabChanged>>', tabChangedHandler)

    ttk.Label(tab1,
              text="Welcome to the main teacher Menu").grid(column=0, row=0, padx=30, pady=30)
    ttk.Label(tab2,
              text="").grid(column=0, row=0, padx=30, pady=30)
    ttk.Label(tab3,
              text="").grid(column=0, row=0, padx=30, pady=30)
    ttk.Label(tab4,
              text="").grid(column=0, row=0, padx=30, pady=30)
    ttk.Label(tab5,
              text="").grid(column=0, row=0, padx=30, pady=30)


def tabChangedHandler(event):
    tab = event.widget.tab('current')['text']
    if tab == 'Teacher DashBoard':
        print("Testing")
    elif tab == 'Add Student':
        print("activating function")
        addStudentUI()
    elif tab == 'Remove Student':
        delStudentUI()
    elif tab == 'Check Student':
        checkStudentUI()


def checkStudentUI():
    global userNameLabel
    global previousResultLabel
    global bestResultLabel
    global averageScoreLabel
    global courseCodeLabel
    Label(tab4, text="Please enter the student's username").grid(
        row=1, column=0, sticky='NWSE', padx=1)
    userNameEntry = Entry(tab4)
    userNameEntry.grid(row=1, column=1, sticky='NWSE', padx=1)
    Label(tab4, text="Username:").grid(
        row=2, column=0, sticky="NWSE", padx=1)
    Label(tab4, text="Previous Result:").grid(
        row=3, column=0, sticky="NWSE", padx=1)
    Label(tab4, text="Best Result:").grid(
        row=4, column=0, sticky="NWSE", padx=1)
    Label(tab4, text="Average Score:").grid(
        row=5, column=0, sticky="NWSE", padx=1)
    Label(tab4, text="Course Code:").grid(
        row=6, column=0, sticky="NWSE", padx=1)

    userNameLabel = Label(tab4)
    userNameLabel.grid(row=2, column=1, sticky="NWSE", padx=1)
    previousResultLabel = Label(tab4)
    previousResultLabel.grid(row=3, column=1, sticky="NWSE", padx=1)
    bestResultLabel = Label(tab4)
    bestResultLabel.grid(row=4, column=1, sticky="NWSE", padx=1)
    averageScoreLabel = Label(tab4)
    averageScoreLabel.grid(row=5, column=1, sticky="NWSE", padx=1)
    courseCodeLabel = Label(tab4)
    courseCodeLabel.grid(row=6, column=1, sticky="NWSE", padx=1)

    Label(tab4, text="New course code:").grid(
        row=8, column=0, sticky='NWSE', padx=1)
    codeEntry = Entry(tab4)
    codeEntry.grid(row=8, column=1, sticky='NWSE', padx=1)
    Button(tab4, text="Check Progress",
           command=lambda: showCode(userNameEntry.get())).grid(row=7, column=0, sticky="NWSE")
    Button(tab4, text="Change Code",
           command=lambda: editFiles("UserName", userNameEntry.get(), "Code", codeEntry.get(), courseCodeLabel)).grid(row=7, column=1, sticky="NWSE")


def showCode(user):
    with open(studentPath) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if any(row):
                if user in row[0]:
                    userName = row[0]
                    courseCode = row[4]
    file.close()
    checkProgress(userName, courseCode)


def checkProgress(user, code):
    # try:
    storePrevResults = []
    count = 0
    with open('result.csv', 'r') as studentProgress:
        csv_reader = csv.DictReader(studentProgress)
        for row in csv_reader:
            if user == row["UserName"]:
                count += 1
                previousResults = row["PreviousResult"]
                storePrevResults.append(int(previousResults))
        total = sum(storePrevResults)
        averageScore = round(total / count, 2)
        bestResult = max(storePrevResults)

        userNameLabel.config(text=user)
        previousResultLabel.config(text=previousResults)
        bestResultLabel.config(text=bestResult)
        averageScoreLabel.config(text=averageScore)
        courseCodeLabel.config(text=code)
        print(
            f"The average score of {user} is {averageScore:.2f}, their previous result was {previousResults} and this students best score so far was {bestResult}.")
        studentProgress.close()
    # except ZeroDivisionError:
    #     print("Error, usually because the user wasn't found or they have no records yet.")
    #     studentProgress.close()


def delStudentUI():
    global listbox1
    global list_of_entries
    list_of_entries = []
    var = StringVar(value=list_of_entries)
    listbox1 = Listbox(tab3, listvariable=var)
    listbox1.grid(row=0, column=0)
    fNameEntry = Entry(tab3)
    fNameEntry.grid(row=2, column=0, sticky="NWSE")
    lNameEntry = Entry(tab3)
    lNameEntry.grid(row=3, column=0, sticky="NWSE")
    Button(tab3, text="Search for Student",
           command=lambda: studentSearch(str(fNameEntry.get()), lNameEntry.get())).grid(row=4, column=0, sticky="NWSE")
    Button(tab3, text="Grab Student Details",
           command=studentDetails).grid(row=5, column=0, sticky="NWSE")
    Button(tab3, text="Delete Student",
           command=deleteStudent).grid(row=4, column=1, rowspan=2, sticky="NWSE")


def studentSearch(first, last):
    with open(studentPath) as f:
        reader = csv.reader(f)
        next(reader)
        listbox1.delete(0, END)
        for row in reader:
            if any(row):
                if first in row[1] and last in row[2]:
                    list_of_entries.append(row[1])
                    listbox1.insert("end", row[0])
        f.close()


def studentDetails():
    Label(tab3, text="Username").grid(
        row=6, column=0, sticky="NWSE", padx=1)
    Label(tab3, text="First Name").grid(
        row=7, column=0, sticky="NWSE", padx=1)
    Label(tab3, text="Last Name").grid(
        row=8, column=0, sticky="NWSE", padx=1)
    Label(tab3, text="Level").grid(
        row=9, column=0, sticky="NWSE", padx=1)
    Label(tab3, text="Code").grid(
        row=10, column=0, sticky="NWSE", padx=1)
    Label(tab3, text="Best Result").grid(
        row=11, column=0, sticky="NWSE", padx=1)

    userNameLabel2 = Label(tab3)
    userNameLabel2.grid(row=6, column=1, sticky="NWSE", padx=1)
    firstNameLabel2 = Label(tab3)
    firstNameLabel2.grid(row=7, column=1, sticky="NWSE", padx=1)
    lastNameLabel2 = Label(tab3)
    lastNameLabel2.grid(row=8, column=1, sticky="NWSE", padx=1)
    levelLabel2 = Label(tab3)
    levelLabel2.grid(row=9, column=1, sticky="NWSE", padx=1)
    codeLabel2 = Label(tab3)
    codeLabel2.grid(row=10, column=1, sticky="NWSE", padx=1)
    bestResultLabel2 = Label(tab3)
    bestResultLabel2.grid(row=11, column=1, sticky="NWSE", padx=1)

    search = listbox1.get(listbox1.curselection()[0])
    with open(studentPath) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if any(row):
                if search in row[0]:
                    # Populate empty labels with results from file
                    userNameLabel2.config(text=row[0])
                    firstNameLabel2.config(text=row[1])
                    lastNameLabel2.config(text=row[2])
                    levelLabel2.config(text=row[3])
                    codeLabel2.config(text=row[4])
                    bestResultLabel2.config(text=row[5])


def deleteStudent():
    user = listbox1.get(listbox1.curselection()[0])
    updatedlist = []
    with open("/Users/jake/College/college-software-solution/student.csv", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if any(row):
                if row[0] != user:
                    updatedlist.append(row)
        print(updatedlist)  # testing
    with open("/Users/jake/College/college-software-solution/student.csv", "w", newline="") as f:
        Writer = csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")
        f.close()
        studentSearch("", "")


def addStudentUI():
    Label(tab2, text="Username").grid(
        row=1, column=0, sticky="NWSE", padx=1)
    Label(tab2, text="First Name").grid(
        row=2, column=0, sticky="NWSE", padx=1)
    Label(tab2, text="Last Name").grid(
        row=3, column=0, sticky="NWSE", padx=1)
    Label(tab2, text="Level").grid(
        row=4, column=0, sticky="NWSE", padx=1)
    Label(tab2, text="Code").grid(
        row=5, column=0, sticky="NWSE", padx=1)

    userNameEntry = Entry(tab2)
    userNameEntry.grid(row=1, column=1, sticky="NWSE", padx=1)
    fNameEntry = Entry(tab2)
    fNameEntry.grid(row=2, column=1, sticky="NWSE", padx=1)
    lNameEntry = Entry(tab2)
    lNameEntry.grid(row=3, column=1, sticky="NWSE", padx=1)
    levelEntry = Entry(tab2)
    levelEntry.grid(row=4, column=1, sticky="NWSE", padx=1)
    codeEntry = Entry(tab2)
    codeEntry.grid(row=5, column=1, sticky="NWSE", padx=1)

    Button(tab2, text="Add a student",
           command=lambda: addStudent(
               str(userNameEntry.get()), str(fNameEntry.get()),
               str(lNameEntry.get()), str(levelEntry.get()),
               str(codeEntry.get()))).grid(row=0, column=0,
                                           sticky="NWSE")


def addStudent(user, first, last, level, code):
    newData = open(
        '/Users/jake/College/college-software-solution/student.csv', 'a')
    BestResult = "0"
    line = ("\n" + user + "," + first + "," + last +
            "," + level + "," + code + "," + BestResult)
    newData.write(line)
    newData.close()


def mathGameUI():
    global firstNumber
    global secondNumber
    global mathSign
    global num2
    global level
    global gameFrame
    global prevQuestions
    global login
    global wrongAnswer
    global gameUI
    global question
    question = 0
    wrongAnswer = 0
    prevQuestions = []

    login = username.get()
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
    studentData.close()
    with open(resultPath, 'r') as resultData:
        csv_reader = csv.DictReader(resultData)
        for row in csv_reader:
            if login == row['UserName']:
                previousResult = row['PreviousResult']
        if bestResult == 0:
            response = str(
                f"Welcome, {name}! It's your first time playing, good luck!")
        else:
            response = str(
                f"Welcome, {name}! Your last result was: {previousResult} and your best result was: {bestResult}.")

    messagebox.showinfo("User Information", response)

    gameUI = Toplevel(main_screen)
    gameUI.title("Math Game")
    gameUI.geometry("700x700")
    gameFrame = Frame(gameUI, width=500, height=500)
    gameFrame.pack(fill="both", expand=1)
    global gameLabel
    gameLabel = Label(gameFrame, text="", font=("Helvetica", 18))
    gameLabel.pack(pady=15)
    mathFrame = Frame(gameFrame, width=400, height=300)
    mathFrame.pack()

    firstNumber = Label(mathFrame, font=("Helvetica", 28))
    secondNumber = Label(mathFrame, font=("Helvetica", 28))
    mathSign = Label(mathFrame, text="+", font=("Helvetica", 28))

    # Grid our labels
    firstNumber.grid(row=0, column=0)
    mathSign.grid(row=0, column=1)
    secondNumber.grid(row=0, column=2)
    # Create answer box and button
    global add_answer
    add_answer = Entry(gameFrame, font=("Helvetica", 18))
    add_answer.pack(pady=30)

    global add_answer_button
    add_answer_button = Button(
        gameFrame, text="Answer", command=lambda: getAnswer(result, bestResult))
    add_answer_button.pack()

    global answer_message
    answer_message = Label(gameFrame, text="", font=("Helvetica", 18))
    answer_message.pack(pady=10)

    global resultPlaceholder
    resultPlaceholder = Label(gameFrame, text="", font=("Helvetica", 18))
    resultPlaceholder.pack(pady=10)
    global resultLabel
    resultLabel = Label(gameFrame, text="", font=("Helvetica", 18))
    resultLabel.pack(padx=10)

    mathsTest(bestResult)


def mathsTest(bestResult):
    global question
    global result
    global startTime
    startTime = time()
    question += 1
    if question != 11:
        questionCount = str("Question number: %d" % question)
        gameLabel.config(text=questionCount)

        a, operator, b, result = calculate(operatorDict)
        currentQuestion = (str(a) + ' ' + str(operator) + ' ' + str(b))

        while currentQuestion in prevQuestions:
            print('dupe detected', a, operator, b)
            a, operator, b, result = calculate(operatorDict)
            currentQuestion = (str(a) + ' ' + str(operator) + ' ' + str(b))

        firstNumber["text"] = str(a)
        mathSign["text"] = str(operator)
        secondNumber["text"] = str(b)
        print(a, operator, b)
        print(f"Answer = {result}")  # testing

        store = (str(a) + ' ' + str(operator) + ' ' + str(b))
        prevQuestions.append(store)
        print(prevQuestions)

    if question == 11:
        gameOver()
        storeResults(login, wrongAnswer, bestResult)


def calculate(operatorDict):
    try:
        operator = random.choice(["/", "+", "-", "*"])
        a = random.randrange(num1, num2, 1)
        b = random.randrange(num1, num2, 1)
        result = operatorDict[operator](a, b)
        if level != 3:
            while result < 0 or b > a and operator == "/":
                print("inside first negative check: ", a, operator, b, result)
                operator = random.choice(["/", "+", "-", "*"])
                a = random.randrange(num1, num2, 1)
                b = random.randrange(num1, num2, 1)
                print("Generating new numbers:", a, operator, b)  # Testing
                result = operatorDict[operator](a, b)
    except ZeroDivisionError:
        print("Zero division inside calculate function ",
              a, operator, b)  # testing
        a = random.randrange(num1, num2, 1)
        b = random.randrange(num1, num2, 1)
        operatorNoDiv = random.choice(["+", "-", "*"])
        result = operatorDict[operatorNoDiv](a, b)
        while level != 3 and result < 0:
            print("Validating inside if statement", a, operator, b)  # testing
            operatorNoDiv = random.choice(["+", "-", "*"])
            a = random.randrange(num1, num2, 1)
            b = random.randrange(num1, num2, 1)
            result = operatorDict[operatorNoDiv](a, b)
        return a, operatorNoDiv, b, result
    return a, operator, b, result


def getAnswer(result, bestResult):
    global wrongAnswer
    answer = int(add_answer.get())
    elapsedTime = time() - startTime
    if answer == result:
        response = f"Correct! the answer was {result} and it took you {elapsedTime:.2f} seconds"
    elif answer != result:
        wrongAnswer += 1
        response = f"Wrong! the answer was {result} and it took you {elapsedTime:.2f} seconds"
    answer_message.config(text=response)
    add_answer.delete(0, END)
    mathsTest(bestResult)


def gameOver():
    print("Game Over")
    add_answer_button["state"] = "disabled"
    add_answer["state"] = "disabled"
    firstNumber["text"] = "Game"
    mathSign["text"] = ""
    secondNumber["text"] = "Over!"
    correct = 10 - wrongAnswer
    response = f"You have completed the game with {correct} correct answers and {wrongAnswer} wrong answers"
    answer_message.config(text=response)
    playAgain = Button(gameFrame, text="Play Again?", command=restart)
    playAgain.pack()


def restart():
    gameUI.destroy()
    mathGameUI()


def storeResults(login, wrongAnswer, bestResult):
    testResult = 10 - wrongAnswer
    currentDate = date.today()
    time = datetime.now()
    studentRecords = open(
        'result.csv', 'a')

    line = ("\n" + login + "," + str(testResult) + "," +
            currentDate.strftime("%d-%m-%Y") + "," +
            time.strftime("%H:%M:%S"))

    print("Details added to database:",
          login + " " + str(testResult) + " " +
          currentDate.strftime("%d-%m-%Y") + " " +
          time.strftime("%H:%M:%S"))

    studentRecords.write(line)
    studentRecords.close()

    if testResult > bestResult:
        updateBestResult(login, testResult)
    elif testResult == int(bestResult):
        resultPlaceholder.config(text="Tied personal best!")
        print("Tied personal best!")
    else:
        resultPlaceholder.config(
            text="Unfortunately, you didn't get a new personal best.")
        print("\nUnfortunately, you didn't get a new personal best.")


def updateBestResult(login, result):
    editFiles("UserName", login, "BestResult", result, resultLabel)
    resultPlaceholder.config(
        text="New Personal best! Congratulations, your file has been updated.")
    resultLabel.config(text="")


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised).pack()


def editFiles(storedUser, login, old, new, label):
    with fileinput.input(files=(studentPath),
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
    label.config(text=new)


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()


def delete_login_success():
    login_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def main():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Please log in.", width="300",
          height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Teacher", height="2", width="30", command=teacherLogin).pack()
    Label(text="").pack()
    Button(text="Student", height="2", width="30", command=studentLogin).pack()
    main_screen.mainloop()


if __name__ == '__main__':
    main()

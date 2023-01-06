from time import time
from datetime import date, datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import fileinput
import operator
import csv

operatorDict = {"+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.floordiv}
studentPath = '/Users/jake/College/college-software-solution/student.csv'
resultPath = '/Users/jake/College/college-software-solution/result.csv'
question = 0
plays = 0
num1 = 0
prevUser = []


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
           height=1, command=lambda: login_verify(str(username_login_entry.get()), str(password_login_entry.get()))).pack()


def login_verify(login, password):
    found = False
    print(login, password)
    path = "/Users/jake/College/college-software-solution/teacherDetails.csv"
    with open(path, 'r') as data:
        csv_reader = csv.DictReader(data)
        for row in csv_reader:
            print(row)  # testing
            if row["User"] == login and row["Password"] == password:
                found = True
                break
        if found == True:
            name = (''.join([row['First'] + ' ' + row['Last']]))
            print("Welcome", name)
            data.close()
            login_success(name)
        else:
            data.close()
            password_not_recognised()


def login_success(teacherName):
    global login_success_screen
    global tab1, tab2, tab3, tab4, tab5
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Student Management")
    login_success_screen.geometry("578x355")
    title = f"Welcome to the teacher dashboard, {teacherName}."
    Label(login_success_screen, text=title).pack()

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

    lbl1 = ttk.Label(tab1,
                     text="Welcome to the teacher dashboard\nHere you will have the option to add, remove or manage students, alongside access to student records showcasing their progress and course code. \nPlease be careful with managing students and check with the IT team if any issues arise.")
    lbl1.config(justify='center')
    lbl1.pack()


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


def teacherDashboard():
    pass


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
    try:
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
    except ZeroDivisionError:
        print("Error, usually because the user wasn't found or they have no records yet.")
        studentProgress.close()
        averageScore = 0
        bestResult = 0
        previousResults = 0
        userNameLabel.config(text=user)
        previousResultLabel.config(text=previousResults)
        bestResultLabel.config(text=bestResult)
        averageScoreLabel.config(text=averageScore)
        courseCodeLabel.config(text=code)


def delStudentUI():
    global listbox1
    global list_of_entries
    list_of_entries = []
    var = StringVar(value=list_of_entries)

    listbox1 = Listbox(tab3, listvariable=var)
    listbox1.grid(row=0, column=0)
    fNameEntry = Entry(tab3)
    fNameEntry.grid(row=1, column=0, sticky="NWSE")
    lNameEntry = Entry(tab3)
    lNameEntry.grid(row=2, column=0, sticky="NWSE")

    Label(tab3, text="Here you can search\nfor a student and\ndelete them if necessary.").grid(
        row=0, column=1, sticky="N")
    Label(tab3, text="Use the Entry\nboxes to search\n for a students\n last or first name.").grid(
        row=0, column=2, sticky="N")

    Label(tab3, text="First Name").grid(
        row=1, column=2, sticky="NWSE", padx=1, pady=1)
    Label(tab3, text="Last Name").grid(
        row=2, column=2, sticky="NWSE", padx=1)
    Label(tab3, text="Level").grid(
        row=3, column=2, sticky="NWSE", padx=1)
    Label(tab3, text="Code").grid(
        row=4, column=2, sticky="NWSE", padx=1)

    Button(tab3, text="Search for Student",
           command=lambda: studentSearch(str(fNameEntry.get()), lNameEntry.get())).grid(row=3, column=0, sticky="NWSE", rowspan=2)
    Button(tab3, text="Grab Student Details",
           command=studentDetails).grid(row=1, column=1, rowspan=2, sticky="NWSE")
    Button(tab3, text="Delete Student",
           command=deleteStudent).grid(row=3, column=1, rowspan=2, sticky="NWSE")


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

    firstNameLabel2 = Label(tab3)
    firstNameLabel2.grid(row=1, column=3, sticky="NWSE", padx=1)
    lastNameLabel2 = Label(tab3)
    lastNameLabel2.grid(row=2, column=3, sticky="NWSE", padx=1)
    levelLabel2 = Label(tab3)
    levelLabel2.grid(row=3, column=3, sticky="NWSE", padx=1)
    codeLabel2 = Label(tab3)
    codeLabel2.grid(row=4, column=3, sticky="NWSE", padx=1)

    search = listbox1.get(listbox1.curselection()[0])
    with open(studentPath) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if any(row):
                if search in row[0]:
                    # Populate empty labels with results from file
                    firstNameLabel2.config(text=row[1])
                    lastNameLabel2.config(text=row[2])
                    levelLabel2.config(text=row[3])
                    codeLabel2.config(text=row[4])


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


def studentLogin():
    global studentLoginScreen
    global username
    global password
    global username_entry

    studentLoginScreen = Toplevel(main_screen)
    studentLoginScreen.title("Register")
    studentLoginScreen.geometry("300x250")
    username = StringVar()

    Label(studentLoginScreen, text="Please enter details below").pack()
    Label(studentLoginScreen, text="").pack()
    username_label = Label(studentLoginScreen, text="Username")
    username_label.pack()
    username_entry = Entry(studentLoginScreen, textvariable=username)
    username_entry.pack()
    Label(studentLoginScreen, text="").pack()
    Button(studentLoginScreen, text="Login", width=10,
           height=1, command=mathGameUI).pack()
    studentLoginScreen.bind('<Return>', (lambda event: mathGameUI()))


def mathGameUI():
    global num2
    global level

    global question
    question = 0
    global wrongAnswer
    wrongAnswer = 0
    global prevQuestions
    prevQuestions = []
    global timeList
    timeList = []

    try:
        global studentUserName
        studentUserName = username.get()
        with open(studentPath, 'r') as studentData:
            csv_reader = csv.DictReader(studentData)
            for row in csv_reader:
                if studentUserName == row["UserName"]:
                    # print(row)  # testing
                    bestResult = int(row["BestResult"])
                    name = (
                        ''.join([row['FirstName'] + ' ' + row['LastName']]))
                    # print("Welcome", name)

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
                if studentUserName == row['UserName']:
                    previousResult = row['PreviousResult']
            if bestResult == 0:
                response = str(
                    f"Welcome, {name}! It's your first time playing, good luck!")
            else:
                response = str(
                    f"Welcome, {name}! Your last result was: {previousResult} and your best result was: {bestResult}.")
        if studentUserName not in prevUser:
            messagebox.showinfo("User Information", response)

        global gameUI
        gameUI = Toplevel(main_screen)
        title = f"Level {level} Maths Game"
        gameUI.title(title)
        gameUI.geometry("635x395")

        global gameFrame
        gameFrame = Frame(gameUI, width=400, height=250)
        gameFrame.pack(fill="both", expand=1)
        global gameLabel
        gameLabel = Label(gameFrame, text="", font=("Helvetica", 18))
        gameLabel.pack(pady=15)
        mathFrame = Frame(gameFrame)
        mathFrame.pack()

        global firstNumber
        firstNumber = Label(mathFrame, font=("Helvetica", 40))
        firstNumber.grid(row=0, column=0)
        global secondNumber
        secondNumber = Label(mathFrame, font=("Helvetica", 40))
        global mathSign
        mathSign = Label(mathFrame, text="", font=("Helvetica", 40))
        mathSign.grid(row=0, column=1)
        secondNumber.grid(row=0, column=2)

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

        global progressBar
        progressBar = ttk.Progressbar(
            gameFrame, orient=HORIZONTAL, length=100, mode='determinate')
        progressBar.pack(padx=20)

        add_answer.bind(
            '<Return>', (lambda event: getAnswer(result, bestResult)))
        mathsTest(bestResult)
    except:
        studentNotFound()


def mathsTest(bestResult):
    global question
    global result
    global startTime
    startTime = time()
    question += 1
    progressBar['value'] += 10
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
        storeResults(studentUserName, wrongAnswer, bestResult)


def calculate(operatorDict):
    try:
        operator = random.choice(["/", "+", "-", "*"])
        a = random.randrange(num1, num2, 1)
        b = random.randrange(num1, num2, 1)
        result = operatorDict[operator](a, b)
        while result < 0 and level != 3 or b > a and operator == "/":
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
    try:
        global wrongAnswer
        global totalTime
        answer = int(add_answer.get())
        elapsedTime = time() - startTime
        timeList.append(float(elapsedTime))
        totalTime = sum(timeList)
        print(f"Total time: {totalTime:.2f} seconds")
        if answer == result:
            response = f"Correct! the answer was {result} and it took you {elapsedTime:.2f} seconds"
        elif answer != result:
            wrongAnswer += 1
            response = f"Wrong! the answer was {result} and it took you {elapsedTime:.2f} seconds"
        answer_message.config(text=response)
        add_answer.delete(0, END)
        mathsTest(bestResult)
    except ValueError:
        messagebox.showinfo("Incorrect Input", "Please only enter numbers.")


def gameOver():
    global plays
    plays += 1
    prevUser.append(studentUserName)
    print(prevUser)
    add_answer_button["state"] = "disabled"
    add_answer["state"] = "disabled"
    firstNumber["text"] = "Game"
    mathSign["text"] = ""
    secondNumber["text"] = "Over!"
    progressBar.pack_forget()
    correct = 10 - wrongAnswer
    response = f"You have completed the game with {correct} correct answers and {wrongAnswer} wrong answers, \nand overall it took you {totalTime:.2f} seconds to complete"
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
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("200x100")
    Label(password_not_recog_screen,
          text="Invalid username or Password").pack(pady=20)
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


def studentNotFound():
    global studentNotFound_screen
    studentNotFound_screen = Toplevel(studentLoginScreen)
    studentNotFound_screen.title("Error")
    studentNotFound_screen.geometry("150x100")
    Label(studentNotFound_screen, text="User Not Found").pack(pady=20)
    Button(studentNotFound_screen, text="OK",
           command=delete_studentNotFound_screen).pack()


def delete_login_success():
    login_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_studentNotFound_screen():
    studentNotFound_screen.destroy()


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

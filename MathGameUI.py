from datetime import date, datetime
from tkinter import messagebox
from tkinter import ttk
from threading import *
from tkinter import *
from time import time

import fileinput
import operator
import random
import csv
import os

# Using the operator import, this is how I randomly choose operators.

operatorDict = {"+": operator.add,
                "-": operator.sub,
                u"\u00D7": operator.mul,
                u"\u00F7": operator.floordiv}

chimeFile = "/Users/jake/College/college-software-solution/correct.mp3"
buzzFile = "/Users/jake/College/college-software-solution/wrong2.mp3"
pbFile = "/Users/jake/College/College-software-solution/celebrate.mp3"

studentPath = '/Users/jake/College/college-software-solution/student.csv'
resultPath = '/Users/jake/College/college-software-solution/result.csv'

# This is unicode for emojis I am using within the game, please let me know if they don't work properly.

thinkingFace = u"\U0001F914"
happyFace = u"\U0001F929"
sadFace = u"\U0001F62D"
multiSymbol = u"\u00D7"
divSymbol = u"\u00F7"

num1 = 0
question = 0
prevUser = []


def teacherLogin():
    global login_screen
    global username_verify
    global teacherUserEntry
    global teacherPasswordEntry

    # Teacher login function, this is just some UI code.

    login_screen = Toplevel(main_screen)
    login_screen.title("EduSoft Teacher Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username").pack()
    teacherUserEntry = Entry(
        login_screen, textvariable=username_verify)
    teacherUserEntry.pack()

    Label(login_screen, text="Password").pack()
    teacherPasswordEntry = Entry(
        login_screen, textvariable=password_verify, show='*')
    teacherPasswordEntry.pack()

    Button(login_screen, text="Login", width=10,
           height=1, command=lambda:
               teacherVerify(str(teacherUserEntry.get()), str(teacherPasswordEntry.get()))).pack()
    login_screen.bind('<Return>', (lambda event:
                                   teacherVerify(str(teacherUserEntry.get()), str(teacherPasswordEntry.get()))))


def teacherVerify(login, password):

    # This is the data validation for the teacher's login.
    teacherUserEntry.delete(0, END)
    teacherPasswordEntry.delete(0, END)
    # this found variable changes to True if the data is correctly validated, running the next part of code.
    found = False
    print(login, password)  # testing
    path = "/Users/jake/College/college-software-solution/teacherDetails.csv"
    with open(path, 'r') as data:
        csv_reader = csv.DictReader(data)
        for row in csv_reader:
            print(row)  # testing
            if row["User"] == login and row["Password"] == password:
                found = True
                global teacherClassCode
                teacherClassCode = row["Code"]
                break
        if found == True:
            name = (''.join([row['First'] + ' ' + row['Last']]))
            print("Welcome", name)  # testing
            data.close()
            login_success(name)
        else:
            data.close()
            passwordNotFound()


def login_success(teacherName):
    global login_success_screen
    global tab1, tab2, tab3, tab4, tab5

    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("EduSoft Student Management")
    login_success_screen.geometry("595x355")
    login_success_screen.resizable(0, 0)
    title = f"Welcome to the teacher dashboard, {teacherName}."
    Label(login_success_screen, text=title).pack()
    login_screen.withdraw()
    main_screen.withdraw()
    # This piece of code using the protocol function, opens the previously withdrawn windows if the teacher
    # closes the window
    login_success_screen.protocol("WM_DELETE_WINDOW", returnToTeacherLogin)

    # Using ttk.Notebook to show the tabs for the teacher dashboard
    tabControl = ttk.Notebook(login_success_screen)
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl)
    tab3 = ttk.Frame(tabControl)
    tab4 = ttk.Frame(tabControl)
    tab5 = ttk.Frame(tabControl)

    # The code for the main part of the dashboard
    tabControl.add(tab1, text='Teacher Information')
    ttk.Label(tab1, text="Welcome to the teacher dashboard").pack()
    ttk.Label(
        tab1, text="Here you will have the option to add, remove or manage students").pack()
    ttk.Label(
        tab1, text="Alongside access to student records showcasing their progress and course code.").pack()
    ttk.Label(tab1, text="Contact the IT team if any issues arise, or if you are unsure on using the program").pack()
    Button(tab1, text="Change Teacher", command=returnToTeacherLogin).pack()

    tabControl.add(tab2, text='Add Student')
    tabControl.add(tab3, text='Remove Student')
    tabControl.add(tab4, text='Check Student')
    tabControl.pack(expand=1, fill="both")
    # Binding the event name of changing tabs to a function, so that new UI gets added based on the tab chosen.
    tabControl.bind('<<NotebookTabChanged>>', tabChangedHandler)


def tabChangedHandler(event):

    # Getting the name of the tab in order to choose which function to open.
    tab = event.widget.tab('current')['text']
    if tab == 'Teacher Information':
        pass
    elif tab == 'Add Student':
        print("activating function")
        addStudentUI()
    elif tab == 'Remove Student':
        delStudentUI()
    elif tab == 'Check Student':
        checkStudentUI()
    else:
        messagebox.showerror("Error: Unknown tab",
                             "Sorry, but you have somehow navigated to an unknown tab.")


def returnToTeacherLogin():
    # This function re-opens any hidden windows.
    main_screen.deiconify()
    login_screen.deiconify()
    login_success_screen.destroy()


def checkStudentUI():
    global studentNameLabel
    global previousResultLabel
    global bestResultLabel
    global averageScoreLabel
    global averageTimeLabel
    global courseCodeLabel
    global bestTimeLabel

    Label(tab4, text="Please enter the student's username").grid(
        row=1, column=0, sticky='NWSE', padx=1)
    global userNameEntryCheck
    userNameEntryCheck = Entry(tab4)
    userNameEntryCheck.grid(row=1, column=1, sticky='NWSE', padx=1)
    Label(tab4, text="Full name:").grid(
        row=2, column=0, sticky="NWSE", padx=1)
    Label(tab4, text="Previous Result:").grid(
        row=3, column=0, sticky="NWSE", padx=1)
    Label(tab4, text="Best Result:").grid(
        row=4, column=0, sticky="NWSE", padx=1)
    Label(tab4, text="Best Time:").grid(
        row=5, column=0, sticky="NWSE", padx=1)
    Label(tab4, text="Average Score:").grid(
        row=6, column=0, sticky="NWSE", padx=1)
    Label(tab4, text="Average Time:").grid(
        row=7, column=0, sticky="NWSE", padx=1)
    Label(tab4, text="Course Code:").grid(
        row=8, column=0, sticky="NWSE", padx=1)

    studentNameLabel = Label(tab4)
    studentNameLabel.grid(row=2, column=1, sticky="NWSE", padx=1)
    previousResultLabel = Label(tab4)
    previousResultLabel.grid(row=3, column=1, sticky="NWSE", padx=1)
    bestResultLabel = Label(tab4)
    bestResultLabel.grid(row=4, column=1, sticky="NWSE", padx=1)
    bestTimeLabel = Label(tab4)
    bestTimeLabel.grid(row=5, column=1, sticky="NWSE", padx=1)
    averageScoreLabel = Label(tab4)
    averageScoreLabel.grid(row=6, column=1, sticky="NWSE", padx=1)
    averageTimeLabel = Label(tab4)
    averageTimeLabel.grid(row=7, column=1, sticky="NWSE", padx=1)
    courseCodeLabel = Label(tab4)
    courseCodeLabel.grid(row=8, column=1, sticky="NWSE", padx=1)

    Label(tab4, text="New course code:").grid(
        row=9, column=0, sticky='NWSE', padx=1)
    global codeEntry
    codeEntry = Entry(tab4)
    codeEntry.grid(row=9, column=1, sticky='NWSE', padx=1)

    # Using some lambda functions in order to parse the arguments i want to the function.
    Button(tab4, text="Check Progress",
           command=lambda: showCode(
               userNameEntryCheck.get())).grid(row=10, column=0, sticky="NWSE")

    Button(tab4, text="Change Code",
           command=lambda: editFiles(
               "UserName",
               str(userNameEntryCheck.get()),
               "Code",
               codeEntry.get(),
               courseCodeLabel)).grid(row=10, column=1, sticky="NWSE")

    # Binding the Enter key to allow some keyboard functionality for the user.
    userNameEntryCheck.bind('<Return>', lambda event: showCode(
        str(userNameEntryCheck.get())))


def showCode(user):
    inClass = False
    with open(studentPath) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if any(row):
                if user in row[0] and row[4] == teacherClassCode:
                    inClass = True
                    break
        if inClass == True:
            courseCode = row[4]
            userName = row[0]
            studentName = (
                ''.join([row[1] + ' ' + row[2]]))
            file.close()
            checkProgress(userName, courseCode, studentName)
        elif inClass == False:
            studentNameLabel.config(text="")
            previousResultLabel.config(text="")
            bestResultLabel.config(text="")
            bestTimeLabel.config(text="")
            averageScoreLabel.config(text="")
            averageTimeLabel.config(text="")
            courseCodeLabel.config(text="")
            userNameEntryCheck.delete(0, END)
            codeEntry.delete(0, END)
            print("Student is not in this teachers class, please try again.")


def checkProgress(user, code, name):
    try:
        storePrevResults = []
        storePrevTime = []
        count = 0

        with open('result.csv', 'r') as studentProgress:
            csv_reader = csv.DictReader(studentProgress)
            for row in csv_reader:
                if user == row["UserName"]:
                    # If the user is found, I add their previous results and previous times to a list
                    count += 1
                    previousResults = row["PreviousResult"]
                    storePrevResults.append(int(previousResults))
                    if row["TimeToComplete"] != None:
                        previousTime = row["TimeToComplete"]
                        storePrevTime.append(float(previousTime))

            # Once they're added the individual lists, I use these two small blocks of code to calculate the
            # average and the best results
            total = sum(storePrevResults)
            averageScore = round(total / count, 2)
            bestResult = max(storePrevResults)

            total2 = sum(storePrevTime)
            averageTime = round(total2 / count, 2)
            bestTime = min(storePrevTime)

            studentNameLabel.config(text=name)
            previousResultLabel.config(text=previousResults)
            bestResultLabel.config(text=bestResult)
            bestTimeLabel.config(text=bestTime)
            averageScoreLabel.config(text=averageScore)
            averageTimeLabel.config(text=averageTime)
            courseCodeLabel.config(text=code)
            print(
                f"The average score of {user} is {averageScore:.2f}, their previous result was {previousResults} and this students best score so far was {bestResult}.")
            studentProgress.close()
    except ZeroDivisionError:
        # Some error handling, mostly for new students.
        print("Error, usually because the user wasn't found or they have no records yet.")
        studentProgress.close()
        averageScore = 0
        bestResult = 0
        previousResults = 0
        studentNameLabel.config(text=name)
        previousResultLabel.config(text=previousResults)
        bestResultLabel.config(text=bestResult)
        averageScoreLabel.config(text=averageScore)
        courseCodeLabel.config(text=code)


def delStudentUI():
    global listbox1
    global list_of_entries
    # An empty list to hold the results of the student search.
    list_of_entries = []
    var = StringVar(value=list_of_entries)

    listbox1 = Listbox(tab3, listvariable=var)
    listbox1.grid(row=0, column=0)
    fNameEntry = Entry(tab3)
    fNameEntry.grid(row=1, column=0, sticky="NWSE")
    lNameEntry = Entry(tab3)
    lNameEntry.grid(row=2, column=0, sticky="NWSE")

    Label(tab3, text="Here you can search\nfor a student and\ndelete them if necessary.\nUse the Entry boxes to search\nfor a students FIRST or LAST name.").grid(
        row=0, column=1, sticky="NS")

    Label(tab3, text="First Name").grid(
        row=1, column=2, sticky="NWSE", padx=1)
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
    # I bind Enter to the student details function which displays the student details of the chosen student.
    listbox1.bind('<Return>', (lambda event: studentDetails()))
    # I also bind Back Space to the delete student function which deletes the student selected.
    listbox1.bind('<BackSpace>', (lambda event: deleteStudent()))
    # I bind enter to the student search function which displays the results of the student search.
    fNameEntry.bind('<Return>', (lambda event: studentSearch(
        str(fNameEntry.get()), lNameEntry.get())))
    lNameEntry.bind('<Return>', (lambda event: studentSearch(
        str(fNameEntry.get()), lNameEntry.get())))


def studentSearch(first, last):
    inClass = False
    with open(studentPath) as f:
        reader = csv.reader(f)
        next(reader)
        listbox1.delete(0, END)
        for row in reader:
            if any(row):
                if first in row[1] and last in row[2]:
                    if row[4] == teacherClassCode:
                        inClass = True
                        list_of_entries.append(row[1])
                        listbox1.insert("end", row[0])
        if inClass == False:
            print("This student is not in your class, please try again.")
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

    # I use the curselection function to generate the results based on who is selected in the listbox.
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
    # I use the curselection function to generate the results based on who is selected in the listbox.
    user = listbox1.get(listbox1.curselection()[0])
    updatedlist = []

    with open(studentPath) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if any(row):
                if user in row[0]:
                    name = (''.join([row[1] + ' ' + row[2]]))
    f.close()
    # I open the student file twice here to handle deleting the student, I add every student except the chosen one to
    # The empty list above, and I then open the file again to update the file with the new list.
    with open("/Users/jake/College/college-software-solution/student.csv", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            if any(row):
                if row[0] != user:
                    updatedlist.append(row)
        print(updatedlist)  # testing
    f.close()

    with open("/Users/jake/College/college-software-solution/student.csv", "w", newline="") as f:
        Writer = csv.writer(f)
        Writer.writerows(updatedlist)
        print("File has been updated")
        f.close()
        # I call the student search function again with decimal points entered acting as the first and last name in order to show an EMPTY listbox.
        studentSearch("", "")
    message = f"The student {name} has been deleted from the system. Please contact IT if this was a mistake."
    messagebox.showwarning("Student Deleted", message)


def addStudentUI():
    labelToBind = Label(tab2, text="Username")
    labelToBind.grid(
        row=0, column=0, sticky="NWSE")
    Label(tab2, text="First Name").grid(
        row=1, column=0, sticky="NWSE")
    Label(tab2, text="Last Name").grid(
        row=2, column=0, sticky="NWSE")
    Label(tab2, text="Level").grid(
        row=3, column=0, sticky="NWSE")
    Label(tab2, text="Code").grid(
        row=4, column=0, sticky="NWSE")

    Label(tab2, text="Please use this program to add new\nstudents to your class. All you\nneed to do is input the new students\ndata into the boxes and then click submit.").grid(
        row=0, column=2, sticky="N", rowspan=5)

    userNameEntry = Entry(tab2)
    userNameEntry.grid(row=0, column=1, sticky="NWSE")
    fNameEntry = Entry(tab2)
    fNameEntry.grid(row=1, column=1, sticky="NWSE")
    lNameEntry = Entry(tab2)
    lNameEntry.grid(row=2, column=1, sticky="NWSE")
    levelEntry = Entry(tab2)
    levelEntry.grid(row=3, column=1, sticky="NWSE")
    codeEntry = Entry(tab2)
    codeEntry.grid(row=4, column=1, sticky="NWSE")

    addStudentButton = Button(tab2, text="Add a student",
                              command=lambda: addStudent(str(userNameEntry.get()),
                                                         str(fNameEntry.get()),
                                                         str(lNameEntry.get()),
                                                         str(levelEntry.get()),
                                                         str(codeEntry.get())))
    addStudentButton.grid(row=6, column=0, columnspan=2, sticky="NWSE")
    codeEntry.bind('<Return>', (lambda event: addStudent(str(userNameEntry.get()),
                                                         str(fNameEntry.get()),
                                                         str(lNameEntry.get()),
                                                         str(levelEntry.get()),
                                                         str(codeEntry.get()))))


def addStudent(user, first, last, level, code):
    addStudentUI()
    if int(level) in range(1, 3 + 1):
        if code == teacherClassCode:
            newData = open(
                '/Users/jake/College/college-software-solution/student.csv', 'a')
            line = ("\n" + user + "," + first + "," + last +
                    "," + level + "," + code)
            newData.write(line)
            newData.close()
            message = f"The new student {first} {last} was added to the system successfully."
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror(
                "Error", "This student cannot be added to your classroom as the Course Code is incorrect.")
            print(
                "This student cannot be added to your classroom as the Course Code is incorrect.")
    else:
        messagebox.showerror(
            "Error", "The students level must be between 1 and 3.")


def studentLogin():
    global studentLoginScreen
    global username_entry

    studentLoginScreen = Toplevel(main_screen)
    studentLoginScreen.title("EduSoft Student Login")
    studentLoginScreen.geometry("300x175")

    Label(studentLoginScreen, text="Please enter details below",
          font=("Helvetica", 20)).pack()
    Label(studentLoginScreen, text="Username",
          font=("Helvetica", 18)).pack(pady=10)

    global username_entry
    username_entry = Entry(studentLoginScreen)
    username_entry.pack()

    Label(studentLoginScreen, text="").pack()
    Button(studentLoginScreen, text="Go!", width=10,
           height=2, command=mathGameUI).pack()

    studentLoginScreen.bind('<Return>', (lambda event: mathGameUI()))


def mathGameUI():
    """mathGameUI function summary:

    This function is used to display the UI for the game, and validating the students via the try and except method. 
    When the student signs in their best result, previous times, best time, level and name are stored into variables.
    The user is welcomed with an infobox containing their name, previous result and best score. 
    """

    num2 = 10
    question = 0
    wrongAnswer = 0
    prevQuestions = []
    global timeList
    timeList = []
    newStudent = True

    # This verifies the student login and if the user doesn't except, it triggers an exception
    # Which will then open the userNotFound Function. Also, I have a variable called newStudent which is set to
    # true by default, in order to search for any new students in the database, and to set their parameters
    # for the game accordingly.

    try:
        global studentUserName
        studentUserName = username_entry.get()
        # Opens file
        with open(studentPath, 'r') as studentData:
            csv_reader = csv.DictReader(studentData)
            for row in csv_reader:
                if studentUserName == row["UserName"]:
                    name = (
                        ''.join([row['FirstName'] + ' ' + row['LastName']]))
                    if row["BestResult"] != None:
                        print("not new")
                        newStudent = False
                        bestResult = int(row["BestResult"])

                    # If statement to set up the game according to the students' levels

                    if int(row["Level"]) == 1:
                        level = 1
                        num1 = 0
                        num2 = 10
                    elif int(row["Level"]) == 2:
                        level = 2
                        num1 = 0
                        num2 = 100
                    elif int(row["Level"]) == 3:
                        level = 3
                        num1 = -100
                        num2 = 100

        studentData.close()
        # Gets the students best time and Previous results

        storePrevTimes = []

        with open(resultPath, 'r') as resultData:
            csv_reader = csv.DictReader(resultData)
            for row in csv_reader:
                if studentUserName == row['UserName']:
                    previousResult = row['PreviousResult']
                    if row["TimeToComplete"] != None:
                        storePrevTimes.append(float(row["TimeToComplete"]))

            if newStudent == False:
                if not storePrevTimes:
                    bestTime = None
                else:
                    bestTime = min(storePrevTimes)
                if previousResult == "":
                    previousResult = 0
                response = str(
                    f"Welcome, {name}! Your last result was: {previousResult} and your best result was: {bestResult}.")

            elif newStudent == True:
                # If the student is new, I set their bestResult to NoneType, and their bestTime to NoneType.
                print("test")
                bestResult = None
                bestTime = None
                response = str(
                    f"Welcome, {name}! It's your first time playing, good luck!")

        if studentUserName not in prevUser:
            messagebox.showinfo("User Information", response)

        global gameUI
        gameUI = Toplevel(main_screen)
        studentLoginScreen.withdraw()
        main_screen.withdraw()
        title = f"EduSoft Level {level} Maths Game"
        gameUI.title(title)
        gameUI.geometry("635x400")
        gameUI.resizable(0, 0)
        gameUI.protocol("WM_DELETE_WINDOW", userChange)

        global gameFrame
        gameFrame = Frame(gameUI, width=400, height=250)
        gameFrame.pack(fill="both", expand=1)
        global gameLabel
        gameLabel = Label(gameFrame, text="", font=("Helvetica", 18))
        gameLabel.pack(pady=15)

        global progressBar
        # Progress bar I added for the student to visually see how many questions are left.
        progressBar = ttk.Progressbar(
            gameFrame, orient=HORIZONTAL, length=100, mode='determinate')
        progressBar.pack()

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

        global answer_message
        answer_message = Label(gameFrame, text="", font=("Helvetica", 18))
        answer_message.pack(pady=10)

        global emojiHolder
        emojiHolder = Label(gameFrame, text=thinkingFace,
                            font=("Helvetica", 60))
        emojiHolder.pack()

        # Calling the mathsTest function which has a **kwargs argument, allowing me to parse as many arguments as necessary to it.
        # the **kwargs argument will then store all the variables into a dictionary.
        mathsTest(level=level, num1=num1, num2=num2, studentUserName=studentUserName,
                  prevQuestions=prevQuestions, wrongAnswer=wrongAnswer, bestResult=bestResult, question=question, bestTime=bestTime)
    except:
        studentNotFound()


def mathsTest(**student):  # bestResult
    print(student)

    """mathsTest function summary:

    This is the other part of the maths game, a timer is started whenever the function is called and the progress bar at the
    top of the program is updated by 10 (to a max of 100), and this function is called for as long as the question number is
    under 11. All current questions are moved to a list and checked for dupes via a while loop, ensuring that the student
    doesn't have to answer the same question twice.

        Args:
            student (**kwargs): this is a keyword argument defined in 
            mathGameUI allowing me to pass as many arguments as needed into mathsTest
    """

    print(student["num1"], student["num2"])
    global startTime
    # startTime is used to track how long the student takes to answer the question, it then adds the result to a list which is later
    # on used to determine how long the entire game took them.
    startTime = time()
    student["question"] += 1
    progressBar['value'] += 10

    global add_answer_button
    add_answer_button = Button(
        gameFrame, text="Answer", command=lambda: getAnswer(student, result))
    add_answer_button.pack()

    add_answer.bind(
        '<Return>', (lambda event: getAnswer(student, result)))

    if student["question"] != 11:
        questionCount = str("Question number: %d" % student["question"])
        gameLabel.config(text=questionCount)

        # Calling the calculate function to get the maths question, and concatenating the current question as I will be adding it to a list.
        a, operator, b, result = calculate(student, operatorDict)
        currentQuestion = (str(a) + ' ' + str(operator) + ' ' + str(b))

        # If the maths question is in the prevQuestions list, then we need to call the calculate function continuously until the question
        # is unique, this piece of code can get quite complicated in some scenarios. It will call the calculate function for a new question,
        # But if the new question isn't unique, or it doesn't meet the parameters set (if level != 3, then result cannot be < 0, or
        # if B > A and it's a division question.), then it has to call the function continuously until the question is unique and meets all the parameters.
        while currentQuestion in student["prevQuestions"]:
            print('dupe detected', a, operator, b)
            a, operator, b, result = calculate(student, operatorDict)
            currentQuestion = (str(a) + ' ' + str(operator) + ' ' + str(b))

        firstNumber["text"] = str(a)
        mathSign["text"] = str(operator)
        secondNumber["text"] = str(b)

        print(a, operator, b)
        print(f"Answer = {result}")  # testing

        store = (str(a) + ' ' + str(operator) + ' ' + str(b))
        student["prevQuestions"].append(store)
        print(student["prevQuestions"])

    if student["question"] == 11:
        # Calling the gameOver function with the **kwargs argument I have used to display the end game UI.
        gameOver(student)
        # Calling the storeResult function with the **kwargs argument I have used to store the result of the game.
        storeResults(student)


def calculate(student, operatorDict):
    """calculate function summary:
    This function is the heart of the maths game. When called, it calculates the question via a random range which
    is defined by the students level, and the result is stored into a variable which is then returned to the mathsTest function.

    There is some error handling in this function, namely Zero Division Errors and I have made it impossible to have any
    negative numbers for students in the levels of 2-3, alongside the removal of any division questions where the secondary
    number is greater than the first, due to the floor division used in this program.

    Returns:
        a: The first number.
        operator: The operator.
        b: the second number.
        result: The result of the equation.

    """

    try:
        # By default it will just run this block of code and return it below.
        operator = random.choice([u"\u00F7", "+", "-", u"\u00D7"])
        a = random.randrange(student["num1"], student["num2"], 1)
        b = random.randrange(student["num1"], student["num2"], 1)
        result = operatorDict[operator](a, b)

        # If the parameters of this lengthy while loop are met, then it will continuously run it.
        while result < 0 and student["level"] != 3 or operator == u"\u00F7" and result == 0:
            print("inside first negative check: ", a, operator, b, result)
            operator = random.choice([u"\u00F7", "+", "-", u"\u00D7"])
            a = random.randrange(student["num1"], student["num2"], 1)
            b = random.randrange(student["num1"], student["num2"], 1)
            print("Generating new numbers:", a, operator, b)  # Testing
            result = operatorDict[operator](a, b)

    except ZeroDivisionError:
        print("Zero division inside calculate function ",
              a, operator, b)  # testing
        # If B = 0 and operator = Division, then a ZeroDivisionError exception gets raised, this is how i handle it. I remove the division
        # operator and roll it again, with a similar while loop below to handle any more potential problems.
        a = random.randrange(student["num1"], student["num2"], 1)
        b = random.randrange(student["num1"], student["num2"], 1)
        operatorNoDiv = random.choice(["+", "-", u"\u00D7"])
        result = operatorDict[operatorNoDiv](a, b)

        while student["level"] != 3 and result < 0:
            print("Validating inside if statement", a, operator, b)  # testing
            operatorNoDiv = random.choice(["+", "-", u"\u00D7"])
            a = random.randrange(student["num1"], student["num2"], 1)
            b = random.randrange(student["num1"], student["num2"], 1)
            result = operatorDict[operatorNoDiv](a, b)

        return a, operatorNoDiv, b, result
    return a, operator, b, result


def getAnswer(student, result):
    """getAnswer function summary:

    This function is called when the student presses enter or clicks the "Answer" button. the function
    plays a sound dependant on whether or not the student got the answer correct. It also records the amount
    of incorrect answers the student has had and stores their total time into a variable via a list.
    Additionally, if the student gets the answer correct a star-struck emoji is shown, and if it is wrong a sad emoji is shown.
    some light error handling is added via the try and except method.

    Args:
        student (**kwargs): this is a keyword argument defined in mathGameUI allowing me to pass as many arguments as needed into mathsTest
        result (int): The result of the calculate function.
    """

    try:
        answer = int(add_answer.get())
        elapsedTime = time() - startTime
        timeList.append(float(elapsedTime))
        totalTime = sum(timeList)
        print(f"Total time: {totalTime:.2f} seconds")

        # Based on the answer, I create a new thread which will then play a sound file based
        # On whether the answer was correct or not, and I show the student how long it took them to answer and what the answer was.
        # I also update the emojiHolder label with an emoji via unicode.
        if answer == result:
            threading(correctAnswer)
            emojiHolder.config(text=happyFace, font=("Helvetica", 60))
            response = f"Correct! the answer was {result} and it took you {elapsedTime:.2f} seconds"
        elif answer != result:
            threading(incorrectAnswer)
            student["wrongAnswer"] += 1
            emojiHolder.config(text=sadFace, font=("Helvetica", 60))
            response = f"Wrong! the answer was {result} and it took you {elapsedTime:.2f} seconds"

        answer_message.config(text=response)
        add_answer.delete(0, END)
        # Unpacking the answer button to avoid duplication
        add_answer_button.pack_forget()
        mathsTest(level=student["level"], num1=student["num1"], num2=student["num2"], studentUserName=student["studentUserName"],
                  prevQuestions=student["prevQuestions"], wrongAnswer=student["wrongAnswer"], bestResult=student["bestResult"], question=student["question"], totalTime=totalTime, bestTime=student["bestTime"])
    except ValueError:
        add_answer_button.pack()
        messagebox.showinfo("Incorrect Input", "Please only enter numbers.")


def gameOver(student):
    """gameOver function summary:

    This function disables and unpacks the relevant widgets in order to display a game over message
    It will show how many questions the user got correct, what time they did it in and offer them to play again or
    to change user.

    Args:
        student (**kwargs): this is a keyword argument defined in mathGameUI allowing me to pass as many arguments as needed into mathsTest
    """

    # This block of code is used to display the game over screen, I also unbind the Enter key to prevent the student from
    # Breaking the game.
    prevUser.append(student["studentUserName"])
    add_answer_button["state"] = "disabled"
    add_answer["state"] = "disabled"
    firstNumber["text"] = "Game"
    mathSign["text"] = ""
    secondNumber["text"] = "Over!"
    add_answer.unbind('<Return>')
    progressBar.pack_forget()
    emojiHolder.pack_forget()
    add_answer_button.pack_forget()

    # I calculate the correct answers by subtracting the amount of wrong answers from 10.
    wrong = student["wrongAnswer"]
    correct = 10 - wrong
    time = student["totalTime"]
    response = f"You have completed the game with {correct} correct answers and {wrong} wrong answers, \nand overall it took you {time:.2f} seconds to complete"
    answer_message.config(text=response)

    global resultPlaceholder
    resultPlaceholder = Label(gameFrame, text="", font=("Helvetica", 18))
    resultPlaceholder.pack()
    global resultLabel
    resultLabel = Label(gameFrame, text="", font=("Helvetica", 18))
    resultLabel.pack()

    # I add some buttons with options for the student to choose from. I added the change user button for testing purposes.
    playAgain = Button(gameFrame, text="Play Again?", command=restart)
    playAgain.pack(side=LEFT, expand=1, fill=X)
    ChangeUser = Button(gameFrame, text="Change User", command=userChange)
    ChangeUser.pack(side=RIGHT, expand=1, fill=X)
    quitProgram = Button(gameFrame, text="Quit", command=endProgram)
    quitProgram.pack(side=TOP, expand=1, fill=X)


def storeResults(student):
    """storeResult function summary:
    This function stores the results of the math game into the result.csv file located in the same folder
    as the program, it calculates the student's score by deducting the wrong answers from 10, and then
    prints the current date and time alongside the student's score into the result.csv file. If the student got a
    new personal best, it updates the main student file.

        Args:
        student (**kwargs): this is a keyword argument defined in mathGameUI allowing me to pass as many arguments as needed into mathsTest"""

    testResult = 10 - student["wrongAnswer"]
    currentDate = date.today()
    time = datetime.now()
    studentRecords = open(
        'result.csv', 'a')

    storeTotalTime = round(student["totalTime"], 2)

    # Storing the students name, result, amount of time it took, and the current date + time.
    line = ("\n" + student["studentUserName"] + "," + str(testResult) + "," +
            currentDate.strftime("%d-%m-%Y") + "," +
            time.strftime("%H:%M:%S") + "," + str(storeTotalTime))

    print("Details added to database:",
          student["studentUserName"] + " " + str(testResult) + " " +
          currentDate.strftime("%d-%m-%Y") + " " +
          time.strftime("%H:%M:%S") + "," + str(storeTotalTime))

    studentRecords.write(line)
    studentRecords.close()

    print(student["bestTime"])

    # As I previously defined in the mathGameUI function, any noneType's in the file should indicate that
    # It is a new student, therefore I created a response based on that.
    if student["bestTime"] == None:
        response1 = f"This was your first time playing, play again to see if you can do it faster!"
    # If the student gets a new best result or a new best time, I play a cheering sound via the threading function
    # And I display a congratulations message.
    elif float(storeTotalTime) < float(student["bestTime"]):
        newPb = float(student["bestTime"]) - float(storeTotalTime)
        response1 = f"Well done! You were {newPb:.2f} seconds faster this time!"
    else:
        response1 = "Unfortunately, you weren't faster this time!"

    if student["bestResult"] != None:

        if testResult > student["bestResult"]:
            response2 = f"\nCongratulations, You got a new Personal best of {testResult}. keep it up!"
            response = str(response1) + str(response2)
            # Opening the updateBestResult function if the student got a new
            updateBestResult(student["studentUserName"], testResult, response)
        elif testResult == int(student["bestResult"]):
            response2 = f"\nThis time you tied your personal best of {testResult}!"
            response = str(response1) + str(response2)
            resultPlaceholder.config(text=response)
        else:
            response2 = "\nUnfortunately, you didn't get a new personal best, but keep trying!"
            response = str(response1) + str(response2)
            resultPlaceholder.config(
                text=response)

    else:
        # This code is ran if the student is new.
        response2 = f"\nThis was your first time playing and your score was: {testResult}!"
        response = str(response1) + str(response2)
        # I open the updateBestResult function as they are a new student and no matter their score it will be a personal best.
        updateBestResult(student["studentUserName"], testResult, response)


def threading(outputFile):
    """threading function summary:

    Args:
        outputFile (variable): Chooses the sound file to play
    """

    t1 = Thread(target=outputFile)
    t1.start()

# These three functions play a sound dependant on the outcome of the current game.


def correctAnswer():
    os.system("afplay " + chimeFile)


def incorrectAnswer():
    os.system("afplay " + buzzFile)


def newPB():
    os.system("afplay " + pbFile)

# If the user wants to change to a different student, this deletes the saved
# username, destroys the game window and shows the login window.


def userChange():
    main_screen.deiconify()
    studentLoginScreen.deiconify()
    gameUI.destroy()
    username_entry.delete(0, END)


def restart():
    gameUI.destroy()
    mathGameUI()


def updateBestResult(login, result, response):
    """updateBestResult function summary:
    This function updates the users best result if they got a new personal best and plays a sound."""

    threading(newPB)
    editFiles("UserName", login, "BestResult", result, resultLabel)
    resultPlaceholder.config(
        text=response)
    resultLabel.config(text="")


def passwordNotFound():
    """passwordNotFound summary:

    This function displays a small window informing the user that they have entered the wrong teacher
    username or password, and that they need to try again.

    """

    global teacherNotFoundScreen
    teacherUserEntry.delete(0, END)
    teacherPasswordEntry.delete(0, END)
    teacherNotFoundScreen = Toplevel(login_screen)
    teacherNotFoundScreen.title("Error")
    teacherNotFoundScreen.geometry("200x100")
    Label(teacherNotFoundScreen,
          text="Invalid username or Password").pack(pady=20)
    Button(teacherNotFoundScreen, text="OK",
           command=teacherNotFound).pack()


def editFiles(storedUser, login, old, new, label):
    """editFiles function summary:

    uses the fileinput import module to edit the files in-place by searching for the specified user
    and then editing the data defined by "old"

    Args:
        storedUser (String): The current user
        login (String): The login of the current user to validate the data
        old (String): The row to edit
        new (String): The new information to edit to the row
        label (String): I left this here to update an empty label if needed. This is used in the CheckProgress function"""

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
    """studentNotFound function summary:

    This function displays a small window informing the user that they have entered the wrong student
    username, and that they need to try again."""

    global studentNotFoundScreen
    studentNotFoundScreen = Toplevel(studentLoginScreen)
    studentNotFoundScreen.title("Error")
    studentNotFoundScreen.geometry("150x100")
    Label(studentNotFoundScreen, text="User Not Found").pack(pady=20)
    Button(studentNotFoundScreen, text="OK",
           command=deleteStudentNotFound).pack()
    studentNotFoundScreen.bind(
        '<Return>', (lambda event: deleteStudentNotFound()))

# These functions destroy windows.


def teacherNotFound():
    teacherNotFoundScreen.destroy()


def deleteStudentNotFound():
    username_entry.delete(0, END)
    studentNotFoundScreen.destroy()


def endProgram():
    main_screen.destroy()


def main():
    """main function summary:
    This function shows the main screen where the user can choose between teacher or student."""

    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("EduSoft Menu")
    Label(text="Please choose from the menu.", width="300",
          height="2", font=("Calibri", 18)).pack()
    Label(text="").pack()
    Button(text="Teacher", height="2", width="30", command=teacherLogin).pack()
    Label(text="").pack()
    Button(text="Student", height="2", width="30", command=studentLogin).pack()
    main_screen.mainloop()


print(gameOver.__doc__)

if __name__ == '__main__':
    main()

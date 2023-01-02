from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import csv
question = 0

# Designing window for registration


def student():
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
    tabControl.add(tab5, text='Manage Student')
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
           command=lambda: studentSearch(str(fNameEntry.get()), lNameEntry.get())).grid(row=4, column=0,
                                                                                        sticky="NWSE")
    Button(tab3, text="Grab Student Details",
           command=studentDetails).grid(row=5, column=0, sticky="NWSE")
    Button(tab3, text="Delete Student",
           command=deleteStudent).grid(row=4, column=1, sticky="NWSE")


def studentSearch(first, last):
    global studentPath
    studentPath = '/Users/jake/College/college-software-solution/student.csv'
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
    userNameLabel = Label(tab3, text="Username").grid(
        row=6, column=0, sticky="NWSE", padx=1)
    firstNameLabel = Label(tab3, text="First Name").grid(
        row=7, column=0, sticky="NWSE", padx=1)
    lastNameLabel = Label(tab3, text="Last Name").grid(
        row=8, column=0, sticky="NWSE", padx=1)
    levelLabel = Label(tab3, text="Level").grid(
        row=9, column=0, sticky="NWSE", padx=1)
    codeLabel = Label(tab3, text="Code").grid(
        row=10, column=0, sticky="NWSE", padx=1)
    bestResultLabel = Label(tab3, text="Best Result").grid(
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
    global add_answer
    global answer_message
    global num1
    global num2
    var = StringVar()
    username_info = username.get().upper()
    username_info = "TIMJ"
    if username_info != "TimJ".upper():
        quit()

    mes1 = "Hello "
    mes2 = "Tim Jones, Your last score was: 7 and your best was: 10"
    mes3 = mes1 + mes2
    messagebox.showinfo("User Information", mes3)

    gameUI = Toplevel(main_screen)
    gameUI.title("Math Game")
    gameUI.geometry("700x700")
    gameFrame = Frame(gameUI, width=500, height=500)
    gameFrame.pack(fill="both", expand=1)
    gameLabel = Label(gameFrame, text="Math Flashcards!",
                      font=("Helvetica", 18)).pack(pady=15)
    mathFrame = Frame(gameFrame, width=400, height=300)
    mathFrame.pack()

    num1 = random.randrange(0, 10)
    num2 = random.randrange(0, 10)

    firstNumber = Label(mathFrame, font=("Helvetica", 28))
    secondNumber = Label(mathFrame, font=("Helvetica", 28))
    math_sign = Label(mathFrame, text="+", font=("Helvetica", 28))

    firstNumber["text"] = str(num1)
    secondNumber["text"] = str(num2)
    # Grid our labels
    firstNumber.grid(row=0, column=0)
    math_sign.grid(row=0, column=1)
    secondNumber.grid(row=0, column=2)
    # Create answer box and button
    add_answer = Entry(gameFrame, font=("Helvetica", 18))
    add_answer.pack(pady=30)

    add_answer_button = Button(gameFrame, text="Answer", command=gameTest)
    add_answer_button.pack()

    answer_message = Label(
        gameFrame, text="The answer was: ", font=("Helvetica", 18))
    answer_message.pack(pady=30)


def gameTest():
    global question
    num1 = random.randrange(0, 10)
    num2 = random.randrange(0, 10)
    firstNumber["text"] = str(num1)
    secondNumber["text"] = str(num2)
    question += 1
    print(question)


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised).pack()

# Designing popup for user not found


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()

# Deleting popups


def delete_login_success():
    login_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Please log in.", width="300",
          height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Teacher", height="2", width="30", command=teacherLogin).pack()
    Label(text="").pack()
    Button(text="Student", height="2", width="30", command=student).pack()
    main_screen.mainloop()


main_account_screen()

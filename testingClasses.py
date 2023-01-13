from tkinter import *


class Menu:
    def launchHello(self):
        print("Hello!")

    def launchBye(self):
        print("Bye")

    def __init__(self):
        self.menu_form = Tk()
        self.menu_form.title("Example Menu")
        self.menu_form.geometry("500x200")
        self.lbl = Label(self.menu_form, text="My Menu")
        self.lbl.pack()

        pixelVirtual = PhotoImage(width=1, height=1)
        self.btn_launchHello = Button(self.menu_form, text="Hello", image=pixelVirtual,
                                      width=120, height=50, compound="c", command=self.launchHello)
        self.btn_launchHello.pack()
        self.btn_launchBye = Button(self.menu_form, text="Bye", image=pixelVirtual,
                                    width=120, height=50, compound="c", command=self.launchBye)
        self.btn_launchBye.pack()

        self.menu_form.mainloop()


Menu()

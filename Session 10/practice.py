#Tinker

from tkinter import*
from tkinter import messagebox

window = Tk()

def popIpMassageBox():
    print("username " + usernameValue)
    print("username " + passwordValue)

def validateInfo(username, psw):
    if (username == "mindx")
window.geometry("800x600")
window.title("From Sign In/Sign Up")

gretting = Label(text="Welcome to my app", bg="red")
gretting.gride(row=0, column=5)
btnSignIn = Button(text="Sign in", bg="green", padx="16", pady="8", command=popUpMessageBox)

userLabel = Label(text = "username")

userLabel.grid(row=1, column=0)
userInput = Entry()
userInput.grid(row=1, column=1)

usernameValue = userInput.get()

passLabel = Label(text="password")

passLabel.grid(row=2, column=0)
passInput = Entry(show="*")
passInput.grid(row=2, column=1)

passwordValue = passInput.get()

btnSignIn.grid(row=3, column=12)
window.mainloop()
# TKinter



from tkinter import *
from tkinter import messagebox
# giong voi turtle (from turtle import *)
window = Tk()


def popUpMessageBox():
    print('username ' + usernameValue)
    print('password ' + passwordValue)

def validateInfo():
    username = userInput.get()
    psw = passInput.get()
    if (username == 'mindx'):
        if (psw == '1234'):
            outputlabel = Label(text="success")
            outputlabel.grid(row=3, column=0)
        else:
            outputlabel = Label(text="wrong")
            outputlabel.grid(row=3, column=0)

window.geometry("800x600")
window.title('Form Sign In/Sign Up')

gretting = Label(text="Welcome to my app", bg="red")
gretting.grid(row=0, column=5)

btnSignIn = Button(text="Sign in", bg="green", padx="16", pady="8", command=lambda: [validateInfo()])

userLabel = Label(text = "username")

userLabel.grid(row=1, column=0)
userInput = Entry()
userInput.grid(row=1, column=1)

passLabel = Label(text="password")

passLabel.grid(row=2, column=0)
passInput = Entry(show="*")
passInput.grid(row=2, column=1)






btnSignIn.grid(row=3, column=12)
window.mainloop()







# This is an attempt at a GUI

#from tkinter import *
#import tkinter.messagebox
# This is a basic login screen
#https://www.youtube.com/watch?v=iCK8adSeG7A


'''

def Login(self):    #define the login screen
    window = Tk() #constructor, blank window
    window.title("FTP")
    window.geometry("460x260") # size of the inital window
    #Creating Login in layout

    userText = Label(window, text="Username:")
    passText = Label(window, text="Password:")

    #setting the layout
    userText.grid(row=1, column=0, sticky=W)
    passText.grid(row=2, column=0, sticky=W)

    userInput = Entry(window)
    passInput = Entry(window, show='*')

    userInput.grid(row=1, column=1)
    passInput.grid(row=2, column=1)

   # loginButton = Button(window, text="Login")
    loginButton = Button(window, text="Login", command=self.login_button_click) # check for login when button clicked
    loginButton.grid(columnspan=2, sticky=W)
    window.mainloop() #runs the window


def login_button_click(self):
    username = self.userInput.get() #get the username from the textbox
    password = self.passInput.get() #get the password from the textbox

    if username == 'admin' and password == 'admin':
        #window.destory() #destroy the login window to open the new window
        tkinter.messagebox.showinfo('YOu are logged in')
    else:
        tkinter.messagebox.showerror('Incorrect details')
################################################################################
# Main ###

Login(self)
'''


################################################################################
# This code is similar to what i want to do, however it displays a messagebox rather than
# opens a new window
''' 
class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_username = Label(self, text="Username")
        self.label_password = Label(self, text="Password")

        self.entry_username = Entry(self)
        self.entry_password = Entry(self, show="*")

        self.label_username.grid(row=0, sticky=E)
        self.label_password.grid(row=1, sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.entry_password.grid(row=1, column=1)

        self.checkbox = Checkbutton(self, text="Keep me logged in")
        self.checkbox.grid(columnspan=2)

        self.logbtn = Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "john" and password == "password":
            tkinter.messagebox.showinfo("Login info", "Welcome John")
        else:
            tkinter.messagebox.showerror("Login error", "Incorrect username")


root = Tk()
lf = LoginFrame(root)
root.mainloop()
'''
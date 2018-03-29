import sys 
from ftplib import FTP
import Tkinter as tk
import tkFileDialog
import os


#import Tkinter as ttk
root = tk.Tk()
root.title('ELEN4017 FTP Server')
root.geometry('980x640')

# create all of the main containers
top_frame =tk.Frame(root, width=450, height=50, pady=3)
clientFrame = tk.Frame(root, bg='blue', width=480, height=400)
serverFrame = tk.Frame(root, bg='green', width=480,height=400)
responseFrame = tk.Frame(root, bg='black', width=480, height=200)
#btm_frame = tk.Frame(root, bg='pink', width=450, height=45, pady=3)
#btm_frame2 = tk.Frame(root, bg='lavender', width=450, height=60, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
clientFrame.grid(row=2, sticky="sw")
serverFrame.grid(row=2, sticky="se")
responseFrame.grid(row=1, sticky='ew')
#btm_frame.grid(row=3, sticky="ew")
#btm_frame2.grid(row=4, sticky="ew")

# ----------------------------------------------- TOP FRAME ------------------------------------------------------------------------
# create the widgets for the top frame
hostName = tk.Label(top_frame, text="Host:")
userText = tk.Label(top_frame, text="Username:")
passText = tk.Label(top_frame, text="Password:")
portNumber = tk.Label(top_frame, text="Port:")
connectButton = tk.Button(top_frame, text="Connect")

hostInput = tk.Entry(top_frame)
userInput = tk.Entry(top_frame)
passInput = tk.Entry(top_frame)
portNumberInput = tk.Entry(top_frame)


# layout the widgets in the top frame
hostName.grid(row=1,column=0)
hostInput.grid(row=1,column=1)
userText.grid(row=1,column=2)
userInput.grid(row=1,column=3)
passText.grid(row=1,column=4)
passInput.grid(row=1,column=5)
portNumber.grid(row=1,column=6)
portNumberInput.grid(row=1,column=7)
connectButton.grid(row=1,column=8)

# -------------------------------------------------------------------------------------------------------------------------------

# create the center widgets
#center.grid_rowconfigure(0, weight=1)
#center.grid_columnconfigure(1, weight=1)

# ----------------------------- Positioning the Base Frames --------------------------------------------------------------------
clientFrame.grid_rowconfigure(0, weight=1)
clientFrame.grid_columnconfigure(1, weight=1)

serverFrame.grid_rowconfigure(0, weight=1)
serverFrame.grid_columnconfigure(2, weight=1)

responseFrame.grid_rowconfigure(0, weight=1)
responseFrame.grid_columnconfigure(1, weight=1)

# -----------------------------------------------------------------------------------------------------------------------------
# ------------------------------------- Widgets for Server Response -----------------------------------------------------------
# creating a scroll bar
#l = tk.Listbox(responseFrame, height=5)
#l.grid(column=0, row=0, sticky='nwes')
#responseScroll = tk.Scrollbar(responseFrame, command=l.yview)
#responseScroll.grid(column=1, row=0, sticky='ns')
#l.yscrollcommand = responseScroll.set

# -----------------------------------------------------------------------------------------------------------------------------



# ------------------------------------- Widgets for Client Frame --------------------------------------------------------------


# -----------------------------------------------------------------------------------------------------------------------------
#ctr_left = tk.Frame(center, bg='blue', width=100, height=190)
#ctr_mid = tk.Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
#ctr_right = tk.Frame(center, bg='green', width=100, height=190, padx=3, pady=3)

#ctr_left.grid(row=0, column=0, sticky="ns")
#ctr_mid.grid(row=0, column=1, sticky="nsew")
#ctr_right.grid(row=0, column=2, sticky="ns")

root.mainloop()


'''
class App(tk.Tk):    
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid()
        self.geometry("980x640")
        self.title("ELEN4019 FTP Server")
       # self.Appbutton = tk.Button(text='Choose a File to Upload', command = self.launch_file_dialog_box).pack()
       # self.Appbutton_FTP = tk.Button(text='Upload File to FTP Server', command =  self.upload_file_to_FTP).pack()
        self.hostName = tk.Label(text="Host:").grid(row=1, column=0)
        self.userText = tk.Label(text="Username:").grid(row=1, column=2)
        self.passText = tk.Label(text="Password:").grid(row=1, column=4)
        self.portNumber = tk.Label(text="Port:").grid(row=1, column=6)

        self.hostName = tk.Entry().grid(row=1, column=1)
        self.userInput = tk.Entry().grid(row=1, column=3)
        self.passInput = tk.Entry().grid(row=1, column=5)
        self.portNumber = tk.Entry().grid(row=1, column=7)
        self.connectButton = tk.Button(text="Connect").grid(row=1,column=8)

        self.clientFrame = tk.Frame(self, bg='cyan', width=640, height = 50, pady=3)


    def launch_file_dialog_box(self):
        self.raw_filename = tkFileDialog.askopenfilename()



    def upload_file_to_FTP(self):
    ##    first thing we do is connect to the ftp host        
            ftp = FTP('')
            ftp.login( user = '', passwd='')
            ftp.cwd("")
            ftp.set_pasv(False)
            file_name = self.raw_filename
            file = open(file_name, 'rb')
            ftp.storbinary('STOR ' + file_name, file)
            file.quit()
app = App()
app.mainloop()
'''
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
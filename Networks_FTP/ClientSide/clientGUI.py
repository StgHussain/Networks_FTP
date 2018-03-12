from tkinter import *

# This is a basic login screen
#https://www.youtube.com/watch?v=iCK8adSeG7A

window = Tk() #constructor, blank window
window.title("FTP")


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

loginButton = Button(window, text="Login")
loginButton.grid(columnspan=2, sticky=W)


window.mainloop() #infinite loop till close is pressed



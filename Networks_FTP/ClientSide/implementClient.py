import socket
import os   # allows for using operating system dependent functionality
import sys  # system-specific parameters and functions

#def TYPE():     # refers to the ASCII Non-print

class FTPClient():

    def __init__(self, server='', user='', password=''):
        
        self.login(user, password) # user has to login
        #if server:
        #    self.connectServer(server) # connects the server 
        #if user:
        #    self.login(user, password) # user has to login

    def login(self, user, password):        
        user = raw_input('Username: ')
        if user == 'admin':
            print('331 Password is required to access account ', user)
        else: 
            self.login(user, password)

        password = raw_input('Password: ') # gets the password
        if password == 'admin':
            print('\n 230 Logged in Successful')
           # self.changeWorkDir()
        else: 
            print('\n Password invalid, please retry login')
            self.login(user, password)


    def connectServer(self, server):
        print('220 You have been connected to the SERVER!\n Please input username and password.\n')

    def changeWorkDir(self, name):   # using os to change the directory
        #if name == '..': # the .. will allow the user to go back

        name = ''
        terminal = 'cwd' + name
        return os.getcwd(terminal) # returns the current working directory

    def listDir(self): # list files in the directory
        
        return os.listdir()

rrun = FTPClient()

#minimum implementation
'''
TYPE - ASCII Non-print
MODE - Stream
STRUCTURE - File, Record
COMMANDS - USER, QUIT, PORT,
            TYPE, MODE, STRU,   
            for all default values
            RETR, STOR,
            NOOP
The default values for transder parameters are:

    TYPE - ASCII Non-print
    MODE - Stream
    STRU - File
'''

# client must use binary transfers
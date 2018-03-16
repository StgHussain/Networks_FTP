import socket
import os   # allows for using operating system dependent functionality
import sys  # system-specific parameters and functions


'''
(ELEN4017.ug.eie.wits.ac.za)

Username: group4

Password: dae3Uiwa
'''


#def TYPE():     # refers to the ASCII Non-print

#class FTPClient():

  #  def __init__(self, server='', user='', password=''):
        
   #     self.login(user, password) # user has to login
        #if server:
        #    self.connectServer(server) # connects the server 
        #if user:
        #    self.login(user, password) # user has to login
# Assuming the login works correctly with the server
def login():   

    user = raw_input('Username: ')
    password = raw_input('Password: ')    
   
    serverName = 'ELEN4017.ug.eie.wits.ac.za'
    #serverName = 'ftp://mirror.ac.za/'
    serverPort = 21 # normal FTP port 
    flag = False   # using flag to test if connection is made to the server
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((serverName, serverPort))
        serverResp = clientSocket.recv(2048)
        clientSocket.send(raw_input("client enter: "))

    except:
        flag = True
        print '\n __________________Unable to connect to Server ______________________ \n'
            
    if not flag:
        try:
            authLogin = 'login ' + user + ' ' + password + '\n'
            clientSocket.send(authLogin)
            serverResp = clientSocket.recv(2048)

        except:
            flag = True
            print '\n __________________________Login details are incorrect _____________________________________\n'
        if not flag:
            print '\n ______________________________Connection to the server was Successful ___________________________________ \n'
        return clientSocket, flag # return the socket and the status of the flag
            
            
            
            
''' user = raw_input('Username: ')
            if user == 'group4':
                print('Password is required to access account ', user)
            else: 
                self.login(user, password)

            password = raw_input('Password: ') # gets the password
            if password == 'dae3Uiwa':
                print('\n 230 Logged in Successful')
            # self.changeWorkDir()
            else: 
                print('\n Password invalid, please retry login')
                self.login(user, password) '''
    

        
# These functions allow the user to move between files on the client/server side
# ------------------------------------------------------------------------------
   
def getCWD():   # using os to change the directory
        #if name == '..': # the .. will allow the user to go back
    rootPath = "" #set a default path
    currentDir = os.getcwd()
    print 'Currently in working directory %s' % currentDir

    return currentDir
    #name = '' #name is the name of the directory
    #terminal = 'cwd' + name
    #return os.getcwd(terminal) # returns the current working directory

def changeCWD():
    path = getCWD()
    changeDir = os.chdir(path)
    print 'Currently in working directory %s' % changeDir
    


def listDir(): # list files in the directory
    
    files = os.listdir(getCWD())
    print '\n _______ List of Files _______\n'
    for file in files:
        print file
    change = raw_input("To change working directory, use cd (name). ")
#changeCWD()
    
    

listDir()
#run = login()
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
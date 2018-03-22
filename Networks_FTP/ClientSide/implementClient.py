import socket
import os   # allows for using operating system dependent functionality
import sys  # system-specific parameters and functions

# www.rhyshaden.com/ftp.htm

'''
(ELEN4017.ug.eie.wits.ac.za)

Username: group4

Password: dae3Uiwa
'''
class FTPClient():

    def __init__(self, serverName, user, password):
        self.serverPort = 21 # default FTP server port
        self.serverName = serverName # 'ELEN4017.ug.eie.wits.ac.za'
        #self.serverName = 'ftp://mirror.ac.za/'
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initiate the client socket
        self.clientSocket.connect((self.serverName, self.serverPort))
        self.isBinaryFile = False # check to see if the file is binary
        self.login(user, password) # user has to login
        self.defaultDirectory = os.path.abspath('./Documents/Wits 4th Year/Semester 1/Networks/Project/')
        print 'The default directory is: ', self.defaultDirectory

    # Receive the response from the server
    def serverResponse(self):
        response = self.clientSocket.recv(2048)
        print '\n Server Response: ', response

    # login to the server
    def login(self, user = '', password = ''):   
        
        #serverName = 'ftp://mirror.ac.za/'
        #serverPort = 21 # normal FTP port 
        
        response = self.serverResponse()
        user = raw_input('Username: ')
        self.USER(user)
        
        password = raw_input('Password: ')    
        self.PASS(password)
        
        #self.PORT(self.serverName, self.serverPort)
        
    # Access control commands for minimal implementation
    # ----------------------------------------------------- 
    def USER(self, user):
        # required for access to the file system
        # send the username to the server
        self.clientSocket.send('USER '+ user + '\r\n') # '\r\n' needed as it is for 
        self.serverResponse()

    def PASS(self, password):
        # send the password to the server 
        
        self.clientSocket.send('PASS ' + password  + '\r\n')
        self.serverResponse()   

    # Not part of minimal implementation
    '''
    def ACCT(self, account):
        # send the account details to the server
        self.clientSocket.send(account)
        self.serverResponse()    
    '''
    def CWD(self, wd):
        # change working directory
        self.clientSocket.send('CWD ' + wd + '\r\n')
        self.serverResponse()

    # need to test this
    def QUIT(self, user):
        # terminates the user and closes server if no transfer is taking place
        # shutdown() shutsdown one or both halves of the connection
        self.clientSocket.send('QUIT ' + user + '\r\n')
        self.clientSocket.shutdown(user)
        self.serverResponse()

    # Transfer parameter commands
    # ----------------------------------------------------------
    
    def PORT(self, hostAddress, portAddress):
        # data PORT for data connection
        # normal circumstances this is not needed
        # this is for ACTIVE mode
        # address information is broken into 8-bit fields then into decimal form
        # PORT h1,h2,h3,h4,p1,p2 where h1 is high order 8 bits 
        splitHostAddress = hostAddress.split('.') # split the ip at each . # host address is 32 bit size
        splitPortAddress = [repr(portAddress//256), repr(portAddress % 256)] # port is 16 bit size

        # Create new ACTIVE MODE socket and send PORT command 
        self.activeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.activeSocket.bind((hostAddress, portAddress))
        self.activeSocket.listen(1)       
        self.clientSocket.send('PORT ' + ','.join(splitHostAddress + splitPortAddress)  + '\r\n')
        print 'ACTIVE MODE connection created.'
        self.serverResponse()


    def TYPE(self, fileType):
        # transfer byte size is always 8 bits
        if fileType.endswith('.txt'):
            self.isBinaryFile = False
            self.clientSocket.send(' File TYPE A \n')
            # TYPE A refers to ASCII
        else:
            self.isBinaryFile = True
            self.clientSocket.send(' File TYPE I \n')
            # TYPE I refers to Image
    
    def STRU(self, fileStructure):
        # specifies file structure
        # F - File (no record structure) - Default
        # R - Record structure
        # P - Page structure
        self.clientSocket.send('STRU ' + fileStructure + '\r\n') # send file structure to the server and get reply
        self.serverResponse()

    def MODE(self, dataMode):
        # specifies data transfer modes
        # S - Stream - Default
        # B - Block
        # C - Compressed
        self.clientSocket.send('MODE ' + dataMode + '\r\n') # send data transfer mode and get a reply
        self.serverResponse() 

# PASV requests the server-DTP to "listen " on a data port and wait for connection
# Passive data connection

    # FTP Service Commands
    # -----------------------------------------------------------
    def RETR(self, copyFile, blocksize = 8192): #DOWNLOAD
        # https://stackoverflow.com/questions/29110620/how-to-download-file-from-local-server-in-python
        # transfer a copy of the file to the server
        # blocksize is the max number of bytes to read from the socket at a time
        self.clientSocket.send('RETR ' + copyFile + '\r\n')
        copyFilePath = os.path.join(os.getcwd(),copyFile)
        # joins the paths of the current wd with the coppied file
        if self.isBinaryFile:
            with open(copyFilePath, 'wb') as file_to_write:
                while True:
                    print 'You are downloading!'
                    data = self.clientSocket.recv(blocksize)
                    if not data:
                        break
                    file_to_write.write(data)
                file_to_write.close()
        else:
            print 'File is not binary'
            copyFile = open(copyFilePath, 'w') # w is write
            
        print 'Download Complete!'
        self.clientSocket.shutdown() # close the connection
        
        # Additional method to download/recieve a file
        '''
        with open('recieved file', 'wb') as f:
            print 'The file has been opened'
            while True:
                print 'Recieving file..'
                data = self.clientSocket.recv(blocksize)
                print ('data = %s', data)
                if not data:
                    f.close()
                    print 'The file has been closed'
                    break
                f.write(data) # write the data to the file

        print 'Upload Complete!'
        self.clientSocket.shutdown() # close connection
        '''

    def STOR(self, uploadFile, blocksize = 8192): #UPLOAD
        #http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
        # accepts data transfer and store the file at server site
        # if pathname exists, file is overwritten at server
        # else new file is stored
        uploadSocket = socket.socket(socket.AF_INET, socket.sock_STREAM) # open a new socket for uploading the file
        uploadSocket.connect((self.))
        uploadFilePath = os.path.join(self.defaultDirectory(os.path.realpath(__file__)), uploadFile)
        
        if os.path.exists(uploadFilePath):
            print 'Attempting to upload a file'
            self.clientSocket.send('STOR ' + uploadFile + '\r\n')
        else:
            print ' Not Found '
            return
        
        
        print ' loool '
        if self.isBinaryFile:
            fileToRead = open(uploadFilePath, 'rb') # read binary
        else:
            fileToRead = open(uploadFilePath, 'r')

        if os.path.exists(uploadFilePath):
            fileUpload = fileToRead.read(blocksize)

            while fileUpload:
                print 'File is uploading..'
                self.clientSocket.send(fileUpload)     
            # the file must be overwritten
            fileToRead.close() # close the file
            self.clientSocket.shutdown()
            self.serverResponse()
            print 'Upload Complete!'
        else: 
            print 'File path does not exist' # thus create new       
            # the new file must be stored
        

    def NOOP(self):
        # does nothing, but gets a 200 OK from the server
        self.clientSocket.send('NOOP \r\n')
        self.serverResponse()

        
# These functions allow the user to move between files on the client/server side
# ------------------------------------------------------------------------------
'''  
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
'''

#run = FTPClient()
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
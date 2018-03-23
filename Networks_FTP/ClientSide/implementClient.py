import socket
import os   # allows for using operating system dependent functionality
import sys  # system-specific parameters and functions

# www.rhyshaden.com/ftp.htm


class FTPClient():

    def __init__(self, serverName, user, password):
        self.serverPort = 21 # default FTP server port
        self.serverName = serverName # 'ELEN4017.ug.eie.wits.ac.za'
        #self.serverName = 'ftp://mirror.ac.za/'
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #initiate the client socket
        self.clientSocket.connect((self.serverName, self.serverPort))
        self.isBinaryFile = False # check to see if the file is binary
        self.login(user, password) # user has to login
        self.defaultDirectory = os.path.abspath('.')
        print 'The default directory is: ', self.defaultDirectory
        self.isPassiveMode = False # set passive mode to false
        self.passiveIP =self.serverName
        self.passivePORT = self.serverPort

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
    def USER(self, user):# works
        # required for access to the file system
        # send the username to the server
        self.clientSocket.send('USER '+ user + '\r\n') # '\r\n' needed as it is for 
        self.serverResponse()

    def PASS(self, password): # works
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

    def CDUP(self):
        self.clientSocket.send('CDUP \r\n')
        self.serverResponse()

    # need to test this
    def QUIT(self): # works
        # terminates the user and closes server if no transfer is taking place
        # shutdown() shutsdown one or both halves of the connection
        self.clientSocket.send('QUIT \r\n')
        #self.clientSocket.shutdown()
        self.serverResponse()

    # Transfer parameter commands
    # ----------------------------------------------------------
    
    def PORT(self, hostAddress, portAddress): # works
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
        #print 'ACTIVE MODE connection created.'
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
    
    def STRU(self, fileStructure): # default works
        # specifies file structure
        # F - File (no record structure) - Default
        # R - Record structure
        # P - Page structure
        self.clientSocket.send('STRU ' + fileStructure + '\r\n') # send file structure to the server and get reply
        self.serverResponse()

    def MODE(self, dataMode): # default works
        # specifies data transfer modes
        # S - Stream - Default
        # B - Block
        # C - Compressed
        self.clientSocket.send('MODE ' + dataMode + '\r\n') # send data transfer mode and get a reply
        self.serverResponse() 

    def PASV(self):
        # PASV requests the server-DTP to "listen " on a data port and wait for connection
        # Passive data connection
        self.clientSocket.send('PASV \r\n')
        # Server correctly enters passive mode
        passiveResponse = self.clientSocket.recv(1024)
        print 'response: ', passiveResponse
        # need to use the ip sent back from the server
        # however server sends back a lot of extra stuff
        # thus need to manipulate only a section of the data in the string
        # the numbers between the brackets are the IP and PORT
        firstBracket = passiveResponse.find('(') # find first bracket
        lastBracket = passiveResponse.find(')') # find last bracket
        betweenBrackets = passiveResponse[firstBracket+1:-(len(passiveResponse) - lastBracket)]
        getIP = betweenBrackets.split(',')
        self.passiveIP = '.'.join(getIP[:4])

        uPort = int(getIP[4]) # take the 4th and 5th entries to form the Port
        lPort = int(getIP[5]) # of the passive mode connection
        self.passivePORT =256*uPort + lPort

        print 'Passive connection server address %s:%u\n' % (self.passiveIP,self.passivePORT)

        self.isPassiveMode = True # set the passive mode to be true

    # FTP Service Commands
    # -----------------------------------------------------------
    def RETR(self, copyFile, blocksize = 8192): #DOWNLOAD
        # https://stackoverflow.com/questions/29110620/how-to-download-file-from-local-server-in-python
        # transfer a copy of the file to the server
        # blocksize is the max number of bytes to read from the socket at a time
        self.clientSocket.send('RETR ' + copyFile + '\r\n')
        copyFilePath = os.path.join(os.getcwd(),copyFile)
        # joins the paths of the current wd with the coppied file
        #if os.path.exists(copyfilePath):

        #    with open(copyFilePath, 'wb') as file_to_write:
        #        while True:
        #            print 'You are downloading!'
        #            data = self.clientSocket.recv(blocksize)
        #            if not data:
        #                break
        #            file_to_write.write(data)
        #        file_to_write.close()
        #else:
        #    print 'file does not exist on server'
        #print 'File is not binary'
        #copyFile = open(copyFilePath, 'w') # w is write
            
        #print 'Download Complete!'
        #self.clientSocket.shutdown() # close the connection
        
        # Additional method to download/recieve a file
        
        with open(copyFile, 'wb') as f:
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

        print 'Download Complete!'
        self.clientSocket.shutdown() # close connection
        

    def STOR(self, fileName): #UPLOAD
        #http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
        # accepts data transfer and store the file at server site
        # if pathname exists, file is overwritten at server
        # else new file is stored
        '''
        filePath = os.path.join(self.defaultDirectory, fileName)
        
        if os.path.exists(filePath):
            self.clientSock.send('STOR '+fileName +'\r\n')
        else:
            print 'File not found'
            return
        print 'here?'
       # if self.calledPortPasv == False:
        #    self.getReply()
         #   return

        self.createSocket()
        
        if self.isBinaryFile:
            requestedFile = open(filePath,'rb')
        else :
            requestedFile = open(filePath,'r')
            
        fileChunk = requestedFile.read(1024)

        while fileChunk:
            print 'Sending...'
            self.newSocket.send(fileChunk)
            fileChunk = requestedFile.read(1024)

        requestedFile.close()
        self.closeSocket()

        print "Done Sending"

        response = self.clientSocket.recv(1024)
        print response

        if response[:3] == '226':
            return
        elif response[:3] == '550':
            print 'File trainsfer failed'
        else:
            print 'Unknown transfer error occured'
            self.serverResponse()
        '''
        # RUNS WITHOUT ERRORS, HOWEVER DOES NOT ACTUALLY UPLOAD
        print 'the fuck?'
        filePath = os.path.join(self.defaultDirectory, uploadFile)
        print filePath

        self.clientSock.send('STOR '+ uploadFile +'\r\n')
        print os.getcwd()
        
        toUpload = open(uploadFile, 'rb')
        self.createSocket()
        print 'File has been opened.'
        data = toUpload.read(1024)
        print 'Data is being read'
        while (data):
            print 'Sending...'
            self.newSocket.send(data)
            print ' Socket created'
            data = toUpload.read(1024)
            print ' Data is reading in...'
            if not data:
                break
        print 'Upload complete'    
        toUpload.close() 
        self.closeSocket() 
        return
        
        '''
        if os.path.exists(uploadPath):
            self.clientSocket.send('STOR ' + uploadFile + '\r\n')
        else:
            print ' Unable to locate file'
            return
        
        print ' File found '
        # open a new socket for uploading
        #uploadSocket = socket.socket(socket.AF_INET, socket.sock_STREAM) # open a new socket for uploading the file
        #uploadSocket.connect((self.serverName,self.serverPort))   
        print 'Connection has been established'
        '''

        '''
        while True:
            
            cmd = uploadSocket.recv(32)

            if cmd == 'getFileName':
                print ' getFileName recieved '
                uploadFile.sendall(uploadFile)
            
            if cmd == 'getFile':
                print ' getFile recieved. Sending file...'
                with open(uploadFile, 'rb') as f:
                    data = f.read()
                uploadSocket.sendall(data)
                print 'File uploaded'

            uploadSocket.shutdown()
            

        
        uploadFilePath = os.path.join(self.defaultDirectory(os.path.realpath(__file__)), uploadFile)
        print 'the upload path', uploadFilePath

        if os.path.exists(uploadFilePath):
            print 'Attempting to upload a file'
            self.uploadSocket.send('STOR ' + uploadFile + '\r\n')
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
                self.uploadSocket.send(fileUpload)     
            # the file must be overwritten
            fileToRead.close() # close the file
            self.uploadSocket.shutdown()
            self.serverResponse()
            print 'Upload Complete!'
        else: 
            print 'File path does not exist' # thus create new       
            # the new file must be stored
        '''
        
    def NOOP(self):
        # does nothing, but gets a 200 OK from the server
        self.clientSocket.send('NOOP \r\n')
        self.serverResponse()

        
# These functions allow the user to move between files on the client/server side
# ------------------------------------------------------------------------------
    def LIST(self):
        self.clientSocket.send('LIST \r\n') # send the command to the server
        files = os.listdir(os.getcwd())
        print '\n _______ List of Files of Client _______\n'
        for file in files:
            print file
        print '___________________________________________'
        self.serverResponse()

    def createSocket(self):
        # create a socket to send/recieve data 
        if self.isPassiveMode == True:
            self.newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.newSocket.connect((self.passiveIP,self.passivePORT))
            print 'Passive mode socket created'
        else:
            print 'Active mode socket created', self.clientSocket.recv(1024)
            self.newSocket, addr = self.activeSocket.accept()

    def closeSocket(self):
        # close the socket created to send/recieve data    
        if self.isPassiveMode == False:
            self.activeSocket.close()
        self.newSocket.close() # clsoe the passive socket




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
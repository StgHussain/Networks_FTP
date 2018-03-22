import socket
import os
from implementClient import FTPClient

defaultUser = 'anonymous'
defaultPass = 'anonymous'
serverAddress = socket.gethostbyname('ELEN4017.ug.eie.wits.ac.za')

clientFTP = FTPClient(serverAddress, defaultUser, defaultPass)

#serverResponse = clientFTP.serverResponse() # get server response to client socket
# first need to check if connection to the server has been made

while True:
    userInput = raw_input('Input a command: ') # prompt the user to input a command 
    
    try: 
        func = getattr(clientFTP, userInput[:4].strip().upper())
        func(userInput)
    except Exception, e:
        
        print 'ERROR: ', 
        break

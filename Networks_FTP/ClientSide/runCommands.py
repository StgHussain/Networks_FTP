import socket
import os
from implementClient import FTPClient

'''
(ELEN4017.ug.eie.wits.ac.za)

Username: group4

Password: dae3Uiwa
'''

defaultUser = 'anonymous'
defaultPass = 'anonymous'
serverAddress = socket.gethostbyname('ELEN4017.ug.eie.wits.ac.za')

clientFTP = FTPClient(serverAddress, defaultUser, defaultPass)

#serverResponse = clientFTP.serverResponse() # get server response to client socket
# first need to check if connection to the server has been made

'''
group4
dae3Uiwa
'''

while True:
    userInput = raw_input('Input a command: ') # prompt the user to input a command 
    
    

    try: 
        #func = getattr(clientFTP, userInput[:4].strip().upper())
        #func(userInput)
        checkFunction = userInput[:4].strip().upper()

        if checkFunction == 'STRU':
            clientFTP.STRU(userInput[5:])

        elif checkFunction == 'MODE':
            clientFTP.MODE(userInput[5:])

        elif checkFunction == 'TYPE':
            clientFTP.TYPE(userInput[5:])

        elif checkFunction == 'LIST':
            clientFTP.LIST()

        elif checkFunction == 'PORT':
            sockPort = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockPort.bind(('',0))
            clientFTP.PORT(socket.gethostbyname(socket.gethostname()),sockPort.getsockname()[1])

        elif checkFunction == 'RETR':
            clientFTP.RETR(userInput[5:])

        elif checkFunction == 'STOR':
            clientFTP.STOR(userInput[5:])
        
        elif checkFunction == 'QUIT':
            clientFTP.QUIT()
            break

    except Exception, e:
        
        print 'ERROR: ', 
        break
# This program will run a simple UI in the terminal
import socket
import getpass # this module/library allows for the password to get hidden and received

def Login(): # this will allow the user to input username and password
    print('\n           Welcome to the FTP server! \n')
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ') # gets the password
    runFTP(username, password)

def runFTP(username, password): # checks the username and password, then runs accordingly
    if username =='admin' and password == 'admin':
        # do stuff
        print('Login Successful!\n')
        loginSuccess()
    else:
        print('Login Unsuccessful, please retry\n')
        Login()
    
def loginSuccess(): # occurs if the login was successful
    print('Please select one of the following:\n')
    userChoice = 0  # value for upload or download
    userChoice = int(raw_input('[1] Upload file\n' + '[2] Download file \n' + '\n Choice: '))    
    if userChoice == 1:
        #uploadFile()
        print('You chose to upload a file. \nPlease select a file to upload.')

    elif userChoice == 2:
        print('You chose to download a file. \nPlease select a file you wish to download\n')
        #downloadFile()
    else: 
        print('That choice is invalid, please select a valid choice.\n')
        loginSuccess()
    


# Run the simpleUI code

Login()




import socket
import threading
import os
import telnetlib


Server_IP = socket.gethostbyname(socket.gethostname())
Server_Port = 8000
currdir = os.path.abspath('.')

class FTPserverThread (threading.Thread):
    user = 'test user'
    password = 'test password'
    def __init__(self, (connection,addr)):
        self.connection = connection
        self.addr = addr
        #self.basewd = currdir #dont really know what this line does
        #self.cwd = self.basewd #dont know whats going on here
        self.rest = False
        self.pasv_mode = False
        threading.Thread.__init__(self)

    def run(self):
        self.connection.send('220 Welcome!\r\n')
        while True:
            cmd = self.connection.recv(256)

    def SYST(self):
        self.connection.send('221 Linux')#change this to whatever system the actual server will be
    def USER(self, userID):
        if userID == user:
            self.connection.send('331 OK \n')
        else:
            self.connection.send('430 No user')
    def PASS(self, passwd):
        if passwd == password:
            self.connection.send('332 OK \n')
        else:
            self.connection.send('331 Incorrect password \n')
    def QUIT(self):
        self.connection.send('221 Goodbye \n')
    def NOOP(self):
        self.connection.send('200 OK \n')
    def CWD(self, cmd ):
        check_Path = cmd.os.path.exists
        if check_Path is True:
            os.chdir(cmd)
            self.connection.send('250 OK \n')
        else:
            self.connection.send('550 No such file, directory \n')
    def CDUP(self, ):
        if not os.path.samefile(self.cwd, self.basewd):
            self.cwd = os.path.abs(os.path.join(self.cwd, '..'))
        self.connection.send('200 OK \n')

    def MOUNT(self, ):

    def PWD(self, cmd):
        cwd = os.path.relpath(self.cmd,self.basewd)
        if cwd=='.':
            cwd='/'
        else:
            cwd='/'+ cwd
        self.connnection.send('257 \"%s\"\r\n'%cwd)

    def PORT(self, cmd):
        if self.pasv_mode:
            self.servsock
            self.pasv_mode = False

    def PASV(self, cmd):
        self.pasv_mode = True
        self.servsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.servesock.bind((Server_IP,0))
        self.servsock.listen(1)
        ip, port = self.servsock



class FTPserver(threading.Thread):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK__STREAM)
        self.socket.bind((Server_IP, Server_Port))
        threading.Thread.__init__(self)

    def run(self):
        self.socket.listen(5)
        while True:
            th = FTPserverThread(self.socket.accept())
            th.daemon = True
            th.start()
    def stop(self):
        self.socket.close()

if __name__ == '__main__':
    ftp  = FTPserver()
    ftp.daemon = True
    ftp.start()
    print 'Connection information', Server_IP, ':', Server_Port
    raw_input('Enter to end...\n')
    ftp.stop()




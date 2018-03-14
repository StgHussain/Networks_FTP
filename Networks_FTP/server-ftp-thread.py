import inspect
import socket
import threading
import os
import time

Server_IP = socket.gethostbyname(socket.gethostname())
Server_Port = 8000
currdir = os.path.abspath('.')

class FTPserverThread (threading.Thread):
    user = 'test user'
    password = 'test password'
    def __init__(self, (connection,addr)):
        self.connection = connection
        self.addr = addr
        self.basewd = currdir
        self.cwd = self.basewd
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

    def LIST(self, cmd):
        self.connection.send('150 Directory listing')
        print 'List:', self.cwd
        self.start_datasock()
        for t in os.listdir(self.cwd):
            k=self.toListItem(os.path.join(self.cwd,t))
            self.datasock.send(k + '\r\n')
        self.stop_datasock()
        self.connection.send('226 Directory sent OK .\r\n')

    def toListItem(self, fn):
        st = os.stat(fn)
        fullmode = 'rwxrwrwx'
        mode = ''
        for i in range (9):
            mode += ((st.st_mode>>(8-i))&1) and fullmode[i] or '-'
        d = (os.path.isdir(fn)) and 'd' or '-'
        ftime = time.strftime(' %b %d %H:%M ', time.gmtime(st.st_mtime))
        return d + mode + ' 1 user group ' + str(st.st_size) + ftime + os.path.basename(fn)

    def CDUP(self, ):
        if not os.path.samefile(self.cwd, self.basewd):
            self.cwd = os.path.abs(os.path.join(self.cwd, '..'))
        self.connection.send('200 OK \n')

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
        l=cmd[5:].split(',')
        self.dataAddr = '.'.join(l[:4])
        self.dataPort = (int(l[4])<<8)+int(l[5])
        self.connection.send('200 Get Port .\r\n')

    def PASV(self, cmd):
        self.pasv_mode = True
        self.servsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.servesock.bind((Server_IP,0))
        self.servsock.listen(1)
        ip, port = self.servsock

    def RETR(self, cmd):
        filePath = os.path.join(self.cwd, cmd[5:-2])
        if self.mode == 'I'
            fileRead = open(filePath, 'rb')
        else:
            fileRead = open(filePath, 'r')
        self.connection.send('150 Opening data connection .\r\n')
        self.datasock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.datasock.connect((self.dataAddr, self.dataPort))
        data = fileRead(1024)
        while data:
            self.datasock.send(data)
            data = fileRead.read(1024)
        self.datasock.close()
        self.connection.send('226 Transfer complete .\r\n')

    def start_datasock(self):
        if self.pasv_mode:
            self.datasock, addr = self.servsock.accept()
            print 'connect:', addr
        else:
            self.datasock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.datasock.connect ((self.dataAddr, self.dataAddr))

    def stop_datasock(self):
        self.datasock.close()
        if self.pasv_mode:
            self.servsock.close()

    def STOR(self, cmd):
        filePath = os.path.join(self.cwd, cmd[5:-2])
        print "Uploading file: ", filePath
        if self.mode == 'I':
            fileRead = open(filePath, 'wb')
        else:
            fileRead = open(filePath, 'w')
        self.connection.send('150 Opening data connection .\r\n')
        self.start_datasock()
        while True:
            data = self.datasock.recv(1024)
            if not data: break
            fileRead.write(data)
        fileRead.close()
        self.stop_datasock()
        self.connection.send('226 Transfer complete')


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




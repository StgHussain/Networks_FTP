import socket
import threading
import os
import shutil
import time

Server_IP = '127.0.0.1'
Server_Port = 21
currdir = os.path.abspath('.')

class FTPserverThread(threading.Thread):
    user = 'test user'
    password = 'test password'

    def __init__(self, (connection, addr)):
        self.connection = connection
        self.addr = addr
        self.dataPort = 21
        self.basewd = currdir
        self.cwd = self.basewd
        self.rest = False
        self.pasv_mode = False

        self.mode = 'I'

        print 'value', self.cwd
        threading.Thread.__init__(self)

    def run(self):
        #self.connection.send('220 Welcome!')
        while True:
            cmd = self.connection.recv(1024)
            if not cmd:
                break
            else:
                print 'Recieved: ', cmd
            try:
                func = getattr(self, cmd[:4].strip().upper())
                func(cmd)
            except Exception, e:
                print 'ERROR:', e
                # traceback.print_exc()
                self.connection.send('500')

    def SYST(self,cmd):
        system = os.name
        self.connection.send('211 ' + system)  # change this to whatever system the actual server will be

    def USER(self, userID):
        if userID == 'user':
            self.connection.send('331 OK \n')
        else:
            self.connection.send('430 No user')

    def PASS(self, passwd):
        if passwd == 'password':
            self.connection.send('332 OK \n')
        else:
            self.connection.send('331 Incorrect password \n')

    def QUIT(self, cmd):
        self.connection.send('221 Goodbye \n')

    def NOOP(self, cmd):
        self.connection.send('200 OK \n')

    def CWD(self, cmd):
        chwd = cmd[4:]
        print 'directory', chwd
        check_Path = True
        check_Path = chwd.os.path.exists
        try:
            if check_Path is True:
                if chwd == '/':
                    self.cwd = self.basewd
                elif chwd[0] == '/':
                    self.cwd = os.path.join(self.basewd, chwd[1:])
                else:
                    self.cwd = os.path.join(self.cwd, chwd)
                os.chdir(chwd)
                print chwd
                self.connection.send('250 OK')
            else:
                self.connection.send('550 No such file, directory \n')
        except Exception, e:
            print 'Error', e
            self.connection.send('451 Error:')

    def LIST(self,cmd):
        self.connection.send('150 Directory listing:')
        self.start_datasock()
        listing = os.listdir('.')
        for t in listing:
            k = self.listItem(t)
            self.datasock.send(k)
        self.datasock.close()
        self.connection.send('226 Directory sent')

    def listItem(self, fileName):
        st = os.stat(fileName)
        fullmode = 'rwxrwxrwx'
        mode = ''
        for n in range (9):
            mode +=((st.st_mode>>(8-n))&1) and fullmode[n] or '-'
        d = (os.path.isdir(fileName)) and 'd' or '-'
        lastMod = time.strftime(' %b %d %H:%M ', time.gmtime(st.st_mtime))
        return d+mode+ '1 user group ' + str(st.st_size) + lastMod + os.path.basename(fileName)

    def PWD(self, cmd):
        cwd = os.getcwd()
        print cwd
        self.connection.send('250 OK' + cwd + '\r\n')

    def DELE(self, cmd):
        filePath = cmd[5:]
        try:
            os.remove(filePath)
        except Exception, e:
            print 'ERROR:', e
            self.connection.send('550')

    def RMD(self, cmd):
        fileDirectory = cmd[4:]
        print fileDirectory
        try:
            os.rmdir(fileDirectory)
        except Exception, e:
            print 'Error:', e
            try:
                shutil.rmtree(fileDirectory)
            except Exception, e:
                print 'Error', e
            self.connection.send('550')

    def PORT(self, cmd):
        print 'port comma'
        #if self.pasv_mode == True:
          #  self.servsock.close()
         #   self.pasv_mode = False
        l = cmd[5:].split(',')
        print 'qqwe'
        self.addr = '.'.join(l[:4])
        self.dataPort = (int(l[4]) << 8) + int(l[5])
        print 'zxczxc'
        self.start_datasock()
        print 'afsdasd'
        self.connection.send('200 Switched port')
        print 'hehre'


    def TYPE(self, cmd):
        self.mode = cmd[5]
        self.connection.send('200 Binary mode')

    def STRU(self, cmd):
        self.connection.send('File')

    def PASV(self, cmd):
        self.pasv_mode = True
        self.servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servsock.bind((Server_IP, 0))
        self.servsock.listen(1)
        ip, port = self.servsock.getsockname()
        print 'open', ip, port
        self.connection.send('227 Entering Passive Mode (%s,%u,%u).\r\n' %
                       (','.join(ip.split('.')), port >> 8 & 0xFF, port & 0xFF))

    def ALLO(self, cmd):
        filepath = os.path.join(self.cwd, cmd[5:])
        try:
            filesize = os.path.getsize(filepath)
            self.connection.send('250 File size ' + filesize)
        except Exception, e:
            print 'Error', e
            self.connection.send('450')

    def RETR(self, cmd):
        directory = os.getcwd()
        filePath = os.path.join(directory, cmd[5:])
        file_exists = True
        print filePath
        e = ''
        #if self.mode == 'I':
        fileRead = open(filePath, 'rb')
        #else:
        #    fileRead = open(filePath, 'r')
        try:
            if file_exists is True:
                self.start_datasock()
                while 1:
                    data = fileRead.read(1024)
                    if not data:
                        break
                    self.datasock.send(data)
                fileRead.close()
                self.stop_datasock()
        except Exception, e:
            self.connection.send('450')
            print 'Error:', e


    def STOR(self, cmd):
        filePath = os.path.join(self.cwd, cmd[5:-2])
        print "Uploading file: ", filePath
        if self.mode == 'I':
            fileread = open(filePath, 'wb')
        else:
            fileread = open(filePath, 'w')
        self.connection.send('150 Opening data connection .\r\n')
        self.start_datasock()
        while True:
            data = self.datasock.recv(1024)
            if not data: break
            fileread.write(data)
        fileread.close()
        self.stop_datasock()
        self.connection.send('226 Transfer complete')


    def start_datasock(self):
        if self.pasv_mode:
            self.datasock, addr = self.servsock.accept()
            print 'connect:', addr
        else:
            self.datasock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.datasock.connect((self.addr, self.dataPort))

    def stop_datasock(self):
        self.datasock.close()
        if self.pasv_mode:
            self.datasock.close()


class FTPserver(threading.Thread):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    ftp = FTPserver()
    ftp.daemon = True
    ftp.start()
    portNum = 21
    print 'Connection information', Server_IP, ':', portNum
    raw_input('Enter to end...\n')
    ftp.stop()

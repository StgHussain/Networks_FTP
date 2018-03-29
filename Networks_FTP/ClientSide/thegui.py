# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'thegui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from implementClient import FTPClient



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ELEN4017FTPServer(object):
    def setupUi(self, ELEN4017FTPServer):
        ELEN4017FTPServer.setObjectName(_fromUtf8("ELEN4017FTPServer"))
        ELEN4017FTPServer.resize(801, 728)
        self.centralwidget = QtGui.QWidget(ELEN4017FTPServer)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.responseFrame = QtGui.QFrame(self.centralwidget)
        self.responseFrame.setGeometry(QtCore.QRect(10, 50, 781, 181))
        self.responseFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.responseFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.responseFrame.setObjectName(_fromUtf8("responseFrame"))
        self.textBrowser = QtGui.QTextBrowser(self.responseFrame)
        self.textBrowser.setGeometry(QtCore.QRect(0, 90, 781, 91))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.responseFrame)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 781, 91))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.clientFrame = QtGui.QFrame(self.centralwidget)
        self.clientFrame.setGeometry(QtCore.QRect(10, 240, 381, 441))
        self.clientFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.clientFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.clientFrame.setObjectName(_fromUtf8("clientFrame"))
        self.clientLabel = QtGui.QLabel(self.clientFrame)
        self.clientLabel.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.clientLabel.setObjectName(_fromUtf8("clientLabel"))
        self.clientTreeView = QtGui.QTreeView(self.clientFrame)
        self.clientTreeView.setGeometry(QtCore.QRect(0, 40, 381, 401))
        self.clientTreeView.setObjectName(_fromUtf8("clientTreeView"))
        self.serverFrame = QtGui.QFrame(self.centralwidget)
        self.serverFrame.setGeometry(QtCore.QRect(420, 240, 371, 441))
        self.serverFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.serverFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.serverFrame.setObjectName(_fromUtf8("serverFrame"))
        self.serverLabel = QtGui.QLabel(self.serverFrame)
        self.serverLabel.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.serverLabel.setObjectName(_fromUtf8("serverLabel"))
        self.serverTreeView = QtGui.QTreeView(self.serverFrame)
        self.serverTreeView.setGeometry(QtCore.QRect(0, 40, 371, 401))
        self.serverTreeView.setObjectName(_fromUtf8("serverTreeView"))
        self.topFrame = QtGui.QFrame(self.centralwidget)
        self.topFrame.setGeometry(QtCore.QRect(0, 0, 791, 41))
        self.topFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.topFrame.setObjectName(_fromUtf8("topFrame"))
        self.passLabel = QtGui.QLabel(self.topFrame)
        self.passLabel.setGeometry(QtCore.QRect(430, 10, 91, 21))
        self.passLabel.setObjectName(_fromUtf8("passLabel"))
        self.loginButton = QtGui.QPushButton(self.topFrame)
        self.loginButton.setGeometry(QtCore.QRect(670, 10, 101, 31))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.userLabel = QtGui.QLabel(self.topFrame)
        self.userLabel.setGeometry(QtCore.QRect(200, 10, 91, 21))
        self.userLabel.setObjectName(_fromUtf8("userLabel"))
        self.hostLabel = QtGui.QLabel(self.topFrame)
        self.hostLabel.setGeometry(QtCore.QRect(20, 10, 70, 21))
        self.hostLabel.setObjectName(_fromUtf8("hostLabel"))
        self.hostInput = QtGui.QLineEdit(self.topFrame)
        self.hostInput.setGeometry(QtCore.QRect(70, 10, 113, 27))
        self.hostInput.setObjectName(_fromUtf8("hostInput"))
        self.userInput = QtGui.QLineEdit(self.topFrame)
        self.userInput.setGeometry(QtCore.QRect(290, 10, 113, 27))
        self.userInput.setObjectName(_fromUtf8("userInput"))
        self.passInput = QtGui.QLineEdit(self.topFrame)
        self.passInput.setGeometry(QtCore.QRect(520, 10, 113, 27))
        self.passInput.setObjectName(_fromUtf8("passInput"))
        ELEN4017FTPServer.setCentralWidget(self.centralwidget)

        self.retranslateUi(ELEN4017FTPServer)
        QtCore.QMetaObject.connectSlotsByName(ELEN4017FTPServer)

    def retranslateUi(self, ELEN4017FTPServer):
        ELEN4017FTPServer.setWindowTitle(_translate("ELEN4017FTPServer", "ELEN4017 FTP Server", None))
        self.clientLabel.setText(_translate("ELEN4017FTPServer", "Client Directory:", None))
        self.serverLabel.setText(_translate("ELEN4017FTPServer", "Server Directory:", None))
        self.passLabel.setText(_translate("ELEN4017FTPServer", "Password:", None))
        self.loginButton.setText(_translate("ELEN4017FTPServer", "Login", None))
        self.userLabel.setText(_translate("ELEN4017FTPServer", "Username:", None))
        self.hostLabel.setText(_translate("ELEN4017FTPServer", "Host:", None))

    def serverResponse(self):

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ELEN4017FTPServer = QtGui.QMainWindow()
    ui = Ui_ELEN4017FTPServer()
    ui.setupUi(ELEN4017FTPServer)
    ELEN4017FTPServer.show()
    sys.exit(app.exec_())


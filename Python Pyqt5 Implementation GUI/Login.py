# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
#sys.path.insert(0, 'images-py')
#sys.path.insert(0, 'Other pages')
import sqlite3
from Admin import Ui_Admin
import  PatientInfo
from PatientInfo import Ui_MainWindow 
class Ui_Login(object):
    
     
    # Create a Connection
    global connection
    connection=sqlite3.connect("sqlitedatabase5.db")     
    
    """
    Def show message Box
    """
    
    def ShowMessageBox(self,title,message):
        messagebox=QtWidgets.QMessageBox()
        messagebox.setIcon(QtWidgets.QMessageBox.Warning)
        messagebox.setWindowTitle(title)
        messagebox.setText(message)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messagebox.exec_()
    """
    It open a Page for the Admin to add the User's Username and password
    """
    
        #I Call it when the account and the password of the user is match
    def openMainWindowPage(self):
            #Create an object from two classes the qtgui and qmain window is inside
            self.selectWindow=QtWidgets.QMainWindow()
            self.ui=Ui_MainWindow()
            self.ui.setupUi(self.selectWindow)
            self.selectWindow.show()
            #Login.hide()
    #I Call it when the account and the password of the admin is match
    def openListAdminDialog(self):
            #Create an object from two classes the qtgui and qmain window is inside
            self.signupWindow=QtWidgets.QMainWindow()
            self.ui=Ui_Admin()
            self.ui.setupUi(self.signupWindow)
            self.signupWindow.show()
            #Login.hide()
         
    """
    Check if the password and the accout match
    """

    def loginCheck(self):
        username=self.Inputs.text()
        password=self.Inputs_2.text()
        import Diagnosis
        import Mammography
        import Sample
        global doctorname
        Sample.doctorname=username
        Diagnosis.doctorname=username
        Mammography.doctorname=username
        PatientInfo.doctorname=username
        
        result1=connection.execute("SELECT * FROM ADMIN WHERE admin=? AND PASSWORD=?",(username,password))
        result2=connection.execute("SELECT * FROM DOCTORS WHERE USER=? AND PASSWORD=?",(username,password))
        if(len(result1.fetchall())>0):
            print("Admin Found!")
            self.openListAdminDialog()  
        elif(len(result2.fetchall())>0):
            print("User Found!")
            self.openMainWindowPage()       
        elif(username=="" and password== ""):
            self.ShowMessageBox('Warning','Enter a username and a password')
        elif(username==""):
            self.ShowMessageBox('Warning','Enter a valid username')
        elif(password==""):
            self.ShowMessageBox('Warning','Enter a valid  password')
        elif(len(username)<3 or len(username)>21):
            self.ShowMessageBox('Warning','username should be at range of 3 to 20 characters')
        else:
            self.ShowMessageBox('Warning','Invalid Email and Password')
            print("User not found")
            
        #mconnection.close()

        
    def setupUi(self, Login): 
        Login.setObjectName("Login")
        Login.resize(1380, 730)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/img/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet("QPushButton {\n"
"    border-radius: 9px;\n"
"    padding: 3px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #ECF0F1;\n"
"    border: 1px solid #F76363;\n"
"\n"
"    color: #787878;\n"
"    border-radius: 4px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #ECF0F1;\n"
"    border: 1px solid #ECF0F1;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:checked:hover{\n"
"    border: 1px solid #ECF0F1;    \n"
"}\n"
"\n"
"QPushButton:selected,\n"
"QPushButton:checked:selected{\n"
"    background: #1464A0;\n"
"    color: #ECF0F1;\n"
"}\n"
"/* QLine ------------------------------------------------------------------ */\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(242, 242, 242);\n"
"    border-style: solid;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    color: #4D4D4D;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    color: #787878;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 1px solid #F76363;\n"
"    color: #4D4D4D;\n"
"}\n"
"\n"
"QLineEdit:selected{\n"
"    background: #1464A0;\n"
"    color: #32414B;\n"
"}\n"
"/* QFrame ----------------------------------------------------------------- */\n"
"\n"
"QFrame {\n"
"    border-radius: 4px;\n"
"    border: 1px solid #32414B;\n"
"}\n"
"\n"
"QFrame[frameShape=\"0\"] {\n"
"    border-radius: 4px;\n"
"    border: 1px transparent #32414B;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginFrame = QtWidgets.QFrame(self.centralwidget)
        self.LoginFrame.setGeometry(QtCore.QRect(490, 350, 351, 241))
        self.LoginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LoginFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LoginFrame.setObjectName("LoginFrame")
        self.Inputs = QtWidgets.QLineEdit(self.LoginFrame)
        self.Inputs.setEnabled(True)
        self.Inputs.setGeometry(QtCore.QRect(140, 55, 170, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.Inputs.setFont(font)
        self.Inputs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Inputs.setAutoFillBackground(False)
        self.Inputs.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Inputs.setInputMask("")
        self.Inputs.setText("")
        self.Inputs.setMaxLength(32767)
        self.Inputs.setFrame(True)
        self.Inputs.setCursorPosition(0)
        self.Inputs.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Inputs.setDragEnabled(False)
        self.Inputs.setReadOnly(False)
        self.Inputs.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Inputs.setObjectName("Inputs")
        self.Inputs_2 = QtWidgets.QLineEdit(self.LoginFrame)
        self.Inputs_2.setEnabled(True)
        self.Inputs_2.setGeometry(QtCore.QRect(140, 105, 170, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.Inputs_2.setFont(font)
        self.Inputs_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Inputs_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.Inputs_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.Inputs_2.setInputMask("")
        self.Inputs_2.setFrame(True)
        self.Inputs_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Inputs_2.setCursorPosition(0)
        self.Inputs_2.setDragEnabled(False)
        self.Inputs_2.setReadOnly(False)
        self.Inputs_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Inputs_2.setObjectName("Inputs_2")
        self.Password = QtWidgets.QLabel(self.LoginFrame)
        self.Password.setGeometry(QtCore.QRect(30, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Password.setFont(font)
        self.Password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Password.setObjectName("Password")
        self.UserName = QtWidgets.QLabel(self.LoginFrame)
        self.UserName.setGeometry(QtCore.QRect(30, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.UserName.setFont(font)
        self.UserName.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.UserName.setObjectName("UserName")
        self.LoginB = QtWidgets.QPushButton(self.LoginFrame)
        self.LoginB.setGeometry(QtCore.QRect(100, 160, 140, 30))
        '''   
        Button Action Here
        '''
        self.LoginB.clicked.connect(self.loginCheck)
        '''   
        Button Action Here
        '''
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.LoginB.setFont(font)
        self.LoginB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginB.setMouseTracking(False)
        self.LoginB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.LoginB.setIconSize(QtCore.QSize(16, 16))
        self.LoginB.setCheckable(False)
        self.LoginB.setAutoRepeat(False)
        self.LoginB.setAutoExclusive(False)
        self.LoginB.setDefault(False)
        self.LoginB.setFlat(False)
        self.LoginB.setObjectName("LoginB")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(400, 50, 511, 261))
        self.Logo.setStyleSheet("image: url(:/images/img/Logo.png);")
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.Obacity = QtWidgets.QLabel(self.centralwidget)
        self.Obacity.setGeometry(QtCore.QRect(860, 80, 581, 621))
        self.Obacity.setStyleSheet("image: url(:/images/img/Obacity.png);")
        self.Obacity.setText("")
        self.Obacity.setObjectName("Obacity")
        self.BCIGP = QtWidgets.QLabel(self.centralwidget)
        self.BCIGP.setGeometry(QtCore.QRect(442, 660, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.BCIGP.setFont(font)
        self.BCIGP.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.BCIGP.setObjectName("BCIGP")
        self.HelpB = QtWidgets.QPushButton(self.centralwidget)
        self.HelpB.setGeometry(QtCore.QRect(1330, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.HelpB.setFont(font)
        self.HelpB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HelpB.setWhatsThis("")
        self.HelpB.setStyleSheet("\n"
"image: url(:/images/img/Help.png);")
        self.HelpB.setText("")
        self.HelpB.setObjectName("HelpB")
        self.LoginFrame.raise_()
        self.Logo.raise_()
        self.Obacity.raise_()
        self.HelpB.raise_()
        self.BCIGP.raise_()
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1380, 21))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)
        self.actionAbout_Breast_Cancer_Detection = QtWidgets.QAction(Login)
        self.actionAbout_Breast_Cancer_Detection.setCheckable(False)
        self.actionAbout_Breast_Cancer_Detection.setWhatsThis("")
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.actionAbout_Breast_Cancer_Detection.setFont(font)
        self.actionAbout_Breast_Cancer_Detection.setObjectName("actionAbout_Breast_Cancer_Detection")
        self.actionAFQ = QtWidgets.QAction(Login)
        self.actionAFQ.setObjectName("actionAFQ")
        self.actionHelp_Center = QtWidgets.QAction(Login)
        self.actionHelp_Center.setObjectName("actionHelp_Center")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.Inputs.setPlaceholderText(_translate("Login", "   username"))
        self.Inputs_2.setPlaceholderText(_translate("Login", "   ********"))
        self.Password.setText(_translate("Login", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-weight:600; color:#4d4d4d;\">Password :</span></p></body></html>"))
        self.UserName.setText(_translate("Login", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-weight:600; color:#4d4d4d;\">User name :</span></p></body></html>"))
        self.LoginB.setToolTip(_translate("Login", "Log in"))
        self.LoginB.setStatusTip(_translate("Login", "Log in to start"))
        self.LoginFrame.setStatusTip(_translate("Login", "if you don't have an account contact with us by our email (htibreasrcancerapp.finalproject@gmail.com)"))
        self.LoginB.setText(_translate("Login", "Log in"))
        self.LoginB.setShortcut(_translate("Login", "Enter"))
        self.BCIGP.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#4d4d4d;\">Checkmate Breast Cancer Application for Graduation Project (2019)</span></p></body></html>"))
        self.HelpB.setToolTip(_translate("Login", "Help"))
        self.HelpB.setStatusTip(_translate("Login", "Need a help ? go to help center"))
        self.HelpB.setShortcut(_translate("Login", "Ctrl+H"))
        self.actionAbout_Breast_Cancer_Detection.setText(_translate("Login", "Help Center"))
        self.actionAbout_Breast_Cancer_Detection.setShortcut(_translate("Login", "Ctrl+H"))
        self.actionAFQ.setText(_translate("Login", "FAQ"))
        self.actionHelp_Center.setText(_translate("Login", "About Us"))

import img

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())


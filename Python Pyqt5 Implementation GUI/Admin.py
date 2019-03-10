# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class Ui_Admin(object):
    
    def __init__(self):
        super(Ui_Admin, self).__init__()
    #database connection
    global connection
    global email,password ,username
    global send_to_email
    global path 
    connection=sqlite3.connect("sqlitedatabase5.db")   
    def closewindow(self):
        self.Admin.hide()
    

       
         
    def search(self):
        username=self.SearchI.text()
        result4=connection.execute("SELECT USER FROM DOCTORS WHERE  USER=?",(username,))        
        if(len(result4.fetchall())>0):
            self.ShowMessageBox('Warning','The user found ')
            
        else:
            self.ShowMessageBox('Warning','The user not found')
    
    """
    Def show message Box
    """
    def loadData(self):
        
        try:
            query="SELECT * FROM DOCTORS"        
            result2 =connection.execute(query)
            print(result2)
            self.AccountsList.setRowCount(0)
            for row_number,row_data in enumerate(result2):
                self.AccountsList.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.AccountsList.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))    
        except Exception as error:
            print(error)
            
    
    def deleterow(self):
        
        query="SELECT * FROM DOCTORS"        
        result2 =connection.execute(query)
        for row_number in enumerate(result2):
                if row_number[0]==self.AccountsList.currentRow():
                    print('ok')
                    print(row_number[1])
                    data=row_number[1]
                    username=data[0]
                    email=data[1]
                    password=data[2]
                    path=data[3]
                    connection.execute("DELETE FROM DOCTORS WHERE USER=? AND EMAIL=?  AND PASSWORD=? AND PATH=?",(username,email,password,path))
                    connection.commit()
                    self.loadData()
                    
    def ShowMessageBox(self,title,message):
        messagebox=QtWidgets.QMessageBox()
        messagebox.setIcon(QtWidgets.QMessageBox.Warning)
        messagebox.setWindowTitle(title)
        messagebox.setText(message)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messagebox.exec_()


    
        
    def insertData(self):
        self.Validation()
        
    def Validation(self):
       
        global send_to_email ,username,password ,email   
        username = self.UsernameI.text()
        email = self.EmailI.text()
        password = self.PasswordI.text()
        
        if(self.EmailI.text().endswith(".com")==False):
            self.EmailI.clear()
            self.ShowMessageBox('Warning','Invalid Email ')
            
            #self.insertData()

        elif(len(self.PasswordI.text())<=7 or len(self.PasswordI.text())>15):
            self.PasswordI.clear()
            self.ShowMessageBox('Warning','invalid Password,Password in range of 8 to 14 character')
            #self.Validation()
            #self.insertData()
        
            #self.Validation()
            #self.insertData()
        
                 ###### Check validation 
        if(username=="" and password== "" and email==""):
            self.EmailI.clear()
            self.PasswordI.clear()
            self.ShowMessageBox('Warning','Enter a username , email and a password ')
            #self.Validation()
        elif(username==""):
            self.EmailI.clear()
            self.PasswordI.clear()
            self.ShowMessageBox('Warning','Enter a valid username')
            #self.Validation()
        elif(password==""):
            self.EmailI.clear()
            self.PasswordI.clear()
            self.ShowMessageBox('Warning','Enter a valid  password')
            #self.Validation()
        elif(email==""):
            self.EmailI.clear()
            self.PasswordI.clear()
            self.ShowMessageBox('Warning','Enter a valid  email')
            #self.Validation()
        elif(len(username)<3 or len(username)>21):
            self.EmailI.clear()
            self.PasswordI.clear()
            self.ShowMessageBox('Warning','username should be at range of 3 to 20 characters')
            #self.Validation()
         #   Have Cancer Before            
        elif((self.Blood.isChecked()==False) and (self.Mammo.isChecked()==False) and (self.Sample.isChecked()==False)):
            self.ShowMessageBox('Warning','Wrong selcection,Please Choose one path from the list')        
        else:
            result2=connection.execute("SELECT * FROM DOCTORS WHERE USER=? AND EMAIL=? AND PASSWORD=?" ,(username,email,password))
            if(len(result2.fetchall())>0):
                self.ShowMessageBox('Warning','This Username is already exist before')
                #self.Validation()
            else:
                self.store()

            #self.closewindow()
    def store(self):    
        global send_to_email
        if(self.Blood.isChecked()==True):
            path=1
        elif(self.Sample.isChecked()==True):
            path=2
        elif(self.Mammo.isChecked()==True):
            path=3  
        send_to_email=email
        connection.execute("INSERT INTO DOCTORS VALUES (?,?,?,?)", (username,email,password,path))
        connection.commit()
        self.ShowMessageBox('Warning','The User add Successfuly')
        self.loadData()
        self.sendinfomail()
        
    def sendinfomail(self):
       appemail='htibreastcancerapp.finalproject@gmail.com'
       apppassword='htibreastcancerapp.finalproject2019'
       subject='Breast Cancer CheckMate app'
       message=('Hello '+username+'! greetings,\n congratulation you have been recived your mail from hti breast cancer check mate.\n you username is '+username+' and your password is '+password)
       print(message)
       
       msg=MIMEMultipart()
       msg["From"]=appemail
       msg["To"]=send_to_email
       msg["Subject"]=subject
       msg.attach(MIMEText(message,'plain'))
       server=smtplib.SMTP('smtp.gmail.com',587)
       server.starttls()
       server.login(appemail,apppassword)
       text=msg.as_string()
       server.sendmail(appemail,send_to_email,text)
       server.quit()      
       
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(850, 690)
        Admin.setMaximumSize(QtCore.QSize(850, 690))
        Admin.move(230,0)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/img/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Admin.setWindowIcon(icon)
        Admin.setStyleSheet("QPushButton {\n"
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
"}\n"
"\n"
"\n"
"/* QCombobox -------------------------------------------------------------- */\n"
"\n"
"QComboBox {\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    selection-background-color: #1464A0;\n"
"\n"
"}\n"
"\n"
"QComboBox:disabled {\n"
"    background-color: rgb(242, 242, 242);\n"
"    color: #787878;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    border: 1px solid #F76363;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    selection-background-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(242, 242, 242);\n"
"    border-radius: 4px;\n"
"    border: 1px solid #32414B;\n"
"    selection-color: #F76363;\n"
"    selection-background-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border-left-width: 0px;\n"
"    border-left-color: #F76363;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    \n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/images/img/down_arrow.png);\n"
"}\n"
"/* QDateEdit-------------------------------------------------------------- */\n"
"\n"
"QDateEdit {\n"
"     background-color: rgb(242, 242, 242);\n"
"    border-style: solid;\n"
"    border: 1px solid #32414B;\n"
"    border-radius: 4px;\n"
"    padding-top: 2px;   \n"
"    padding-bottom: 2px;  \n"
"    padding-left: 4px;\n"
"}\n"
"QDateEdit:hover{\n"
"    border: 1px solid #F76363;\n"
"    color: #4D4D4D;\n"
"}")
        Admin.setIconSize(QtCore.QSize(27, 27))
        self.centralwidget = QtWidgets.QWidget(Admin)
        self.centralwidget.setObjectName("centralwidget")
        self.AccountsList = QtWidgets.QTableWidget(self.centralwidget)
        self.AccountsList.setGeometry(QtCore.QRect(80, 380, 691, 241))
        self.AccountsList.setColumnCount(3)
        self.AccountsList.setObjectName("AccountsList")
        self.AccountsList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.AccountsList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.AccountsList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.AccountsList.setHorizontalHeaderItem(2, item)
        self.AccountsList.horizontalHeader().setDefaultSectionSize(222)
        self.AccountsList.horizontalHeader().setMinimumSectionSize(30)
        self.AccountsList.verticalHeader().setDefaultSectionSize(30)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(220, 77, 411, 261))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.EmailI = QtWidgets.QLineEdit(self.frame)
        self.EmailI.setEnabled(True)
        self.EmailI.setGeometry(QtCore.QRect(150, 75, 221, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.EmailI.setFont(font)
        self.EmailI.setAutoFillBackground(False)
        self.EmailI.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EmailI.setInputMask("")
        self.EmailI.setFrame(True)
        self.EmailI.setCursorPosition(0)
        self.EmailI.setDragEnabled(False)
        self.EmailI.setReadOnly(False)
        self.EmailI.setPlaceholderText("")
        self.EmailI.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.EmailI.setObjectName("EmailI")
        self.UsernameI = QtWidgets.QLineEdit(self.frame)
        self.UsernameI.setEnabled(True)
        self.UsernameI.setGeometry(QtCore.QRect(150, 35, 221, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.UsernameI.setFont(font)
        self.UsernameI.setAutoFillBackground(False)
        self.UsernameI.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.UsernameI.setInputMask("")
        self.UsernameI.setFrame(True)
        self.UsernameI.setCursorPosition(0)
        self.UsernameI.setDragEnabled(False)
        self.UsernameI.setReadOnly(False)
        self.UsernameI.setPlaceholderText("")
        self.UsernameI.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.UsernameI.setObjectName("UsernameI")
        self.Password = QtWidgets.QLabel(self.frame)
        self.Password.setGeometry(QtCore.QRect(30, 110, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Password.setFont(font)
        self.Password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Password.setObjectName("Password")
        self.Username = QtWidgets.QLabel(self.frame)
        self.Username.setGeometry(QtCore.QRect(50, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Username.setFont(font)
        self.Username.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Username.setObjectName("Username")
        self.PasswordI = QtWidgets.QLineEdit(self.frame)
        self.PasswordI.setEnabled(True)
        self.PasswordI.setGeometry(QtCore.QRect(150, 115, 221, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.PasswordI.setFont(font)
        self.PasswordI.setAutoFillBackground(False)
        self.PasswordI.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PasswordI.setInputMask("")
        self.PasswordI.setFrame(True)
        self.PasswordI.setCursorPosition(0)
        self.PasswordI.setDragEnabled(False)
        self.PasswordI.setReadOnly(False)
        self.PasswordI.setPlaceholderText("")
        self.PasswordI.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.PasswordI.setObjectName("PasswordI")
        self.AddB = QtWidgets.QPushButton(self.frame)
        self.AddB.setGeometry(QtCore.QRect(290, 220, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        
        '''Load the data into tables
        '''
        
        self.loadData()
        
        '''Load the data into tables
        '''
        
        
        self.AddB.setFont(font)
        self.AddB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddB.setStatusTip("")
        self.AddB.setWhatsThis("")
        self.AddB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.AddB.setObjectName("AddB")
        
        '''
        Action Here for Pushbutton
        '''
        
        self.AddB.clicked.connect(self.insertData)
        
        '''
        Action Here for Pushbutton
        '''
        self.Email = QtWidgets.QLabel(self.frame)
        self.Email.setGeometry(QtCore.QRect(20, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Email.setFont(font)
        self.Email.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Email.setObjectName("Email")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 150, 110, 100))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Blood = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Blood.setFont(font)
        self.Blood.setStyleSheet("color: rgb(77, 77, 77);")
        self.Blood.setObjectName("Blood")
        self.verticalLayout.addWidget(self.Blood)
        self.Sample = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Sample.setFont(font)
        self.Sample.setStyleSheet("color: rgb(77, 77, 77);")
        self.Sample.setObjectName("Sample")
        self.verticalLayout.addWidget(self.Sample)
        self.Mammo = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Mammo.setFont(font)
        self.Mammo.setStyleSheet("color: rgb(77, 77, 77);")
        self.Mammo.setObjectName("Mammo")
        self.verticalLayout.addWidget(self.Mammo)
        #self.FNA = QtWidgets.QRadioButton(self.layoutWidget)
        #font = QtGui.QFont()
        #font.setPointSize(10)
        #self.FNA.setFont(font)
        #self.FNA.setStyleSheet("color: rgb(77, 77, 77);")
        #self.FNA.setObjectName("FNA")
        #self.verticalLayout.addWidget(self.FNA)
        self.Password_2 = QtWidgets.QLabel(self.frame)
        self.Password_2.setGeometry(QtCore.QRect(30, 144, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Password_2.setFont(font)
        self.Password_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Password_2.setObjectName("Password_2")
        self.NewPatient = QtWidgets.QLabel(self.centralwidget)
        self.NewPatient.setGeometry(QtCore.QRect(240, 62, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.NewPatient.setFont(font)
        self.NewPatient.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NewPatient.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.NewPatient.setObjectName("NewPatient")
        self.AccountsT = QtWidgets.QLabel(self.centralwidget)
        self.AccountsT.setGeometry(QtCore.QRect(250, 7, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.AccountsT.setFont(font)
        self.AccountsT.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.AccountsT.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.AccountsT.setFrameShape(QtWidgets.QFrame.Box)
        self.AccountsT.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.AccountsT.setObjectName("AccountsT")
        self.ExitB = QtWidgets.QPushButton(self.centralwidget)
        self.ExitB.setGeometry(QtCore.QRect(630, 630, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ExitB.setFont(font)
        self.ExitB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitB.setStatusTip("")
        self.ExitB.setWhatsThis("")
        self.ExitB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.ExitB.setObjectName("ExitB")
        '''
        Close window
        '''
        self.ExitB.clicked.connect(Admin.hide)
        '''
        Close window
        '''        
        self.DeleteB = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteB.setGeometry(QtCore.QRect(500, 630, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.DeleteB.setFont(font)
        self.DeleteB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DeleteB.setWhatsThis("")
        self.DeleteB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.DeleteB.setObjectName("DeleteB")
        '''
        DeleteB action
        '''
        self.DeleteB.clicked.connect(self.deleterow)
        self.SearchI = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchI.setEnabled(True)
        self.SearchI.setGeometry(QtCore.QRect(240, 347, 231, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.SearchI.setFont(font)
        self.SearchI.setAutoFillBackground(False)
        self.SearchI.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SearchI.setInputMask("")
        self.SearchI.setFrame(True)
        self.SearchI.setCursorPosition(0)
        self.SearchI.setDragEnabled(False)
        self.SearchI.setReadOnly(False)
        self.SearchI.setPlaceholderText("")
        self.SearchI.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.SearchI.setObjectName("SearchI")
        self.SearchB = QtWidgets.QPushButton(self.centralwidget)
        self.SearchB.setGeometry(QtCore.QRect(500, 344, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.SearchB.setFont(font)
        self.SearchB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SearchB.setStatusTip("")
        self.SearchB.setWhatsThis("")
        self.SearchB.setStyleSheet("background-color: rgb(149, 149, 149);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/img/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchB.setIcon(icon)
        self.SearchB.setIconSize(QtCore.QSize(15, 15))
        self.SearchB.setObjectName("SearchB")
        '''
        Search Button action
        '''
        self.SearchB.clicked.connect(self.search)
        '''
        Search Button action
        '''
        self.HelpB = QtWidgets.QPushButton(self.centralwidget)
        self.HelpB.setGeometry(QtCore.QRect(810, 10, 31, 31))
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
        self.Obacity = QtWidgets.QLabel(self.centralwidget)
        self.Obacity.setGeometry(QtCore.QRect(450, 80, 581, 621))
        self.Obacity.setStyleSheet("image: url(:/images/img/Obacity.png);")
        self.Obacity.setText("")
        self.Obacity.setObjectName("Obacity")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(20, 10, 151, 81))
        self.Logo.setStyleSheet("image: url(:/images/img/Logo.png);")
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.Obacity.raise_()
        self.frame.raise_()
        self.NewPatient.raise_()
        self.AccountsT.raise_()
        self.ExitB.raise_()
        self.DeleteB.raise_()
        self.SearchI.raise_()
        self.SearchB.raise_()
        self.HelpB.raise_()
        self.AccountsList.raise_()
        self.Logo.raise_()
        Admin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Admin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menubar.setObjectName("menubar")
        Admin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Admin)
        self.statusbar.setObjectName("statusbar")
        Admin.setStatusBar(self.statusbar)
        self.actionHelp_Center = QtWidgets.QAction(Admin)
        self.actionHelp_Center.setObjectName("actionHelp_Center")
        self.actionFAQ = QtWidgets.QAction(Admin)
        self.actionFAQ.setObjectName("actionFAQ")
        self.actionAbout_Us = QtWidgets.QAction(Admin)
        self.actionAbout_Us.setObjectName("actionAbout_Us")

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)
        Admin.setTabOrder(self.UsernameI, self.EmailI)
        Admin.setTabOrder(self.EmailI, self.PasswordI)
        Admin.setTabOrder(self.PasswordI, self.AddB)
        Admin.setTabOrder(self.AddB, self.SearchI)
        Admin.setTabOrder(self.SearchI, self.SearchB)
        Admin.setTabOrder(self.SearchB, self.AccountsList)
        Admin.setTabOrder(self.AccountsList, self.DeleteB)
        Admin.setTabOrder(self.DeleteB, self.ExitB)
        Admin.setTabOrder(self.ExitB, self.HelpB)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Admin"))
        item = self.AccountsList.horizontalHeaderItem(0)
        item.setText(_translate("Admin", "User Name"))
        item = self.AccountsList.horizontalHeaderItem(1)
        item.setText(_translate("Admin", "E-mail Adress"))
        item = self.AccountsList.horizontalHeaderItem(2)
        item.setText(_translate("Admin", "Password"))
        self.Password.setText(_translate("Admin", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Password :</span></p></body></html>"))
        self.Username.setText(_translate("Admin", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">User Name :</span></p></body></html>"))
        self.AddB.setToolTip(_translate("Admin", "Add Acouunt"))
        self.AddB.setText(_translate("Admin", "Add"))
        self.AddB.setShortcut(_translate("Admin", "Enter"))
        self.Email.setText(_translate("Admin", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">E-mail Address :</span></p></body></html>"))
        self.Blood.setText(_translate("Admin", "Blood Analysis"))
        self.Sample.setText(_translate("Admin", "Sample"))
        self.Mammo.setText(_translate("Admin", "Mammography"))
        #self.FNA.setText(_translate("Admin", "FNA"))
        self.Password_2.setText(_translate("Admin", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Path :</span></p></body></html>"))
        self.NewPatient.setText(_translate("Admin", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#4d4d4d;\">Create Account</span></p></body></html>"))
        self.AccountsT.setText(_translate("Admin", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#4d4d4d;\">Accounts List</span></p></body></html>"))
        self.ExitB.setToolTip(_translate("Admin", "Exit"))
        self.ExitB.setText(_translate("Admin", "Exit"))
        self.ExitB.setShortcut(_translate("Admin", "Esc"))
        self.DeleteB.setToolTip(_translate("Admin", "Delete"))
        self.DeleteB.setStatusTip(_translate("Admin", "Select the user name that you need to delete and delete it"))
        self.DeleteB.setText(_translate("Admin", "Delete"))
        self.DeleteB.setShortcut(_translate("Admin", "Del"))
        self.SearchB.setToolTip(_translate("Admin", "Search"))
        self.SearchB.setText(_translate("Admin", "Search"))
        self.HelpB.setToolTip(_translate("Admin", "Help"))
        self.HelpB.setStatusTip(_translate("Admin", "Need a help ? go to help center"))
        self.HelpB.setShortcut(_translate("Admin", "Ctrl+H"))
        self.actionHelp_Center.setText(_translate("Admin", "Help Center"))
        self.actionHelp_Center.setShortcut(_translate("Admin", "Ctrl+H"))
        self.actionFAQ.setText(_translate("Admin", "FAQ"))
        self.actionAbout_Us.setText(_translate("Admin", "About Us"))

import img

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QMainWindow()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())


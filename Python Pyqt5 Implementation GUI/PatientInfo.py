# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PatientInfo.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

#import Diagnosis
#from Login import username
class Ui_MainWindow(object):
    global doctorname
    
    # Create a Connection
    global connection
    connection=sqlite3.connect("sqlitedatabase5.db")     
    
    def OpenBloodHistory(self):
        from HistoryBlood import Ui_HistoryBlood
        #Create an object from two classes the qtgui and qmain window is inside
        self.selectWindow=QtWidgets.QMainWindow()
        self.ui=Ui_HistoryBlood()
        self.ui.setupUi(self.selectWindow)
        self.selectWindow.show()
        #MainWindow.hide()
    def OpenSampleHistory(self):
        from HistorySample import Ui_SampleHistory
        #Create an object from two classes the qtgui and qmain window is inside
        self.selectWindow=QtWidgets.QMainWindow()
        self.ui=Ui_SampleHistory()
        self.ui.setupUi(self.selectWindow)
        self.selectWindow.show()
    def OpenMammoHistory(self):
        from HistoryMammo import Ui_HistoryMammo
        #Create an object from two classes the qtgui and qmain window is inside
        self.selectWindow=QtWidgets.QMainWindow()
        self.ui=Ui_HistoryMammo()
        self.ui.setupUi(self.selectWindow)
        self.selectWindow.show()
        #MainWindow.hide()

    def OpenFNAHistory(self):
        from HistoryFNA import Ui_HistoryFNA
        #Create an object from two classes the qtgui and qmain window is inside
        self.selectWindow=QtWidgets.QMainWindow()
        self.ui=Ui_HistoryFNA()
        self.ui.setupUi(self.selectWindow)
        self.selectWindow.show()
        #MainWindow.hide()
        
    def ShowMessageBox(self,title,message):
        messagebox=QtWidgets.QMessageBox()
        messagebox.setIcon(QtWidgets.QMessageBox.Warning)
        messagebox.setWindowTitle(title)
        messagebox.setText(message)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messagebox.exec_()
    

        
    
    def checkIdInfo(self):
        global SSNI
        SSNI=self.SSN_Input.text()
        
        
        
       
        
        """HistoryMammo.doctorname=doctorname
        HistorySample.doctorname=doctorname
        HistoryBlood.doctorname=doctorname
        HistoryFNA.doctorname=doctorname
        """

        
        
        result3=connection.execute("SELECT PATIENTID FROM PATIENT WHERE  PATIENTID=?",(SSNI,))
        #print(result3)
        if(len(result3.fetchall())>0):
            #self.ShowMessageBox('Warning','The App find the user Successfuly')
            print('Found Successfully')
            PatientPath =connection.execute("SELECT PATH FROM DOCTORS WHERE USER=? ",(doctorname,))
            for row_number in PatientPath.fetchall():
                data=row_number[0]
                print(data)
                if(data==1):
                    import Diagnosis
                    import HistoryBlood
                    Diagnosis.PatientID=SSNI
                    HistoryBlood.PatientID=SSNI
                    self.OpenBloodHistory()
                    #MainWindow.hide()
                elif(data==2):
                    import Sample
                    import HistorySample
                    HistorySample.PatientID=SSNI
                    import SampleRecerrence
                    SampleRecerrence.PatientID=SSNI
                    Sample.PatientID=SSNI
                    
                    self.OpenSampleHistory()
                elif(data==3):
                    import Mammography
                    import HistoryMammo
                    import CancerInfoMammo
                    Mammography.PatientID=SSNI
                    HistoryMammo.PatientID=SSNI
                    CancerInfoMammo.PatientID=SSNI
                    self.OpenMammoHistory()
                elif(data==4):
                    import FNA
                    import HistoryFNA
                    HistoryFNA.PatientID=SSNI
                    FNA.PatientID=SSNI
                    self.OpenFNAHistory()
                else:
                    self.ShowMessageBox('Warning','Error happend')           
            #Patient =connection.execute("SELECT * FROM PATIENT WHERE PATIENTID=1234 ")
            '''
            Path1=connection.execute("SELECT PATH FROM DOCTORS WHERE  USER=? AND PATH=1",(doctorname,))
            Path2=connection.execute("SELECT PATH FROM DOCTORS WHERE  USER=? AND PATH=2",(doctorname,))
            Path3=connection.execute("SELECT PATH FROM DOCTORS WHERE  USER=? AND PATH=3",(doctorname,))
            Path4=connection.execute("SELECT PATH FROM DOCTORS WHERE  USER=? AND PATH=4",(doctorname,))

            if(len(Path1.fetchall())>0):
                self.OpenBloodHistory()
            elif(len(Path2.fetchall())>0):
                self.OpenSampleHistory()
            elif(len(Path3.fetchall())>0):
                self.OpenMammoHistory()
            elif(len(Path4.fetchall())>0):
                self.OpenFNAHistory()
            
            else:
                self.ShowMessageBox('Warning','Error happend')
            
            if(len(result1.fetchall())>0):
                print((len(Path.fetchone())==1))
                
            elif(len(Path.fetchone())==2):
                print((len(Path.fetchone())==2))
            elif(len(Path.fetchone())==3):
                print((len(Path.fetchone())==3))
            elif(len(Path.fetchone())==4):
                print((len(Path.fetchone())==4))
                self.OpenFNAHistory()
            '''
        
                
            
        else:
            self.ShowMessageBox('Warning','The user not found')
            
    def saveInfo(self):
        FirstNameI=self.FirstNameI.text()
        FamilyNameI=self.FamilyNameI.text()
        SSNI=self.SSNI.text()
        PhoneNoI=self.PhoneNoI.text() #1 
        dateEdit=self.dateEdit.text()
           
        #   Have Cancer Before
        
        if(self.Male.isChecked()==True):
            Gender="Male"
        elif(self.Female.isChecked()==True):
            Gender="Female"
            
        #   Have Cancer Before
        
        if(self.cancero.isChecked()==True):
            Cancer="Yes"
        elif(self.nocancero.isChecked()==True):
            Cancer="No"
        
        #   Have Diabetes Before
        
        if(self.diabeteso.isChecked()==True):
            Diabetes="Yes"
        elif(self.nodiabeteso.isChecked()==True):
            Diabetes="No"
            
        #   Have Blood peressure Before
        
        if(self.bloodpo.isChecked()==True):
            BloodPressure="Yes"
        elif(self.nobloodpo.isChecked()==True):
            BloodPressure="No"

        #   Have Anemia Before
        
        if(self.anemiao.isChecked()==True):
            Anemia="Yes"
        elif(self.noanemiao.isChecked()==True):
            Anemia="No"
        
        #print(self.Gender)
        
        result3=connection.execute("SELECT * FROM PATIENT WHERE FIRSTNAME=? AND FAMILYNAME=? AND PATIENTID=? AND PHONENUMBER=? AND BIRTHDATE=? AND GENDER=? AND CANCER=? AND DIABETES=? AND BLOODPRESSURE=? AND ANEMIA=?",(FirstNameI,FamilyNameI,SSNI,PhoneNoI,dateEdit,Gender,Cancer,Diabetes,BloodPressure,Anemia))
        #connection.execute("INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?,?,?)",('moh','essam',35545678910112,'01144931949','01-12-2010','Male','Yes','Yes','Yes','Yes'))
        if(len(result3.fetchall())>0):
            print("ID exist before")
    
        else:
            if(len(SSNI)<7 or len(SSNI)>15):
                self.ShowMessageBox('Warning','The Identity Card should be in range of 7 to 14')

            else:
                connection.execute("INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?,?,?)",(FirstNameI,FamilyNameI,SSNI,PhoneNoI,dateEdit,Gender,Cancer,Diabetes,BloodPressure,Anemia))
                connection.commit()
                self.ShowMessageBox('Warning','The User Added Successfuly')
            #connection.close()
            
    def DAWarnning(self):
        self.ShowMessageBox('Warning',"This Page doesn't available for you ")
    
    
    def SSWarnning(self):
        self.ShowMessageBox('Warning',"Wrong Choice,Check if the patient is registerd or add new patient")
    
    
    def SPWarnning(self):
        self.ShowMessageBox('Warning',"You are in the same page")
    
    
    def setupUi(self, MainWindow):        
        print(doctorname)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1380, 730)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/img/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QPushButton {\n"
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(580, 260, 400, 1))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(270, 50, 1041, 621))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Obacity = QtWidgets.QLabel(self.frame)
        self.Obacity.setGeometry(QtCore.QRect(690, 70, 641, 591))
        self.Obacity.setStyleSheet("image: url(:/images/img/Obacity.png);")
        self.Obacity.setText("")
        self.Obacity.setObjectName("Obacity")
        self.NewPatientF = QtWidgets.QFrame(self.frame)
        self.NewPatientF.setGeometry(QtCore.QRect(210, 250, 581, 351))
        self.NewPatientF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NewPatientF.setFrameShadow(QtWidgets.QFrame.Plain)
        self.NewPatientF.setObjectName("NewPatientF")
        self.FirstName = QtWidgets.QLabel(self.NewPatientF)
        self.FirstName.setGeometry(QtCore.QRect(20, 35, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.FirstName.setFont(font)
        self.FirstName.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.FirstName.setObjectName("FirstName")
        self.SaveB = QtWidgets.QPushButton(self.NewPatientF)
        self.SaveB.setGeometry(QtCore.QRect(220, 310, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.SaveB.setFont(font)
        self.SaveB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveB.setMouseTracking(False)
        self.SaveB.setWhatsThis("")
        self.SaveB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.SaveB.setIconSize(QtCore.QSize(16, 16))
        self.SaveB.setAutoExclusive(False)
        self.SaveB.setDefault(False)
        self.SaveB.setFlat(False)
        self.SaveB.setObjectName("SaveB")
        ''' 
        Button Action to save info start
        '''
        self.SaveB.clicked.connect(self.saveInfo)
        
        ''' 
        Button Action to save info end
        '''
        self.FirstNameI = QtWidgets.QLineEdit(self.NewPatientF)
        self.FirstNameI.setEnabled(True)
        self.FirstNameI.setGeometry(QtCore.QRect(120, 40, 141, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.FirstNameI.setFont(font)
        self.FirstNameI.setAutoFillBackground(False)
        self.FirstNameI.setStyleSheet("")
        self.FirstNameI.setInputMask("")
        self.FirstNameI.setFrame(True)
        self.FirstNameI.setCursorPosition(0)
        self.FirstNameI.setDragEnabled(False)
        self.FirstNameI.setReadOnly(False)
        self.FirstNameI.setPlaceholderText("")
        self.FirstNameI.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.FirstNameI.setObjectName("FirstNameI")
        self.FamilyNameI = QtWidgets.QLineEdit(self.NewPatientF)
        self.FamilyNameI.setEnabled(True)
        self.FamilyNameI.setGeometry(QtCore.QRect(410, 40, 141, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.FamilyNameI.setFont(font)
        self.FamilyNameI.setAutoFillBackground(False)
        self.FamilyNameI.setStyleSheet("")
        self.FamilyNameI.setInputMask("")
        self.FamilyNameI.setFrame(True)
        self.FamilyNameI.setCursorPosition(0)
        self.FamilyNameI.setDragEnabled(False)
        self.FamilyNameI.setReadOnly(False)
        self.FamilyNameI.setPlaceholderText("")
        self.FamilyNameI.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.FamilyNameI.setObjectName("FamilyNameI")
        self.SSNI = QtWidgets.QLineEdit(self.NewPatientF)
        self.SSNI.setEnabled(True)
        self.SSNI.setGeometry(QtCore.QRect(120, 80, 141, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.SSNI.setFont(font)
        self.SSNI.setAutoFillBackground(False)
        self.SSNI.setStyleSheet("")
        self.SSNI.setInputMask("")
        self.SSNI.setFrame(True)
        self.SSNI.setCursorPosition(0)
        self.SSNI.setDragEnabled(False)
        self.SSNI.setReadOnly(False)
        self.SSNI.setPlaceholderText("")
        self.SSNI.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.SSNI.setObjectName("SSNI")
        self.dateEdit = QtWidgets.QDateEdit(self.NewPatientF)
        self.dateEdit.setGeometry(QtCore.QRect(120, 120, 141, 25))
        self.dateEdit.setObjectName("dateEdit")
        self.PhoneNo = QtWidgets.QLabel(self.NewPatientF)
        self.PhoneNo.setGeometry(QtCore.QRect(10, 75, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.PhoneNo.setFont(font)
        self.PhoneNo.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PhoneNo.setObjectName("PhoneNo")
        self.Age = QtWidgets.QLabel(self.NewPatientF)
        self.Age.setGeometry(QtCore.QRect(20, 115, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Age.setFont(font)
        self.Age.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Age.setObjectName("Age")
        self.LastName = QtWidgets.QLabel(self.NewPatientF)
        self.LastName.setGeometry(QtCore.QRect(290, 35, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.LastName.setFont(font)
        self.LastName.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.LastName.setObjectName("LastName")
        self.Gender = QtWidgets.QLabel(self.NewPatientF)
        self.Gender.setGeometry(QtCore.QRect(310, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Gender.setFont(font)
        self.Gender.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Gender.setObjectName("Gender")
        self.PhoneNo_2 = QtWidgets.QLabel(self.NewPatientF)
        self.PhoneNo_2.setGeometry(QtCore.QRect(280, 75, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.PhoneNo_2.setFont(font)
        self.PhoneNo_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PhoneNo_2.setObjectName("PhoneNo_2")
        self.PhoneNoI = QtWidgets.QLineEdit(self.NewPatientF)
        self.PhoneNoI.setEnabled(True)
        self.PhoneNoI.setGeometry(QtCore.QRect(410, 80, 141, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.PhoneNoI.setFont(font)
        self.PhoneNoI.setAutoFillBackground(False)
        self.PhoneNoI.setStyleSheet("")
        self.PhoneNoI.setInputMask("")
        self.PhoneNoI.setFrame(True)
        self.PhoneNoI.setCursorPosition(0)
        self.PhoneNoI.setDragEnabled(False)
        self.PhoneNoI.setReadOnly(False)
        self.PhoneNoI.setPlaceholderText("")
        self.PhoneNoI.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.PhoneNoI.setObjectName("PhoneNoI")
        self.Hint_2 = QtWidgets.QFrame(self.NewPatientF)
        self.Hint_2.setGeometry(QtCore.QRect(400, 300, 171, 41))
        self.Hint_2.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.Hint_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Hint_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Hint_2.setObjectName("Hint_2")
        self.Hint = QtWidgets.QLabel(self.Hint_2)
        self.Hint.setGeometry(QtCore.QRect(40, 10, 121, 21))
        self.Hint.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Hint.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.Hint.setObjectName("Hint")
        self.label = QtWidgets.QLabel(self.Hint_2)
        self.label.setGeometry(QtCore.QRect(12, 12, 20, 20))
        self.label.setStyleSheet("image: url(:/images/img/Hint.png);\n"
"background-color: rgb(242, 242, 242);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Age_2 = QtWidgets.QLabel(self.NewPatientF)
        self.Age_2.setGeometry(QtCore.QRect(10, 193, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Age_2.setFont(font)
        self.Age_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Age_2.setObjectName("Age_2")
        self.Age_4 = QtWidgets.QLabel(self.NewPatientF)
        self.Age_4.setGeometry(QtCore.QRect(17, 223, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Age_4.setFont(font)
        self.Age_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Age_4.setObjectName("Age_4")
        self.Age_3 = QtWidgets.QLabel(self.NewPatientF)
        self.Age_3.setGeometry(QtCore.QRect(10, 163, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Age_3.setFont(font)
        self.Age_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Age_3.setObjectName("Age_3")
        self.Age_5 = QtWidgets.QLabel(self.NewPatientF)
        self.Age_5.setGeometry(QtCore.QRect(10, 253, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Age_5.setFont(font)
        self.Age_5.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Age_5.setObjectName("Age_5")
        self.widget = QtWidgets.QWidget(self.NewPatientF)
        self.widget.setGeometry(QtCore.QRect(412, 116, 123, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Female = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Female.setFont(font)
        self.Female.setStyleSheet("color: rgb(77, 77, 77);")
        self.Female.setObjectName("Female")
        self.horizontalLayout.addWidget(self.Female)
        self.Male = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Male.setFont(font)
        self.Male.setStyleSheet("color: rgb(77, 77, 77);")
        self.Male.setObjectName("Male")
        self.horizontalLayout.addWidget(self.Male)
        self.widget1 = QtWidgets.QWidget(self.NewPatientF)
        self.widget1.setGeometry(QtCore.QRect(200, 170, 181, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancero = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancero.setFont(font)
        self.cancero.setStyleSheet("color: rgb(77, 77, 77);")
        self.cancero.setObjectName("Yes")
        self.horizontalLayout_2.addWidget(self.cancero)
        self.nocancero = QtWidgets.QRadioButton(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nocancero.setFont(font)
        self.nocancero.setStyleSheet("color: rgb(77, 77, 77);")
        self.nocancero.setObjectName("No")
        self.horizontalLayout_2.addWidget(self.nocancero)
        self.widget2 = QtWidgets.QWidget(self.NewPatientF)
        self.widget2.setGeometry(QtCore.QRect(200, 200, 181, 22))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.diabeteso = QtWidgets.QRadioButton(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.diabeteso.setFont(font)
        self.diabeteso.setStyleSheet("color: rgb(77, 77, 77);")
        self.diabeteso.setObjectName("Yes_2")
        self.horizontalLayout_3.addWidget(self.diabeteso)
        self.nodiabeteso = QtWidgets.QRadioButton(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nodiabeteso.setFont(font)
        self.nodiabeteso.setStyleSheet("color: rgb(77, 77, 77);")
        self.nodiabeteso.setObjectName("No_2")
        self.horizontalLayout_3.addWidget(self.nodiabeteso)
        self.widget3 = QtWidgets.QWidget(self.NewPatientF)
        self.widget3.setGeometry(QtCore.QRect(200, 230, 181, 22))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bloodpo = QtWidgets.QRadioButton(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bloodpo.setFont(font)
        self.bloodpo.setStyleSheet("color: rgb(77, 77, 77);")
        self.bloodpo.setObjectName("Yes_3")
        self.horizontalLayout_4.addWidget(self.bloodpo)
        self.nobloodpo = QtWidgets.QRadioButton(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nobloodpo.setFont(font)
        self.nobloodpo.setStyleSheet("color: rgb(77, 77, 77);")
        self.nobloodpo.setObjectName("No_3")
        self.horizontalLayout_4.addWidget(self.nobloodpo)
        self.widget4 = QtWidgets.QWidget(self.NewPatientF)
        self.widget4.setGeometry(QtCore.QRect(200, 260, 181, 22))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.anemiao = QtWidgets.QRadioButton(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.anemiao.setFont(font)
        self.anemiao.setStyleSheet("color: rgb(77, 77, 77);")
        self.anemiao.setObjectName("Yes_4")
        self.horizontalLayout_5.addWidget(self.anemiao)
        self.noanemiao = QtWidgets.QRadioButton(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.noanemiao.setFont(font)
        self.noanemiao.setStyleSheet("color: rgb(77, 77, 77);")
        self.noanemiao.setObjectName("No_4")
        self.horizontalLayout_5.addWidget(self.noanemiao)
        self.PatientSSN = QtWidgets.QLabel(self.frame)
        self.PatientSSN.setGeometry(QtCore.QRect(360, 95, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.PatientSSN.setFont(font)
        self.PatientSSN.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PatientSSN.setObjectName("PatientSSN")
        self.StartB = QtWidgets.QPushButton(self.frame)
        self.StartB.setGeometry(QtCore.QRect(470, 140, 101, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.StartB.setFont(font)
        self.StartB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StartB.setMouseTracking(False)
        self.StartB.setWhatsThis("")
        self.StartB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.StartB.setIconSize(QtCore.QSize(16, 16))
        self.StartB.setAutoExclusive(False)
        self.StartB.setDefault(False)
        self.StartB.setObjectName("StartB")
        ''' 
        Button Action to save open history start
        '''
        self.StartB.clicked.connect(self.checkIdInfo)
        
        ''' 
        Button Action to open history end
        '''
        self.SSN_Input = QtWidgets.QLineEdit(self.frame)
        self.SSN_Input.setEnabled(True)
        self.SSN_Input.setGeometry(QtCore.QRect(470, 100, 191, 25))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.SSN_Input.setFont(font)
        self.SSN_Input.setAutoFillBackground(False)
        self.SSN_Input.setStyleSheet("")
        self.SSN_Input.setInputMask("")
        self.SSN_Input.setFrame(True)
        self.SSN_Input.setCursorPosition(0)
        self.SSN_Input.setDragEnabled(False)
        self.SSN_Input.setReadOnly(False)
        self.SSN_Input.setPlaceholderText("")
        self.SSN_Input.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.SSN_Input.setObjectName("SSN_Input")
        self.PatientInfoT = QtWidgets.QLabel(self.frame)
        self.PatientInfoT.setGeometry(QtCore.QRect(340, 20, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.PatientInfoT.setFont(font)
        self.PatientInfoT.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PatientInfoT.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.PatientInfoT.setFrameShape(QtWidgets.QFrame.Box)
        self.PatientInfoT.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.PatientInfoT.setObjectName("PatientInfoT")
        self.NewPatient = QtWidgets.QLabel(self.frame)
        self.NewPatient.setGeometry(QtCore.QRect(240, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.NewPatient.setFont(font)
        self.NewPatient.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NewPatient.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NewPatient.setObjectName("NewPatient")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(30, 20, 161, 111))
        self.Logo.setStyleSheet("image: url(:/images/img/Logo.png);")
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.MammoB = QtWidgets.QPushButton(self.centralwidget)
        self.MammoB.setGeometry(QtCore.QRect(50, 360, 170, 95))
        self.MammoB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MammoB.setWhatsThis("")
        self.MammoB.setStyleSheet("QPushButton{\n"
"image: url(:/images/img/XRay.png);\n"
" border: 0px solid #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:checked:hover{\n"
"    border: 1px solid #4D4D4D;    \n"
"}")
        self.MammoB.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/img/Detect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MammoB.setIcon(icon)
        self.MammoB.setIconSize(QtCore.QSize(90, 90))
        self.MammoB.setFlat(True)
        self.MammoB.setObjectName("MammoB")

        
        self.SampleB = QtWidgets.QPushButton(self.centralwidget)
        self.SampleB.setGeometry(QtCore.QRect(50, 240, 170, 95))
        self.SampleB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SampleB.setWhatsThis("")
        self.SampleB.setStyleSheet("QPushButton {\n"
"image: url(:/images/img/Sample.png);\n"
" border: 0px solid #4D4D4D;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:checked:hover{\n"
"    border: 1px solid #4D4D4D;    \n"
"}")
        self.SampleB.setText("")
        self.SampleB.setIcon(icon)
        self.SampleB.setIconSize(QtCore.QSize(90, 90))
        self.SampleB.setFlat(True)
        self.SampleB.setObjectName("SampleB")
        ''' 
        ACtion for Save or Start Warnning
        '''
        self.SampleB.clicked.connect(self.OpenSampleHistory)
        self.PrintB = QtWidgets.QPushButton(self.centralwidget)
        self.PrintB.setGeometry(QtCore.QRect(50, 600, 170, 95))
        self.PrintB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PrintB.setWhatsThis("")
        self.PrintB.setStyleSheet("QPushButton{\n"
" border: 0px solid #4D4D4D;\n"
"image: url(:/newPrefix/img/Print.png);\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:checked:hover{\n"
"    border: 1px solid #4D4D4D;    \n"
"}")
        self.PrintB.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/img/Print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PrintB.setIcon(icon1)
        self.PrintB.setIconSize(QtCore.QSize(90, 90))
        self.PrintB.setFlat(True)
        self.PrintB.setObjectName("PrintB")
        ''' 
        ACtion for Save or Start Warnning
        '''
        self.PrintB.clicked.connect(self.SSWarnning)
        self.DiagnosisB = QtWidgets.QPushButton(self.centralwidget)
        self.DiagnosisB.setGeometry(QtCore.QRect(50, 120, 170, 95))
        self.DiagnosisB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DiagnosisB.setWhatsThis("")
        self.DiagnosisB.setStyleSheet("QPushButton {\n"
"image: url(:/images/img/Diagnosis.png);\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:checked:hover{\n"
"    border: 1px solid #4D4D4D;    \n"
"}")
        self.DiagnosisB.setText("")
        self.DiagnosisB.setIcon(icon)
        self.DiagnosisB.setIconSize(QtCore.QSize(90, 90))
        self.DiagnosisB.setFlat(True)
        self.DiagnosisB.setObjectName("DiagnosisB")
        self.PatientInfoB = QtWidgets.QPushButton(self.centralwidget)
        self.PatientInfoB.setGeometry(QtCore.QRect(50, 10, 170, 95))
        self.PatientInfoB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PatientInfoB.setWhatsThis("")
        self.PatientInfoB.setStyleSheet("QPushButton {\n"
"image: url(:/newPrefix/img/Patient.png);\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:checked:hover{\n"
"    border: 1px solid #4D4D4D;    \n"
"}")
        self.PatientInfoB.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/img/Patient.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PatientInfoB.setIcon(icon2)
        self.PatientInfoB.setIconSize(QtCore.QSize(180, 180))
        self.PatientInfoB.setCheckable(False)
        self.PatientInfoB.setAutoExclusive(False)
        self.PatientInfoB.setDefault(False)
        self.PatientInfoB.setFlat(True)
        self.PatientInfoB.setObjectName("PatientInfoB")
        self.Help = QtWidgets.QPushButton(self.centralwidget)
        self.Help.setGeometry(QtCore.QRect(1330, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Help.setFont(font)
        self.Help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Help.setWhatsThis("")
        self.Help.setStyleSheet("\n"
"image: url(:/images/img/Help.png);")
        self.Help.setText("")
        self.Help.setObjectName("Help")
        self.FNAB = QtWidgets.QPushButton(self.centralwidget)
        self.FNAB.setGeometry(QtCore.QRect(50, 480, 170, 95))
        self.FNAB.setStyleSheet("QPushButton{\n"
" border: 0px solid #4D4D4D;\n"
"    image: url(:/images/img/FNA.png);\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:checked:hover{\n"
"    border: 1px solid #4D4D4D;    \n"
"}")
        self.FNAB.setText("")
        self.FNAB.setObjectName("FNAB")
        self.frame.raise_()
        self.line.raise_()
        self.MammoB.raise_()
        self.SampleB.raise_()
        self.PrintB.raise_()
        self.DiagnosisB.raise_()
        self.PatientInfoB.raise_()
        self.Help.raise_()
        self.FNAB.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1380, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp_Center = QtWidgets.QAction(MainWindow)
        self.actionHelp_Center.setObjectName("actionHelp_Center")
        self.actionFAQ = QtWidgets.QAction(MainWindow)
        self.actionFAQ.setObjectName("actionFAQ")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        
        
        '''
        Button ACtion 
        
        '''
        self.PatientInfoB.clicked.connect(self.SPWarnning)
        self.MammoB.clicked.connect(self.SSWarnning)
        self.DiagnosisB.clicked.connect(self.SSWarnning)
        self.FNAB.clicked.connect(self.SSWarnning)
        self.PrintB.clicked.connect(self.DAWarnning)
        self.SampleB.clicked.connect(self.SSWarnning)
        '''
        Button ACtion 
        
        '''
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.PatientInfoB, self.DiagnosisB)
        MainWindow.setTabOrder(self.DiagnosisB, self.SampleB)
        MainWindow.setTabOrder(self.SampleB, self.MammoB)
        MainWindow.setTabOrder(self.MammoB, self.PrintB)
        MainWindow.setTabOrder(self.PrintB, self.SSN_Input)
        MainWindow.setTabOrder(self.SSN_Input, self.StartB)
        MainWindow.setTabOrder(self.StartB, self.FirstNameI)
        MainWindow.setTabOrder(self.FirstNameI, self.FamilyNameI)
        MainWindow.setTabOrder(self.FamilyNameI, self.SSNI)
        MainWindow.setTabOrder(self.SSNI, self.PhoneNoI)
        MainWindow.setTabOrder(self.PhoneNoI, self.dateEdit)
        MainWindow.setTabOrder(self.dateEdit, self.Female)
        MainWindow.setTabOrder(self.Female, self.Male)
        MainWindow.setTabOrder(self.Male, self.cancero)
        MainWindow.setTabOrder(self.cancero, self.nocancero)
        MainWindow.setTabOrder(self.nocancero, self.diabeteso)
        MainWindow.setTabOrder(self.diabeteso, self.nodiabeteso)
        MainWindow.setTabOrder(self.nodiabeteso, self.bloodpo)
        MainWindow.setTabOrder(self.bloodpo, self.nobloodpo)
        MainWindow.setTabOrder(self.nobloodpo, self.anemiao)
        MainWindow.setTabOrder(self.anemiao, self.noanemiao)
        MainWindow.setTabOrder(self.noanemiao, self.SaveB)
        MainWindow.setTabOrder(self.SaveB, self.Help)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patient Information"))
        self.frame.setStatusTip(_translate("MainWindow", "show patient history and start"))
        self.frame.setWhatsThis(_translate("MainWindow", "start investigate"))
        self.FirstName.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">First Name :</span></p></body></html>"))
        self.SaveB.setToolTip(_translate("MainWindow", "save"))
        self.SaveB.setStatusTip(_translate("MainWindow", "save information of new patient"))
        self.SaveB.setText(_translate("MainWindow", "Save"))
        self.SaveB.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.PhoneNo.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Patient SSN  :</span></p></body></html>"))
        self.Age.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">BirthDate :</span></p></body></html>"))
        self.LastName.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Family Name :</span></p></body></html>"))
        self.Gender.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Gender :</span></p></body></html>"))
        self.PhoneNo_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Phone Number :</span></p></body></html>"))
        self.Hint.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">you must enter all fields.</p></body></html>"))
        self.Age_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Have Diabetes ?</span></p></body></html>"))
        self.Age_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Have Blood Pressure ?</span></p></body></html>"))
        self.Age_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Have Cancer before ?</span></p></body></html>"))
        self.Age_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Have Anemia ?</span></p></body></html>"))
        self.Female.setText(_translate("MainWindow", "Female"))
        self.Male.setText(_translate("MainWindow", "Male"))
        self.cancero.setText(_translate("MainWindow", "Yes"))
        self.nocancero.setText(_translate("MainWindow", "No"))
        self.diabeteso.setText(_translate("MainWindow", "Yes"))
        self.nodiabeteso.setText(_translate("MainWindow", "No"))
        self.bloodpo.setText(_translate("MainWindow", "Yes"))
        self.nobloodpo.setText(_translate("MainWindow", "No"))
        self.anemiao.setText(_translate("MainWindow", "Yes"))
        self.noanemiao.setText(_translate("MainWindow", "No"))
        self.PatientSSN.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600; color:#4d4d4d;\">Patient SSN :</span></p></body></html>"))
        self.StartB.setToolTip(_translate("MainWindow", "Start"))
        self.StartB.setStatusTip(_translate("MainWindow", "show patient history and start the investigation"))
        self.StartB.setText(_translate("MainWindow", "Start"))
        self.StartB.setShortcut(_translate("MainWindow", "Enter"))
        self.PatientInfoT.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#4d4d4d;\">Patient Information</span></p></body></html>"))
        self.NewPatient.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#4d4d4d;\">New Patient</span></p></body></html>"))
        self.MammoB.setToolTip(_translate("MainWindow", "Mammography Mass"))
        self.MammoB.setStatusTip(_translate("MainWindow", "Detect tumor by Mammography"))
        self.SampleB.setToolTip(_translate("MainWindow", "Sample detect"))
        self.SampleB.setStatusTip(_translate("MainWindow", "detect tumor by sample and determine the recurrence "))
        self.PrintB.setToolTip(_translate("MainWindow", "Print"))
        self.PrintB.setStatusTip(_translate("MainWindow", "Print patient report"))
        self.DiagnosisB.setToolTip(_translate("MainWindow", "Diagnosis"))
        self.DiagnosisB.setStatusTip(_translate("MainWindow", "show if patient have tumor or not "))
        self.PatientInfoB.setToolTip(_translate("MainWindow", "Patient Information"))
        self.PatientInfoB.setStatusTip(_translate("MainWindow", "external and internal patient page"))
        self.Help.setToolTip(_translate("MainWindow", "Help"))
        self.Help.setStatusTip(_translate("MainWindow", "Need a help ? go to help center."))
        self.Help.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.FNAB.setToolTip(_translate("MainWindow", "Fine Needle Aspirate"))
        self.FNAB.setStatusTip(_translate("MainWindow", "Detect Tumor by Fine Needle Aspirate (FNA)"))
        self.actionHelp_Center.setText(_translate("MainWindow", "Help Center"))
        self.actionHelp_Center.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionFAQ.setText(_translate("MainWindow", "FAQ"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))

import img

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


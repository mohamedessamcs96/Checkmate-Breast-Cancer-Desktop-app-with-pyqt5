# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HistoryB.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from Diagnosis import Ui_Diagnosis
class Ui_HistoryBlood(object):
    global connection, PatientID
    PatientID=""
    connection=sqlite3.connect("sqlitedatabase5.db")   



        #I Call it when the account and the password of the user is match
    def openDiagnosisWindowPage(self):
            #Create an object from two classes the qtgui and qmain window is inside
            self.selectWindow=QtWidgets.QMainWindow()
            self.ui=Ui_Diagnosis()
            self.ui.setupUi(self.selectWindow)
            self.selectWindow.show()
    """
    Def show message Box
    """
    def loadData(self):
        Patient =connection.execute("SELECT * FROM PATIENT WHERE PATIENTID=? ",(PatientID,))
        
        #Patient =connection.execute("SELECT * FROM PATIENT WHERE PATIENTID=1234 ")
        for row_number in Patient.fetchall():
                    global fname,familyname,ssnn,phonen,birthdate,gender,cancer,diabetes,bloodpressure,anemia
                    data=row_number
                    fname=data[0]
                    familyname=data[1]
                    ssnn=data[2]
                    phonen=data[3]
                    birthdate=data[4]
                    gender=data[5]
                    cancer=data[6]
                    diabetes=data[7]
                    bloodpressure=data[8]
                    anemia=data[9]
                    
                    print(data[0])
                    print(data[1])
                    print(data[2])
                    print(data[3])
                    print(data[4])
                    print(data[5])
                    print(data[6])
                    print(data[7])
                    print(data[8])
                    print(data[9])

                    
    def ShowMessageBox(self,title,message):
        messagebox=QtWidgets.QMessageBox()
        messagebox.setIcon(QtWidgets.QMessageBox.Warning)
        messagebox.setWindowTitle(title)
        messagebox.setText(message)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messagebox.exec_()
                    

    

    def loadtableData(self):
        print(PatientID)   
        result2 =connection.execute("SELECT DATE,BLOODRESULT,BMI,LEPTIN,GLUCOSE,ADIPONECTIN,INSULIN,RESISTINT,HOMA,MCP FROM BLOODANALYSIS WHERE PATIENTID=? ",(PatientID,))
                                                                                  
        #result2 =connection.execute("SELECT DATE,BLOODRESULT,BMI,LEPTIN,GLUCOSE,ADIPONECTIN,
        #INSULIN,RESISTINT,HOMA,MCP FROM BLOODANALYSIS  WHERE PATIENTID=? ",(PatientID,))
        
        print(result2)
        self.BloodL.setRowCount(0)
        for row_number,row_data in enumerate(result2):
            self.BloodL.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.BloodL.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))    
        
            
    
    
    def DAWarnning(self):
        self.ShowMessageBox('Warning',"This Page doesn't available for you ")
    
    
    def SSWarnning(self):
        self.ShowMessageBox('Warning',"Wrong Choice,Check if the patient is registerd or add new patient")
    
    
    def SPWarnning(self):
        self.ShowMessageBox('Warning',"You are in the same page")
    
    def setupUi(self, MainWindow):
        self.loadData()
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
        self.PatientInfoF = QtWidgets.QFrame(self.frame)
        self.PatientInfoF.setGeometry(QtCore.QRect(210, 90, 621, 171))
        self.PatientInfoF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PatientInfoF.setFrameShadow(QtWidgets.QFrame.Plain)
        self.PatientInfoF.setObjectName("PatientInfoF")
        self.FirstName = QtWidgets.QLabel(self.PatientInfoF)
        self.FirstName.setGeometry(QtCore.QRect(25, 1, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.FirstName.setFont(font)
        self.FirstName.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.FirstName.setObjectName("FirstName")
        self.PhoneNo = QtWidgets.QLabel(self.PatientInfoF)
        self.PhoneNo.setGeometry(QtCore.QRect(25, 31, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.PhoneNo.setFont(font)
        self.PhoneNo.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PhoneNo.setObjectName("PhoneNo")
        self.Age = QtWidgets.QLabel(self.PatientInfoF)
        self.Age.setGeometry(QtCore.QRect(25, 65, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Age.setFont(font)
        self.Age.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Age.setObjectName("Age")
        self.Gender = QtWidgets.QLabel(self.PatientInfoF)
        self.Gender.setGeometry(QtCore.QRect(25, 134, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.Gender.setFont(font)
        self.Gender.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Gender.setObjectName("Gender")
        self.PhoneNo_2 = QtWidgets.QLabel(self.PatientInfoF)
        self.PhoneNo_2.setGeometry(QtCore.QRect(25, 101, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.PhoneNo_2.setFont(font)
        self.PhoneNo_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PhoneNo_2.setObjectName("PhoneNo_2")
        self.FirstNamel = QtWidgets.QLabel(self.PatientInfoF)
        self.FirstNamel.setGeometry(QtCore.QRect(80, 2, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.FirstNamel.setFont(font)
        self.FirstNamel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.FirstNamel.setObjectName("FirstNamel")
        self.ssnl = QtWidgets.QLabel(self.PatientInfoF)
        self.ssnl.setGeometry(QtCore.QRect(73, 32, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.ssnl.setFont(font)
        self.ssnl.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.ssnl.setObjectName("ssnl")
        self.birthdatel = QtWidgets.QLabel(self.PatientInfoF)
        self.birthdatel.setGeometry(QtCore.QRect(109, 66, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.birthdatel.setFont(font)
        self.birthdatel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.birthdatel.setObjectName("birthdatel")
        self.familynamel = QtWidgets.QLabel(self.PatientInfoF)
        self.familynamel.setGeometry(QtCore.QRect(180, 2, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.familynamel.setFont(font)
        self.familynamel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.familynamel.setObjectName("familynamel")
        self.genderl = QtWidgets.QLabel(self.PatientInfoF)
        self.genderl.setGeometry(QtCore.QRect(95, 135, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.genderl.setFont(font)
        self.genderl.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.genderl.setObjectName("genderl")
        self.phonel = QtWidgets.QLabel(self.PatientInfoF)
        self.phonel.setGeometry(QtCore.QRect(149, 101, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.phonel.setFont(font)
        self.phonel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.phonel.setObjectName("phonel")
        self.cancerl = QtWidgets.QLabel(self.PatientInfoF)
        self.cancerl.setGeometry(QtCore.QRect(540, 7, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.cancerl.setFont(font)
        self.cancerl.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cancerl.setObjectName("cancerl")
        self.cancerQ = QtWidgets.QLabel(self.PatientInfoF)
        self.cancerQ.setGeometry(QtCore.QRect(350, 1, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.cancerQ.setFont(font)
        self.cancerQ.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cancerQ.setObjectName("cancerQ")
        self.PressureQ = QtWidgets.QLabel(self.PatientInfoF)
        self.PressureQ.setGeometry(QtCore.QRect(357, 61, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.PressureQ.setFont(font)
        self.PressureQ.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PressureQ.setObjectName("PressureQ")
        self.AnemiaQ = QtWidgets.QLabel(self.PatientInfoF)
        self.AnemiaQ.setGeometry(QtCore.QRect(350, 91, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.AnemiaQ.setFont(font)
        self.AnemiaQ.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.AnemiaQ.setObjectName("AnemiaQ")
        self.DiabetesQ = QtWidgets.QLabel(self.PatientInfoF)
        self.DiabetesQ.setGeometry(QtCore.QRect(350, 31, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.DiabetesQ.setFont(font)
        self.DiabetesQ.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.DiabetesQ.setObjectName("DiabetesQ")
        self.anemial = QtWidgets.QLabel(self.PatientInfoF)
        self.anemial.setGeometry(QtCore.QRect(540, 100, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.anemial.setFont(font)
        self.anemial.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.anemial.setObjectName("anemial")
        self.diabetesl = QtWidgets.QLabel(self.PatientInfoF)
        self.diabetesl.setGeometry(QtCore.QRect(540, 38, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.diabetesl.setFont(font)
        self.diabetesl.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.diabetesl.setObjectName("diabetesl")
        self.pressurel = QtWidgets.QLabel(self.PatientInfoF)
        self.pressurel.setGeometry(QtCore.QRect(540, 69, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(8)
        self.pressurel.setFont(font)
        self.pressurel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.pressurel.setObjectName("pressurel")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(30, 20, 161, 111))
        self.Logo.setStyleSheet("image: url(:/images/img/Logo.png);")
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.PatientHistoryT = QtWidgets.QLabel(self.frame)
        self.PatientHistoryT.setGeometry(QtCore.QRect(349, 20, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.PatientHistoryT.setFont(font)
        self.PatientHistoryT.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.PatientHistoryT.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.PatientHistoryT.setFrameShape(QtWidgets.QFrame.Box)
        self.PatientHistoryT.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.PatientHistoryT.setObjectName("PatientHistoryT")
        self.BloodL = QtWidgets.QTableWidget(self.frame)
        self.BloodL.setGeometry(QtCore.QRect(10, 280, 1021, 321))
        self.BloodL.setColumnCount(10)
        self.BloodL.setObjectName("BloodL")
        self.BloodL.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.BloodL.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.BloodL.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.BloodL.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.BloodL.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.BloodL.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.BloodL.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.BloodL.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.BloodL.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.BloodL.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.BloodL.setHorizontalHeaderItem(9, item)
        self.BloodL.horizontalHeader().setDefaultSectionSize(120)
        self.BloodL.horizontalHeader().setMinimumSectionSize(30)
        self.BloodL.verticalHeader().setMinimumSectionSize(19)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.PatientInfoB, self.DiagnosisB)
        MainWindow.setTabOrder(self.DiagnosisB, self.SampleB)
        MainWindow.setTabOrder(self.SampleB, self.MammoB)
        MainWindow.setTabOrder(self.MammoB, self.PrintB)
        MainWindow.setTabOrder(self.PrintB, self.Help)
        


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Blood analysis patient history"))
        self.frame.setStatusTip(_translate("MainWindow", "show patient history and start"))
        self.frame.setWhatsThis(_translate("MainWindow", "start investigate"))
        self.FirstName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\">Name :</span></p></body></html>"))
        self.PhoneNo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\">SSN :</span></p></body></html>"))
        self.Age.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\">BirthDate :</span></p></body></html>"))
        self.Gender.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\">Gender :</span></p></body></html>"))
        self.PhoneNo_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\">Phone Number :</span></p></body></html>"))
        #self.FirstNamel.setText(_translate("MainWindow", "<html><head/><body><p>first name</p></body></html>"))
        #self.ssnl.setText(_translate("MainWindow", "<html><head/><body><p>ssn</p></body></html>"))
        #self.Birthdatel.setText(_translate("MainWindow", "<html><head/><body><p>birthdate</p></body></html>"))
        #self.familynamel.setText(_translate("MainWindow", "<html><head/><body><p>family name</p></body></html>"))
        #self.genderl.setText(_translate("MainWindow", "<html><head/><body><p>gender</p></body></html>"))
        #self.phonel.setText(_translate("MainWindow", "<html><head/><body><p>phone no.</p></body></html>"))
        #self.cancerl.setText(_translate("MainWindow", "<html><head/><body><p>cancer</p></body></html>"))
        self.cancerQ.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Have Cancer before </span></p></body></html>"))
        self.PressureQ.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Have Blood Pressure </span></p></body></html>"))
        self.AnemiaQ.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Have Anemia </span></p></body></html>"))
        self.DiabetesQ.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#4d4d4d;\">Have Diabetes </span></p></body></html>"))
        #self.anemial.setText(_translate("MainWindow", "<html><head/><body><p>anemia</p></body></html>"))
        #self.diabetesl.setText(_translate("MainWindow", "<html><head/><body><p>Diabetes</p></body></html>"))
        #self.pressurel.setText(_translate("MainWindow", "<html><head/><body><p>pressure</p></body></html>"))
        self.PatientHistoryT.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#4d4d4d;\">Patient History</span></p></body></html>"))
        self.FirstNamel.setText(fname)
        self.anemial.setText(anemia)    
        self.pressurel.setText(bloodpressure)  
        self.diabetesl.setText(diabetes)
        self.cancerl.setText(cancer)
        self.phonel.setText(phonen)
        self.genderl.setText(gender)
        self.familynamel.setText(familyname)
        self.birthdatel.setText(birthdate)
        self.ssnl.setText(PatientID)        
         
        
        '''
        Button ACtion 
        
        '''
        self.PatientInfoB.clicked.connect(self.DAWarnning)
        self.MammoB.clicked.connect(self.DAWarnning)
        self.DiagnosisB.clicked.connect(self.openDiagnosisWindowPage)
        self.FNAB.clicked.connect(self.DAWarnning)
        self.PrintB.clicked.connect(self.DAWarnning)
        self.SampleB.clicked.connect(self.DAWarnning)
        '''
        Button ACtion 
        
        '''
        
        self.loadtableData()
        
        
        item = self.BloodL.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.BloodL.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Blood Result"))
        item = self.BloodL.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "BMI"))
        item = self.BloodL.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Glucose"))
        item = self.BloodL.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Insulin"))
        item = self.BloodL.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "HOMA"))
        item = self.BloodL.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Adiponectin"))
        item = self.BloodL.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Resistin"))
        item = self.BloodL.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Mcp1"))
        item = self.BloodL.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Leptin"))
        self.MammoB.setToolTip(_translate("MainWindow", "Mammography Mass"))
        self.MammoB.setStatusTip(_translate("MainWindow", "Detect tumor by Mammography"))
        self.SampleB.setToolTip(_translate("MainWindow", "Sample detect"))
        self.SampleB.setStatusTip(_translate("MainWindow", "detect tumor by sample "))
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
    ui = Ui_HistoryBlood()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Diagnosis2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from PatientInfo import Ui_MainWindow
import sqlite3
from sklearn.externals import joblib
import csv
from datetime import date
import time
from datetime import datetime
import datetime
import pandas as pd
import numpy as np
#from datetime import year
class Ui_Diagnosis(object):
    global PatientID ,connection,result,BMIResult,lastyear,Currentyear,Age,doctorname,time,date
    PatientID=""
    doctorname=""
    connection=sqlite3.connect("sqlitedatabase5.db")    
    
    
 
    
    now = datetime.datetime.now()
    date=str(now.day)+'/'+str(now.month)+'/'+str(now.year)
    time=str(now.hour)+':'+str(now.minute)
    print(time)

    def BMICalculation(self):
        height=self.lineEdit_5.text()
        weight=self.lineEdit_6.text()
        BMIResult=((float(height))*(float(weight)))
        self.BMIResult.setText(repr(BMIResult))
        self.BMIResult.setGeometry(QtCore.QRect(70, 133, 81, 16))

    
    def Machinelearning(self):
        print("Diagnosis Page,ML Function")
        print(type(PatientID))
        global BMI,Leptin,Glucose,Adiponectin,Insulin,Resistin,HOMA,MCP,result,Age,Notes
        BMI=float(self.lineEdit.text())
        Leptin =float(self.lineEdit_13.text())
        Glucose=float(self.lineEdit_2.text())
        Adiponectin =float(self.lineEdit_7.text())
        Insulin =float(self.lineEdit_3.text())
        Resistin =float(self.lineEdit_8.text())
        HOMA=(float(Glucose)*float(Insulin))
        MCP =float(self.lineEdit_9.text())
        Notes=self.lineEdit_4.toPlainText()
        def age():
            #Birthdate=connection.execute("SELECT BIRTHDATE FROM PATIENT WHERE PATIENTID='123'")
            Birthdate=connection.execute("SELECT BIRTHDATE FROM PATIENT WHERE PATIENTID=?",(PatientID,))
            global data ,Output
            for row_number in Birthdate.fetchall():
                data=row_number[0]
                print(data)
            yeardate=data.split('/')
            Patientyear=int(yeardate[2])
            now = datetime.datetime.now()
            Currentyear=now.year
            return Currentyear-Patientyear    
        Age=age()
        print(Age)
        
        clf=joblib.load('bloodmodel')
        Blood_data=[[Age,BMI,Leptin,Glucose,Adiponectin,Insulin,Resistin,HOMA,MCP]]
        prediction=clf.predict(Blood_data)
        
        for i in range(len(prediction)):
            if(prediction[i]==1):
                global Output
                print("The tumor is Healthy")
                Output="Healthy controls"
                self.ShowMessageBox('Diagnosis','The Diagnosis of this Analysis say that this person is: Health controll')

            elif(prediction[i]==2):
                print("The tumor is Patient")
                Output="Patient"        
                self.ShowMessageBox('Diagnosis','The Diagnosis of this Analysis say that this person is: Patient')
        self.PrintReport()
        self.dataHistory()
        self.UpdatingDataset()
    def dataHistory(self):
        global BMI,Leptin,Glucose,Adiponectin,Insulin,Resistin,HOMA,MCP,result
        BMI=float(self.lineEdit.text())
        Leptin =float(self.lineEdit_13.text())
        Glucose=float(self.lineEdit_2.text())
        Adiponectin =float(self.lineEdit_7.text())
        Insulin =float(self.lineEdit_3.text())
        Resistin =float(self.lineEdit_8.text())
        HOMA=(float(Glucose)*float(Insulin))
        MCP =float(self.lineEdit_9.text())
        
        unix=time
        #currentdate=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))   
        #print(currentdate)
        connection.execute('INSERT INTO BLOODANALYSIS(DATE,BLOODRESULT,BMI,LEPTIN,GLUCOSE,ADIPONECTIN,INSULIN,RESISTINT,HOMA,MCP,PATIENTID) VALUES(?,?,?,?,?,?,?,?,?,?,?) ',(unix,Output,BMI,Leptin,
                           Glucose,Adiponectin,Insulin,Resistin,HOMA,MCP,PatientID,))
        connection.commit()
    
        
    def UpdatingDataset(self):
        
            '''Making a dataset from scractch '''
        
            with open('Blood_Dataset.csv', mode='a',) as new_data:
                X = csv.writer(new_data, delimiter=',')
                X.writerow([Age,BMI,Leptin,Glucose,Adiponectin,Insulin,Resistin,HOMA,MCP])
                new_data.close()
                
            '''adding the features to the newest dataset '''
            with open('updated_prepared_Blood Analysis.csv', mode='a',) as new_data:
                X = csv.writer(new_data, delimiter=',')
                X.writerow([Age,BMI,Leptin,Glucose,Adiponectin,Insulin,Resistin,HOMA,MCP])
                new_data.close()
            

            
    
    def DAWarnning(self):
        self.ShowMessageBox('Warning',"This Page doesn't available for you ")
    
    
    def SSWarnning(self):
        self.ShowMessageBox('Warning',"Wrong Choice,Check if the patient is registerd or add new patient")
    
    
    def SPWarnning(self):
        self.ShowMessageBox('Warning',"You are in the same page")
 
    def PrintReport(self):
        import fpdf
        from fpdf import FPDF
        patientdata=connection.execute('SELECT * FROM PATIENT WHERE PATIENTID=?',(PatientID,))
        for row_number in patientdata.fetchall():
            fname=row_number[0]
            lname=row_number[1]
            ssni=row_number[2]
            #Birhdate=row_number[4]
            gender=row_number[5]
            print(row_number)
        name=fname+' '+lname

        #print(date)
        pdf=FPDF()
        pdf.add_page()
        pdf.set_author('Check Mate Breast Cancer')
        #pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
        
        
        pdf.image('Logo.png', 10, 8, 33)
        # Arial bold 15
        pdf.set_font('Arial', 'B', 20)
        pdf.cell(70)
        pdf.write(30, 'Patient Report')
        pdf.ln(5)
    
      
        #Date
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(80, 'Date:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(80,time)
        #Time in
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(100)
        pdf.write(80, 'Time in:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(80, date)
            
        pdf.ln(5)
        #Location
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(83, 'Location:')
        pdf.set_font('Arial', '', 10)
        pdf.write(83, 'HTI Cancer Hospital')
        pdf.ln(5)
            
        #Patient details Title
        pdf.set_font('Arial', '', 15)
        pdf.cell(5)
        pdf.write(100, 'Patient details')
        pdf.set_font('Arial', '', 13)
        '''    ###############################################'''  
        #Their information
        #Date
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(110, 'Name:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(110, name)
        #Time in
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(105)
        pdf.write(110, 'Age:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(110,str(Age))
        
        pdf.ln(5)
        #Location
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(115, 'SSN:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(115,str(ssni))
        pdf.ln(5) 
        pdf.cell(5)
        #Location
        pdf.cell(130)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(105, 'Gender:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(105,str(gender))
        pdf.ln(5)  
        '''    ###############################################'''  
        #Their information
        #Date
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(125, 'BMI:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(125,str(BMI))
        #Time in
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(125)
        pdf.write(125, 'Leptin:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(125,str(Leptin))
        
        pdf.ln(5)
        #Location
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(130, 'Glucose:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(130,str(Glucose))
        pdf.ln(5)
            
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(140)
        pdf.write(120, 'Adiponectin:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(120,str(Adiponectin))
        pdf.ln(3)
            
        '''    ###############################################'''  
        #Their information
        #Date
        
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(128, 'Insulin:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(128,str(Insulin))
        #Time in
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(125)
        pdf.write(128, 'Resistin:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(128,str(Resistin))
        
        pdf.ln(5)
        #Location
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(133, 'HOMA:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(133,str(HOMA))
        pdf.ln(5)
        
        #Location
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(133, 'MCP:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(133,str(MCP))
        pdf.ln(5) 
                    
        '''    ###############################################'''  
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(140,'Result:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(140,Output)
        #Time in
        
        pdf.ln(5)
                #Location
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(160, 'Notes:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(170,str(Notes))
        pdf.ln(5)            
        
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(125)
        pdf.write(180, 'Doctor:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(180,doctorname)
        pdf.ln(3)       
    
   
        pdf.output('PatientBloodAnalysisReport.pdf', 'F')
        import os 
        os.startfile("PatientBloodAnalysisReport.pdf")      
    def ShowMessageBox(self,title,message):
        messagebox=QtWidgets.QMessageBox()
        messagebox.setIcon(QtWidgets.QMessageBox.Warning)
        messagebox.setWindowTitle(title)
        messagebox.setText(message)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messagebox.exec_()    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1503, 758)
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
        self.BloodAnalysisT = QtWidgets.QLabel(self.frame)
        self.BloodAnalysisT.setGeometry(QtCore.QRect(318, 120, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.BloodAnalysisT.setFont(font)
        self.BloodAnalysisT.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.BloodAnalysisT.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.BloodAnalysisT.setFrameShape(QtWidgets.QFrame.Box)
        self.BloodAnalysisT.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BloodAnalysisT.setObjectName("BloodAnalysisT")
        self.BloodF = QtWidgets.QFrame(self.frame)
        self.BloodF.setGeometry(QtCore.QRect(240, 140, 501, 421))
        self.BloodF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BloodF.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BloodF.setObjectName("BloodF")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.BloodF)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 110, 109, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_11 = QtWidgets.QLabel(self.BloodF)
        self.label_11.setGeometry(QtCore.QRect(240, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.DiagnoseB = QtWidgets.QPushButton(self.BloodF)
        self.DiagnoseB.setGeometry(QtCore.QRect(110, 330, 110, 30))
        self.DiagnoseB.clicked.connect(self.Machinelearning)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.DiagnoseB.setFont(font)
        self.DiagnoseB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DiagnoseB.setStatusTip("")
        self.DiagnoseB.setWhatsThis("")
        self.DiagnoseB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.DiagnoseB.setObjectName("DiagnoseB")
        self.label_8 = QtWidgets.QLabel(self.BloodF)
        self.label_8.setGeometry(QtCore.QRect(270, 210, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.BloodF)
        self.label_9.setGeometry(QtCore.QRect(30, 60, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.ResetB = QtWidgets.QPushButton(self.BloodF)
        self.ResetB.setGeometry(QtCore.QRect(300, 330, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ResetB.setFont(font)
        self.ResetB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResetB.setWhatsThis("")
        self.ResetB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.ResetB.setObjectName("ResetB")
        self.lineEdit = QtWidgets.QLineEdit(self.BloodF)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 109, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_13 = QtWidgets.QLabel(self.BloodF)
        self.label_13.setGeometry(QtCore.QRect(30, 210, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.BloodF)
        self.label_14.setGeometry(QtCore.QRect(30, 110, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.BloodF)
        self.lineEdit_7.setGeometry(QtCore.QRect(340, 110, 109, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.BloodF)
        self.lineEdit_9.setGeometry(QtCore.QRect(340, 210, 109, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_7 = QtWidgets.QLabel(self.BloodF)
        self.label_7.setGeometry(QtCore.QRect(30, 160, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.BloodF)
        self.lineEdit_13.setGeometry(QtCore.QRect(340, 60, 109, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setStyleSheet("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.BloodF)
        self.lineEdit_8.setGeometry(QtCore.QRect(340, 160, 109, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_10 = QtWidgets.QLabel(self.BloodF)
        self.label_10.setGeometry(QtCore.QRect(270, 60, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.BloodF)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 160, 109, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_12 = QtWidgets.QLabel(self.BloodF)
        self.label_12.setGeometry(QtCore.QRect(270, 160, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.frame_2 = QtWidgets.QFrame(self.BloodF)
        self.frame_2.setGeometry(QtCore.QRect(15, 370, 221, 41))
        self.frame_2.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Hint = QtWidgets.QLabel(self.frame_2)
        self.Hint.setGeometry(QtCore.QRect(38, 10, 171, 21))
        self.Hint.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Hint.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.Hint.setObjectName("Hint")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(22, 10, 21, 21))
        self.label.setStyleSheet("image: url(:/images/img/Hint.png);\n"
"background-color: rgb(242, 242, 242);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame_5 = QtWidgets.QFrame(self.BloodF)
        self.frame_5.setGeometry(QtCore.QRect(99, 210, 109, 22))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(11, 3, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_18 = QtWidgets.QLabel(self.BloodF)
        self.label_18.setGeometry(QtCore.QRect(20, 260, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.lineEdit_4 = QtWidgets.QPlainTextEdit(self.BloodF)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 250, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(30, 20, 161, 111))
        self.Logo.setStyleSheet("image: url(:/images/img/Logo.png);")
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.calculationF = QtWidgets.QFrame(self.frame)
        self.calculationF.setGeometry(QtCore.QRect(40, 250, 161, 161))
        self.calculationF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calculationF.setFrameShadow(QtWidgets.QFrame.Raised)
        self.calculationF.setObjectName("calculationF")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.calculationF)
        self.lineEdit_5.setGeometry(QtCore.QRect(65, 23, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.calculationF)
        self.lineEdit_6.setGeometry(QtCore.QRect(65, 53, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.CalculateB = QtWidgets.QPushButton(self.calculationF)
        self.CalculateB.setGeometry(QtCore.QRect(39, 88, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.CalculateB.setFont(font)
        self.CalculateB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CalculateB.setStatusTip("")
        self.CalculateB.setWhatsThis("")
        self.CalculateB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.CalculateB.setObjectName("CalculateB")
        self.CalculateB.clicked.connect(self.BMICalculation)
        self.label_17 = QtWidgets.QLabel(self.calculationF)
        self.label_17.setGeometry(QtCore.QRect(11, 53, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(self.calculationF)
        self.label_16.setGeometry(QtCore.QRect(16, 23, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.BMIResult = QtWidgets.QLabel(self.calculationF)
        self.BMIResult.setGeometry(QtCore.QRect(43, 133, 81, 16))
        self.BMIResult.setObjectName("BMIResult")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(61, 230, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 570, 281, 41))
        self.frame_3.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Hint_2 = QtWidgets.QLabel(self.frame_3)
        self.Hint_2.setGeometry(QtCore.QRect(37, 11, 231, 20))
        self.Hint_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Hint_2.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.Hint_2.setObjectName("Hint_2")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.label_4.setStyleSheet("image: url(:/images/img/Hint.png);\n"
"background-color: rgb(242, 242, 242);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.Obacity.raise_()
        self.BloodF.raise_()
        self.BloodAnalysisT.raise_()
        self.Logo.raise_()
        self.calculationF.raise_()
        self.label_15.raise_()
        self.frame_3.raise_()
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/img/Detect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SampleB.setIcon(icon)
        self.SampleB.setIconSize(QtCore.QSize(90, 90))
        self.SampleB.setFlat(True)
        self.SampleB.setObjectName("SampleB")
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
        self.MammoB.setIcon(icon)
        self.MammoB.setIconSize(QtCore.QSize(90, 90))
        self.MammoB.setFlat(True)
        self.MammoB.setObjectName("MammoB")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1503, 21))
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
        self.ResetB.clicked.connect(self.lineEdit.clear)
        self.ResetB.clicked.connect(self.lineEdit_2.clear)
        self.ResetB.clicked.connect(self.lineEdit_3.clear)
        self.ResetB.clicked.connect(self.lineEdit_13.clear)
        self.ResetB.clicked.connect(self.lineEdit_7.clear)
        self.ResetB.clicked.connect(self.lineEdit_8.clear)
        self.ResetB.clicked.connect(self.lineEdit_9.clear)
        self.ResetB.clicked.connect(self.lineEdit_4.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.PatientInfoB, self.DiagnosisB)
        MainWindow.setTabOrder(self.DiagnosisB, self.SampleB)
        MainWindow.setTabOrder(self.SampleB, self.MammoB)
        MainWindow.setTabOrder(self.MammoB, self.FNAB)
        MainWindow.setTabOrder(self.FNAB, self.PrintB)
        MainWindow.setTabOrder(self.PrintB, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_13)
        MainWindow.setTabOrder(self.lineEdit_13, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        MainWindow.setTabOrder(self.lineEdit_8, self.lineEdit_9)
        MainWindow.setTabOrder(self.lineEdit_9, self.DiagnoseB)
        MainWindow.setTabOrder(self.DiagnoseB, self.ResetB)
        MainWindow.setTabOrder(self.ResetB, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.CalculateB)
        MainWindow.setTabOrder(self.CalculateB, self.Help)


        '''
        Button ACtion 
        
        '''
        self.PatientInfoB.clicked.connect(self.DAWarnning)
        self.MammoB.clicked.connect(self.DAWarnning)
        self.DiagnosisB.clicked.connect(self.SPWarnning)
        self.FNAB.clicked.connect(self.DAWarnning)
        self.PrintB.clicked.connect(self.DAWarnning)
        self.SampleB.clicked.connect(self.DAWarnning)
        '''
        Button ACtion 
        
        '''
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BloodAnalysisT.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#4d4d4d;\">Blood Analysis</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Adiponectin :"))
        self.DiagnoseB.setToolTip(_translate("MainWindow", "Diagnose"))
        self.DiagnoseB.setText(_translate("MainWindow", "Diagnose"))
        self.DiagnoseB.setShortcut(_translate("MainWindow", "Enter"))
        self.label_8.setText(_translate("MainWindow", "MCP.1 :"))
        self.label_9.setText(_translate("MainWindow", "BMI :"))
        self.ResetB.setToolTip(_translate("MainWindow", "Reset"))
        self.ResetB.setStatusTip(_translate("MainWindow", "Reset all fields"))
        self.ResetB.setText(_translate("MainWindow", "Reset"))
        self.ResetB.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.label_13.setText(_translate("MainWindow", "HOMA :"))
        self.label_14.setText(_translate("MainWindow", "Glucose :"))
        self.label_7.setText(_translate("MainWindow", "Insulin :"))
        self.label_10.setText(_translate("MainWindow", "Leptin :"))
        self.label_12.setText(_translate("MainWindow", "Resistin :"))
        self.Hint.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">you must enter all fields.</span></p></body></html>"))
        self.label_3.setStatusTip(_translate("MainWindow", "HOMA feature is calculated by (Glucose*Insulin)"))
        self.label_3.setText(_translate("MainWindow", " Glucose * Insulin"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Notes:</span></p></body></html>"))
        self.calculationF.setStatusTip(_translate("MainWindow", "BMI Calculation which calculate the body mass \"BMI\" by the patient Height and Weight (BMI=Height/(Weight)^2)"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "centimeters"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Kilograms"))
        self.CalculateB.setToolTip(_translate("MainWindow", "calculate"))
        self.CalculateB.setText(_translate("MainWindow", "Calculate"))
        self.CalculateB.setShortcut(_translate("MainWindow", "Enter"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Weight :</p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Height :</p></body></html>"))
        self.BMIResult.setText(_translate("MainWindow", "Result is here..."))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">BMI Calculation</p></body></html>"))
        self.Hint_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">These features are include patient age</span></p></body></html>"))
        self.Help.setToolTip(_translate("MainWindow", "Help"))
        self.Help.setStatusTip(_translate("MainWindow", "Need a help ? go to help center."))
        self.Help.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.SampleB.setToolTip(_translate("MainWindow", "Sample detect"))
        self.SampleB.setStatusTip(_translate("MainWindow", "detect tumor by sample "))
        self.MammoB.setToolTip(_translate("MainWindow", "Mammography Mass"))
        self.MammoB.setStatusTip(_translate("MainWindow", "Detect tumor by Mammography"))
        self.FNAB.setToolTip(_translate("MainWindow", "Fine Needle Aspirate"))
        self.FNAB.setStatusTip(_translate("MainWindow", "Detect Tumor by Fine Needle Aspirate (FNA)"))
        self.PrintB.setToolTip(_translate("MainWindow", "Print"))
        self.PrintB.setStatusTip(_translate("MainWindow", "Print patient report"))
        self.DiagnosisB.setToolTip(_translate("MainWindow", "Diagnosis"))
        self.DiagnosisB.setStatusTip(_translate("MainWindow", "show if patient have tumor or not "))
        self.PatientInfoB.setToolTip(_translate("MainWindow", "Patient Information"))
        self.PatientInfoB.setStatusTip(_translate("MainWindow", "external and internal patient page"))
        self.actionHelp_Center.setText(_translate("MainWindow", "Help Center"))
        self.actionHelp_Center.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionFAQ.setText(_translate("MainWindow", "FAQ"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us"))

import img

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Diagnosis()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


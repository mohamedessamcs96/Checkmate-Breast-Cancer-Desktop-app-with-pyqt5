# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mammography2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from sklearn.externals import joblib
import csv
from datetime import date
import time
from datetime import datetime
import datetime
#import pandas as pd
class Ui_MammoDetect(object):
    global PatientID,Mefalsepause,Breastquad,Falsedecaps,Irradiat,Degmalig,Tumorsize,Breast,Invnodes,connection,doctorname,time,date
    Mefalsepause=""
    Breastquad=""
    Falsedecaps=""
    Irradiat=""
    Degmalig=""
    Tumorsize=""
    Breast=""
    Invnodes=""
    PatientID=""
    doctorname=""
    
    connection=sqlite3.connect("sqlitedatabase5.db")    

    
    now = datetime.datetime.now()
    date=str(now.day)+'/'+str(now.month)+'/'+str(now.year)
    time=str(now.hour)+':'+str(now.minute)
    
    def ShowMessageBox(self,title,message):
        messagebox=QtWidgets.QMessageBox()
        messagebox.setIcon(QtWidgets.QMessageBox.Warning)
        messagebox.setWindowTitle(title)
        messagebox.setText(message)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messagebox.exec_()  
    
    def Machinelearning(self):
        print("Mamography Page,ML Function")
        print(type(PatientID))
        global MassShape,BIRADS,MassMargin,MassDensity,Age,Notes
        MassShape=int(self.comboBox_1.currentText())
        BIRADS=int(self.comboBox_6.currentText())
        MassMargin=int(self.comboBox_2.currentText())
        MassDensity=int(self.comboBox_7.currentText())
        Notes=self.plainTextEdit.toPlainText()
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
        
        clf=joblib.load('mmamographmodel')
        Blood_data=[[BIRADS,Age,MassShape,MassMargin,MassDensity]]
        prediction=clf.predict(Blood_data)
        
        for i in range(len(prediction)):
            if(prediction[i]==0):
                global Output
                print("The tumor is Begnin")
                Output="Begnin"
                self.ShowMessageBox('Diagnosis','The Diagnosis of this Analysis say that this person is:Begnin')

            elif(prediction[i]==1):
                print("The tumor is Malignant")
                Output="Malignant"        
                self.ShowMessageBox('Diagnosis','The Diagnosis of this Analysis say that this person is: Malignant')
        
        self.PrintReport()
        self.dataHistory()
        self.UpdatingDataset()
    def dataHistory(self):
        global MassShape,BIRADS,MassMargin,MassDensity,Age,Notes
        MassShape=int(self.comboBox_1.currentText())
        BIRADS=int(self.comboBox_6.currentText())
        MassMargin=int(self.comboBox_2.currentText())
        MassDensity=int(self.comboBox_7.currentText())        
        unix=time
        #currentdate=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))   
        #print(currentdate)
        connection.execute('INSERT INTO MOMGRAPH(DATE,MAMORESULT,BIRADS,MASSHAPE,MASSSMARGIN,MASSDENISITY,BREAST,BREASTSQUAD,TUMORSIZE,DEGMALIG,IRRADIAT,INVFALSEDES,PATIENTID)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) ',
                           (unix,Output,BIRADS,MassShape,MassMargin,MassDensity,Breast,Breastquad,Tumorsize,Degmalig,Invnodes,Irradiat,PatientID))
        connection.commit()
    
        
    def UpdatingDataset(self):
        
            '''Making a dataset from scractch '''
        
            with open('Mammo_Dataset.csv', mode='a',) as new_data:
                X = csv.writer(new_data, delimiter=',')
                X.writerow([BIRADS,Age,MassShape,MassMargin,MassDensity])
                new_data.close()
            
            import pandas as pd
            Mammo_Dataset=pd.read_csv('Mammo_Dataset.csv', delimiter=',')
            print(Mammo_Dataset.shape)
            Mammo_Dataset.drop_duplicates(subset=None,inplace=False)
            Mammo_Dataset.to_csv('Mammo_Dataset.csv', encoding='utf-8',sep=',',index=False)


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
        #pdf.ln(5)
    
      
        #Date
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(80, 'Date:')
        pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(80,time)
        #Time in
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(80, 'Time in:')
        pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(80, date)
            
        pdf.ln(5)
        #Location
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(90, 'Location:')
        pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(90, 'HTI Cancer Hospital')
        pdf.ln(5)
            
        #Patient details Title
        pdf.set_font('Arial', '', 15)
        pdf.cell(5)
        pdf.write(100, 'Patient details')
        pdf.ln(5)        
        pdf.set_font('Arial', '', 13)
        '''    ###############################################'''  
        #Their information
        #Date
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(115, 'Name:')
        
        pdf.set_font('Arial', '', 10)
        pdf.write(115, name)
        #Time in
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(105)
        pdf.write(140, 'Age:')
        pdf.set_font('Arial', '', 10)
        pdf.write(140,str(Age))
        
        pdf.ln(5)
        #Location
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(130, 'SSN:')
        pdf.set_font('Arial', '', 10)
        pdf.write(130,str(ssni))
        pdf.ln(5) 
        pdf.cell(5)
        #Location
        pdf.cell(130)
        pdf.set_font('Arial', 'B', 10)
        pdf.write(105, 'Gender:')
        pdf.set_font('Arial', '', 10)
        pdf.write(105,str(gender))
        pdf.ln(5)  
        '''    ###############################################'''  
        #Their information
        #Date
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(125, 'Mass Shape:')
        pdf.set_font('Arial', '', 10)
        pdf.write(125,str(MassShape))
        #Time in
        
        BIRADS,Age,MassShape,MassMargin,MassDensity,Breast,Breastquad,Tumorsize,Degmalig,Invnodes,Irradiat,
        
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(105)
        pdf.write(130, 'BI-RADS:')
        #pdf.cell(5)
        pdf.set_font('Arial', 'B', 10)
        pdf.write(130,str(BIRADS))
        
        pdf.ln(5)
        #Location
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(135, 'Mass Margin:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(135,str(MassMargin))
        pdf.ln(5)
            
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(130)
        pdf.write(127, 'Mass Density:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(127,str(MassDensity))
        pdf.ln(3)
            
        '''    ###############################################'''  
        #Their information
        #Date
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(128, 'Breast:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(128,str(Breast))
        #Time in
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(105)
        pdf.write(140, 'Breastquad:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(140,str(Breastquad))
        
        pdf.ln(5)
        #Location
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(134, 'Invnodes:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(134,str(Invnodes))
        pdf.ln(5)
        
        #Location
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(133, 'Degmalig:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(133,str(Degmalig))
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
        pdf.write(155, 'Notes:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 8)
        pdf.write(165,str(Notes))
        pdf.ln(1)            
        
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(125)
        pdf.write(175, 'Doctor:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(175,doctorname)
               
    
   
        pdf.output('PatientMammoGraphReport.pdf', 'F')
        import os 
        os.startfile("PatientMammoGraphReport.pdf")       
    
    
    def DAWarnning(self):
        self.ShowMessageBox('Warning',"This Page doesn't available for you ")
    
    
    def SSWarnning(self):
        self.ShowMessageBox('Warning',"Wrong Choice,Check if the patient is registerd or add new patient")
    
    
    def SPWarnning(self):
        self.ShowMessageBox('Warning',"You are in the same page")
    
    
    
    
    
    def setupUi(self, SampleDetect):
        SampleDetect.setObjectName("SampleDetect")
        SampleDetect.resize(1380, 730)
        SampleDetect.setStyleSheet("QPushButton {\n"
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
        self.centralwidget = QtWidgets.QWidget(SampleDetect)
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
        self.MammoT = QtWidgets.QLabel(self.frame)
        self.MammoT.setGeometry(QtCore.QRect(350, 160, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.MammoT.setFont(font)
        self.MammoT.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.MammoT.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.MammoT.setFrameShape(QtWidgets.QFrame.Box)
        self.MammoT.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.MammoT.setObjectName("MammoT")
        self.MammoF = QtWidgets.QFrame(self.frame)
        self.MammoF.setGeometry(QtCore.QRect(260, 180, 531, 381))
        self.MammoF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MammoF.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.MammoF.setObjectName("MammoF")
        self.NextB = QtWidgets.QPushButton(self.MammoF)
        self.NextB.setGeometry(QtCore.QRect(140, 270, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.NextB.setFont(font)
        self.NextB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.NextB.setObjectName("NextB")
        self.NextB.clicked.connect(self.Machinelearning)
        self.ResetB = QtWidgets.QPushButton(self.MammoF)
        self.ResetB.setGeometry(QtCore.QRect(310, 270, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ResetB.setFont(font)
        self.ResetB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResetB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.ResetB.setObjectName("ResetB")
        self.label_1 = QtWidgets.QLabel(self.MammoF)
        self.label_1.setGeometry(QtCore.QRect(39, 70, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.comboBox_7 = QtWidgets.QComboBox(self.MammoF)
        self.comboBox_7.setGeometry(QtCore.QRect(400, 120, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_7.setStyleSheet("")
        self.comboBox_7.setEditable(False)
        self.comboBox_7.setMaxVisibleItems(10)
        self.comboBox_7.setMaxCount(10)
        self.comboBox_7.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_7.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_7.setMinimumContentsLength(1)
        self.comboBox_7.setDuplicatesEnabled(False)
        self.comboBox_7.setModelColumn(0)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.MammoF)
        self.comboBox_6.setGeometry(QtCore.QRect(400, 70, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_6.setStyleSheet("")
        self.comboBox_6.setEditable(False)
        self.comboBox_6.setMaxVisibleItems(10)
        self.comboBox_6.setMaxCount(10)
        self.comboBox_6.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_6.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_6.setMinimumContentsLength(1)
        self.comboBox_6.setDuplicatesEnabled(False)
        self.comboBox_6.setModelColumn(0)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_29 = QtWidgets.QLabel(self.MammoF)
        self.label_29.setGeometry(QtCore.QRect(260, 120, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.comboBox_1 = QtWidgets.QComboBox(self.MammoF)
        self.comboBox_1.setGeometry(QtCore.QRect(190, 70, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_1.setStyleSheet("")
        self.comboBox_1.setEditable(False)
        self.comboBox_1.setMaxVisibleItems(10)
        self.comboBox_1.setMaxCount(10)
        self.comboBox_1.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_1.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_1.setMinimumContentsLength(1)
        self.comboBox_1.setIconSize(QtCore.QSize(3, 3))
        self.comboBox_1.setDuplicatesEnabled(False)
        self.comboBox_1.setModelColumn(0)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.label_23 = QtWidgets.QLabel(self.MammoF)
        self.label_23.setGeometry(QtCore.QRect(260, 70, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_23.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_25 = QtWidgets.QLabel(self.MammoF)
        self.label_25.setGeometry(QtCore.QRect(50, 120, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.comboBox_2 = QtWidgets.QComboBox(self.MammoF)
        self.comboBox_2.setGeometry(QtCore.QRect(190, 120, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_2.setStyleSheet("")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(10)
        self.comboBox_2.setMaxCount(10)
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_2.setMinimumContentsLength(1)
        self.comboBox_2.setDuplicatesEnabled(False)
        self.comboBox_2.setModelColumn(0)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.MammoF)
        self.frame_2.setGeometry(QtCore.QRect(10, 330, 221, 41))
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
        self.label_26 = QtWidgets.QLabel(self.MammoF)
        self.label_26.setGeometry(QtCore.QRect(20, 200, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.MammoF)
        self.plainTextEdit.setGeometry(QtCore.QRect(160, 180, 261, 71))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(30, 20, 161, 111))
        self.Logo.setStyleSheet("image: url(:/images/img/Logo.png);")
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 570, 281, 41))
        self.frame_4.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.Hint_3 = QtWidgets.QLabel(self.frame_4)
        self.Hint_3.setGeometry(QtCore.QRect(37, 11, 231, 20))
        self.Hint_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Hint_3.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.Hint_3.setObjectName("Hint_3")
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 21, 21))
        self.label_5.setStyleSheet("image: url(:/images/img/Hint.png);\n"
"background-color: rgb(242, 242, 242);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.Obacity.raise_()
        self.MammoF.raise_()
        self.MammoT.raise_()
        self.Logo.raise_()
        self.frame_4.raise_()
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
        
        '''
        Button ACtion 
        
        '''
        self.PatientInfoB.clicked.connect(self.DAWarnning)
        self.MammoB.clicked.connect(self.SPWarnning)
        self.DiagnosisB.clicked.connect(self.DAWarnning)
        self.FNAB.clicked.connect(self.DAWarnning)
        self.PrintB.clicked.connect(self.DAWarnning)
        #self.SampleB.clicked.connect(self.DAWarnning)
        '''
        Button ACtion 
        
        '''
        
        
        
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
        SampleDetect.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SampleDetect)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1380, 21))
        self.menubar.setObjectName("menubar")
        SampleDetect.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SampleDetect)
        self.statusbar.setObjectName("statusbar")
        SampleDetect.setStatusBar(self.statusbar)
        self.actionHelp_Center = QtWidgets.QAction(SampleDetect)
        self.actionHelp_Center.setObjectName("actionHelp_Center")
        self.actionFAQ = QtWidgets.QAction(SampleDetect)
        self.actionFAQ.setObjectName("actionFAQ")
        self.actionAbout_Us = QtWidgets.QAction(SampleDetect)
        self.actionAbout_Us.setObjectName("actionAbout_Us")

        self.retranslateUi(SampleDetect)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_1.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.ResetB.clicked.connect(self.comboBox_1.clear)
        self.ResetB.clicked.connect(self.comboBox_2.clear)
        self.ResetB.clicked.connect(self.comboBox_6.clear)
        self.ResetB.clicked.connect(self.comboBox_7.clear)
        QtCore.QMetaObject.connectSlotsByName(SampleDetect)
        SampleDetect.setTabOrder(self.PatientInfoB, self.DiagnosisB)
        SampleDetect.setTabOrder(self.DiagnosisB, self.SampleB)
        SampleDetect.setTabOrder(self.SampleB, self.MammoB)
        SampleDetect.setTabOrder(self.MammoB, self.FNAB)
        SampleDetect.setTabOrder(self.FNAB, self.PrintB)
        SampleDetect.setTabOrder(self.PrintB, self.comboBox_1)
        SampleDetect.setTabOrder(self.comboBox_1, self.comboBox_2)
        SampleDetect.setTabOrder(self.comboBox_2, self.comboBox_6)
        SampleDetect.setTabOrder(self.comboBox_6, self.comboBox_7)
        SampleDetect.setTabOrder(self.comboBox_7, self.NextB)
        SampleDetect.setTabOrder(self.NextB, self.ResetB)
        SampleDetect.setTabOrder(self.ResetB, self.Help)

    def retranslateUi(self, SampleDetect):
        _translate = QtCore.QCoreApplication.translate
        SampleDetect.setWindowTitle(_translate("SampleDetect", "MainWindow"))
        self.MammoT.setText(_translate("SampleDetect", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#4d4d4d;\">Mammography Mass</span></p></body></html>"))
        self.NextB.setToolTip(_translate("SampleDetect", "Next to Tumor Recerrence"))
        self.NextB.setText(_translate("SampleDetect", "Detect"))
        self.NextB.setShortcut(_translate("SampleDetect", "Enter"))
        self.ResetB.setToolTip(_translate("SampleDetect", "Reset"))
        self.ResetB.setStatusTip(_translate("SampleDetect", "Reset all fields"))
        self.ResetB.setText(_translate("SampleDetect", "Reset"))
        self.ResetB.setShortcut(_translate("SampleDetect", "Ctrl+R"))
        self.label_1.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Mass Shape :</span></p></body></html>"))
        self.comboBox_7.setStatusTip(_translate("SampleDetect", "1=high  2=iso  3=low  4=fat-containing"))
        self.comboBox_7.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_7.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_7.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_7.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_6.setStatusTip(_translate("SampleDetect", "1 to 5 (ordinal, non-predictive)"))
        self.comboBox_6.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_6.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_6.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_6.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_6.setItemText(4, _translate("SampleDetect", "5"))
        self.label_29.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Mass Density  :</span></p></body></html>"))
        self.comboBox_1.setStatusTip(_translate("SampleDetect", "1=round  2=oval  3=lobular  4=irregular"))
        self.comboBox_1.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_1.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_1.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_1.setItemText(3, _translate("SampleDetect", "4"))
        self.label_23.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">BI-RADS Assessment :</span></p></body></html>"))
        self.label_25.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Mass Margin :</span></p></body></html>"))
        self.comboBox_2.setStatusTip(_translate("SampleDetect", "1=circumscribed  2=microlobulated  3=obscured  4=ill-defined  5=spiculated"))
        self.comboBox_2.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_2.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_2.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_2.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_2.setItemText(4, _translate("SampleDetect", "5"))
        self.Hint.setText(_translate("SampleDetect", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">you must enter all fields.</span></p></body></html>"))
        self.label_26.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" font-size:14pt; color:#232323;\">Notes :</span></p></body></html>"))
        self.Hint_3.setText(_translate("SampleDetect", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">These features are include patient age</span></p></body></html>"))
        self.Help.setToolTip(_translate("SampleDetect", "Help"))
        self.Help.setStatusTip(_translate("SampleDetect", "Need a help ? go to help center."))
        self.Help.setShortcut(_translate("SampleDetect", "Ctrl+H"))
        self.SampleB.setToolTip(_translate("SampleDetect", "Sample detect"))
        self.SampleB.setStatusTip(_translate("SampleDetect", "detect tumor by sample "))
        self.MammoB.setToolTip(_translate("SampleDetect", "Mammography Mass"))
        self.MammoB.setStatusTip(_translate("SampleDetect", "Detect tumor by Mammography"))
        self.FNAB.setToolTip(_translate("SampleDetect", "Fine Needle Aspirate"))
        self.FNAB.setStatusTip(_translate("SampleDetect", "Detect Tumor by Fine Needle Aspirate (FNA)"))
        self.PrintB.setToolTip(_translate("SampleDetect", "Print"))
        self.PrintB.setStatusTip(_translate("SampleDetect", "Print patient report"))
        self.DiagnosisB.setToolTip(_translate("SampleDetect", "Diagnosis"))
        self.DiagnosisB.setStatusTip(_translate("SampleDetect", "show if patient have tumor or not "))
        self.PatientInfoB.setToolTip(_translate("SampleDetect", "Patient Information"))
        self.PatientInfoB.setStatusTip(_translate("SampleDetect", "external and internal patient page"))
        self.actionHelp_Center.setText(_translate("SampleDetect", "Help Center"))
        self.actionHelp_Center.setShortcut(_translate("SampleDetect", "Ctrl+H"))
        self.actionFAQ.setText(_translate("SampleDetect", "FAQ"))
        self.actionAbout_Us.setText(_translate("SampleDetect", "About Us"))

import img
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SampleDetect = QtWidgets.QMainWindow()
    ui = Ui_SampleDetect()
    ui.setupUi(SampleDetect)
    SampleDetect.show()
    sys.exit(app.exec_())


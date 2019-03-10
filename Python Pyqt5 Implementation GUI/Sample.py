# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sample.ui'
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
#from requests.exceptions import Exception


class Ui_SampleDetect(object):
    global PatientID ,connection,doctorname,sampleResult,Output,BinaryOutput,Samplemodel,Mefalsepause,Breastquad ,Irradiat,Falsedecaps,Degmalig,Tumorsize,Breast,Invnodes,now,time,date,unix
    global Mefalsepause_I,Breastquad_I ,Irradiat_I,Falsedecaps_I,Degmalig_I,Tumorsize_I ,Breast_I,Invnodes_I
    connection=sqlite3.connect("sqlitedatabase5.db")    
    now = datetime.datetime.now()
    date=str(now.day)+'/'+str(now.month)+'/'+str(now.year)
    time=str(now.hour)+':'+str(now.minute)
    print(time)
        
    PatientID=""
    doctorname=""        
    Mefalsepause =""
    Breastquad=""
    Falsedecaps=""
    Irradiat =""
    Degmalig =""
    Tumorsize =""
    Breast=""
    Invnodes=""
    print(Mefalsepause,Breastquad ,Irradiat,Falsedecaps,Degmalig,Tumorsize ,Breast,Invnodes)
    
    print(doctorname)
                
    def FirstScore():
        return 0.959
    
    
    def dataHistory(self):
        unix=time
        #currentdate=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))   
        #print(currentdate)
        connection.execute('INSERT INTO SAMPLE(DATE,SAMPLRESULT,TUMORRECURRENCE,BREAST,BREASTSQUAD,TUMORSIZE,DEGMALIG,IRRADIAT,INVFALSEDES,PATIENTID) VALUES(?,?,?,?,?,?,?,?,?,?)',
                           (unix,SampleOutput,sampleRecurrence,Breast,Breastquad,Tumorsize,Degmalig,Irradiat,Invnodes,PatientID,))
        #print(unix,SampleOutput,sampleRecurrence,Breast,Breastquad,Tumorsize,Degmalig,Irradiat,Invnodes,PatientID)
        #print(type(unix),type(SampleOutput),type(sampleRecurrence),type(Breast),type(Breastquad),type(Tumorsize),type(Degmalig),type(Irradiat),type(Invnodes),type(PatientID))
        connection.commit()
    def Machinelearning(self):
        
        global MarginalAdhesion,ShapeUniformity,ClumbThickness,SizeUniformity,EpithelialSize,BlandChromatin,NormalNucleoli,BareNuclue,Mitoses,result,count,Age,Samplemodel
        MarginalAdhesion=int(self.comboBox_1.currentText())
        ShapeUniformity=int(self.comboBox_2.currentText())
        ClumbThickness=int(self.comboBox_3.currentText())
        SizeUniformity=int(self.comboBox_4.currentText())
        EpithelialSize=int(seldataHistoryf.comboBox_5.currentText())
        BlandChromatin =int(self.comboBox_6.currentText())
        NormalNucleoli =int(self.comboBox_7.currentText())
        BareNuclue =int(self.comboBox_8.currentText())
        Mitoses =int(self.comboBox_9.currentText())
        #import the model
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
        
        
        
        print('beforemodel')
        Samplemodel=joblib.load('samplemodel')
        print('aftermodel')
        Sampleresult=Samplemodel.predict([[MarginalAdhesion,ShapeUniformity,ClumbThickness,SizeUniformity,EpithelialSize,BlandChromatin,NormalNucleoli,BareNuclue,Mitoses]])
        print(Sampleresult)
        #i will use variable out put to store as a string in the db
        #and i will use BinaryOutput to added to the old data as a binary
        global SampleBinaryOutput,SampleOutput,RecurrenceBinaryOutput,Recurrenceresult,sampleRecurrence
        
        for i in range(len(Sampleresult)):
            if(Sampleresult[i]==2):
                SampleOutput="Begnin"
                SampleBinaryOutput=Sampleresult[i]
                print(SampleBinaryOutput)
                self.ShowMessageBox('Diagnosis',SampleOutput)

            elif(Sampleresult[i]==4):
                SampleOutput="Malignant"
                SampleBinaryOutput=Sampleresult[i]
                print(SampleBinaryOutput)
                self.ShowMessageBox('Diagnosis',SampleOutput)
        """
        The Recurrence Statement
        """
        global Mefalsepause_I,Breastquad_I ,Irradiat_I,Falsedecaps_I,Degmalig_I,Tumorsize_I ,Breast_I,Invnodes_I
    
        
        if(Mefalsepause=='Premefalse'):
            Mefalsepause_I=1
        elif(Mefalsepause=='ge40'):
            Mefalsepause_I=2
        elif(Mefalsepause=='lt40'):
            Mefalsepause_I=3
        
    
        if(Breastquad=='Left up'):
            Breastquad_I=7
        elif(Breastquad=='Left low'):
            Breastquad_I=1
        elif(Breastquad=='Right up'):
            Breastquad_I=9
        elif(Breastquad=='Right low'):
            Breastquad_I=3
        elif(Breastquad=='Central'):
            Breastquad_I=5
    
        if(Irradiat=='True'):
            Irradiat_I=2
        elif(Irradiat=='False'):
            Irradiat_I=3
    
        if(Falsedecaps=='True'):
            Falsedecaps_I=2
        elif(Falsedecaps=='False'):
            Falsedecaps_I=3
        
        if(Breast=='Right'):
            Breast_I=4
        elif(Breast=='Left'):
            Breast_I=6
            
            

        Degmalig_I=int(Degmalig)
        Tumorsize_I=int(Tumorsize)
        Invnodes_I=int(Invnodes)
        print("The Mapping Results")
        print(Mefalsepause_I,Breastquad_I ,Irradiat_I,Falsedecaps_I,Degmalig_I,Tumorsize_I ,Breast_I,Invnodes_I)
        #import the model
        print('beforemodel')
        model=joblib.load('recurrencemodel')
        print('aftermodel')
        Recurrenceresult=model.predict([[Mefalsepause_I,Breastquad_I,Falsedecaps_I,Irradiat_I,Degmalig_I,Tumorsize_I,Breast_I,Invnodes_I]])
        print(Recurrenceresult)
        #i will use variable out put to store as a string in the db
        #and i will use BinaryOutput to added to the old data as a binary
        for i in range(len(Recurrenceresult)):
            if(Recurrenceresult[i]==4):
                sampleRecurrence="non recurrence"
                RecurrenceBinaryOutput=Recurrenceresult[i]
                print(RecurrenceBinaryOutput)
                self.ShowMessageBox('Diagnosis',sampleRecurrence)

            elif(Recurrenceresult[i]==6):
                sampleRecurrence="recurrence"
                RecurrenceBinaryOutput=Recurrenceresult[i]
                print(RecurrenceBinaryOutput)
                self.ShowMessageBox('Diagnosis',sampleRecurrence)
        
        self.PrintReport()
        self.UpdatingDataset()
        self.dataHistory()
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
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(80,date)
        #Time in
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(80, 'Time in:')
        pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(80, time)
            
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
        pdf.cell(90)
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
        pdf.cell(120)
        pdf.set_font('Arial', 'B', 10)
        pdf.write(90, 'Gender:')
        pdf.set_font('Arial', '', 10)
        pdf.write(90,str(gender))
        pdf.ln(5)  
        '''    ###############################################'''  
        #Their information
        #Date
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(125, 'Clumb Thickness:')
        pdf.set_font('Arial', '', 10)
        pdf.write(125,str(ClumbThickness))
        #Time in
        
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(90)
        pdf.write(130, 'Shape Uniformity:')
        #pdf.cell(5)
        pdf.set_font('Arial', 'B', 10)
        pdf.write(130,str(ShapeUniformity))
        
        pdf.ln(5)
        #Location
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(5)
        pdf.write(135, 'Size Uniformity:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(135,str(SizeUniformity))
        pdf.ln(5)
            
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(130)
        pdf.write(127, 'Epithelial Size:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(127,str(EpithelialSize))
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
        pdf.write(140,SampleOutput)
        #Time in
        pdf.set_font('Arial', 'B', 10)
        pdf.ln(5)
        pdf.cell(120)
        pdf.write(140,'Recurrence:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(140,sampleRecurrence)                  
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(125)
        pdf.write(160, 'Doctor:')
        #pdf.cell(5)
        pdf.set_font('Arial', '', 10)
        pdf.write(160,doctorname)        
    
        pdf.output('PatientSampleReport.pdf', 'F')
        import os 
        os.startfile("PatientSampleReport.pdf")        
        
    def ShowMessageBox(self,title,message):
        messagebox=QtWidgets.QMessageBox()
        messagebox.setIcon(QtWidgets.QMessageBox.Warning)
        messagebox.setWindowTitle(title)
        messagebox.setText(message)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messagebox.exec_()   
          
    def DAWarnning(self):
        self.ShowMessageBox('Warning',"This Page doesn't available for you ")
    
    
    def SSWarnning(self):
        self.ShowMessageBox('Warning',"Wrong Choice,Check if the patient is registerd or add new patient")
    
    
    def SPWarnning(self):
        self.ShowMessageBox('Warning',"You are in the same page")
    
    
    def UpdatingDataset(self):
        
            '''Making a dataset from scractch '''
        
            with open('Sample_Dataset.csv', mode='a',) as new_data:
                X = csv.writer(new_data, delimiter=',')
                X.writerow([ClumbThickness,SizeUniformity,ShapeUniformity,MarginalAdhesion,EpithelialSize,BareNuclue,BlandChromatin,NormalNucleoli,Mitoses,SampleBinaryOutput])
                new_data.close()
                
            '''adding the features to the newest dataset '''
            with open('updated_prepared_sample_dataest.csv', mode='a',) as new_data:
                X = csv.writer(new_data, delimiter=',')
                X.writerow([ClumbThickness,SizeUniformity,ShapeUniformity,MarginalAdhesion,EpithelialSize,BareNuclue,BlandChromatin,NormalNucleoli,Mitoses,SampleBinaryOutput])
                new_data.close()
            
            #####
            import pandas as pd
            raw_data=pd.read_csv('Sample_Dataset.csv', delimiter=',')
            print(raw_data.shape)
            ####       
            #####
            import pandas as pd
            updated_data=pd.read_csv('updated_prepared_sample_dataest.csv', delimiter=',')
            print(updated_data.shape)
            updated_data.drop_duplicates(subset=None,inplace=False)
            count=len(updated_data)
            if(count%1000==0):
                self.UpdatingModel()
                
          
    
    def UpdatingModel(self):
        from sklearn.svm import SVC
        from sklearn import tree
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.model_selection import train_test_split
        import pandas as pd
        global SvmTestPrediction,KnnTestPrediction,TreeTestPrediction ,algorithmname,accuracy
        global Samplemodel
        def check_svm(self):
            '''SVM'''
            sample_svm=pd.read_csv('prepared_sample_dataest.csv', delimiter=',')
            X=sample_svm[['clump_thickness','size_uniformity','shape_uniformity','marginal_adhesion','epithelial_size','bare_nucleoli','bland_chromatin','normal_nucleoli','mitoses']]
            y=sample_svm['class']
            X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0)               
            min_train = X_train.min(axis=0)
            range_train = (X_train - min_train).max(axis=0)
            X_train_scaled = (X_train - min_train)/range_train
            X_test_scaled = (X_test - min_train)/range_train
            svm = SVC(100)
            svm=svm.fit(X_train_scaled, y_train)
            SvmTrainPrediction=svm.score(X_train,y_train)
            SvmTestPrediction=svm.score(X_test_scaled,y_test)
            print('Accuracy on the training subset: {:.3f}'.format(SvmTrainPrediction))
            print('Accuracy on the test subset: {:.3f}'.format(SvmTestPrediction))            
            '''SVM'''
        
        def check_KNN(self):
            '''KNN'''
            knn = KNeighborsClassifier()
            sample_knn=pd.read_csv('prepared_sample_dataest.csv', delimiter=',')
            X=sample_knn[['clump_thickness','size_uniformity','shape_uniformity','marginal_adhesion','epithelial_size','bare_nucleoli','bland_chromatin','normal_nucleoli','mitoses']]
            y=sample_knn['class']
            X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0) 
            knn=knn.fit(X_train,y_train)
            KnnTrainPrediction=knn.score(X_train,y_train)
            KnnTestPrediction=knn.score(X_test,y_test)
            print('Accuracy on the training subset: {:.3f}'.format(KnnTrainPrediction))
            print('Accuracy on the test subset: {:.3f}'.format(KnnTestPrediction))
            
            '''KNN'''
        def check_tree(self):
            '''TREE'''
            sample_tree=pd.read_csv('prepared_sample_dataest.csv', delimiter=',')
            X=sample_tree[['clump_thickness','size_uniformity','shape_uniformity','marginal_adhesion','epithelial_size','bare_nucleoli','bland_chromatin','normal_nucleoli','mitoses']]
            y=sample_tree['class']
            X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=0) 
            clf = tree.DecisionTreeClassifier()
            clf=clf.fit(X_train,y_train)
            TreeTrainPrediction=clf.score(X_train,y_train)
            TreeTestPrediction=clf.score(X_test,y_test)
            print('Accuracy on the training subset: {:.3f}'.format(TreeTrainPrediction))
            print('Accuracy on the test subset: {:.3f}'.format(TreeTestPrediction))
            
            '''TREE'''
            ''' 
            Now we check what is the Algorithm is better.
            '''
        if(SvmTestPrediction > TreeTestPrediction and SvmTestPrediction > KnnTestPrediction):
            if(SvmTestPrediction > self.FirstScore()):
                print(self.FirstScore())
                sample_svm=pd.read_csv('updated_prepared_sample_dataest.csv', delimiter=',')
                X=sample_svm[['clump_thickness','size_uniformity','shape_uniformity','marginal_adhesion','epithelial_size','bare_nucleoli','bland_chromatin','normal_nucleoli','mitoses']]
                y=sample_svm['class']                
                min_X = X.min(axis=0)
                X_range = (X - min_X).max(axis=0)
                X = (X - min_X)/X_range
                svm = SVC(C=100)
                clf=svm.fit(X,y)
                Samplemodel=joblib.dump(clf,'samplemodel')
                algorithmname="SVM"
                accuracy=SvmTestPrediction
                self.sendinfomail()
        elif(TreeTestPrediction>SvmTestPrediction and TreeTestPrediction > KnnTestPrediction):
            if(TreeTestPrediction > self.FirstScore()):
                print(self.FirstScore())
                sample_svm=pd.read_csv('updated_prepared_sample_dataest.csv', delimiter=',')
                X=sample_svm[['clump_thickness','size_uniformity','shape_uniformity','marginal_adhesion','epithelial_size','bare_nucleoli','bland_chromatin','normal_nucleoli','mitoses']]
                y=sample_svm['class']                
                knn = KNeighborsClassifier()
                knn=knn.fit(X,y)
                Samplemodel=joblib.dump(knn,'samplemodel')
                algorithmname="Tree"
                accuracy=TreeTestPrediction
                self.sendinfomail()
        elif(KnnTestPrediction>SvmTestPrediction and KnnTestPrediction > SvmTestPrediction):
            if(TreeTestPrediction > self.FirstScore()):
                print(self.FirstScore())
                sample_svm=pd.read_csv('updated_prepared_sample_dataest.csv', delimiter=',')
                X=sample_svm[['clump_thickness','size_uniformity','shape_uniformity','marginal_adhesion','epithelial_size','bare_nucleoli','bland_chromatin','normal_nucleoli','mitoses']]
                y=sample_svm['class']                
                clf = tree.DecisionTreeClassifier()
                clf=clf.fit(X,y)
                Samplemodel=joblib.dump(clf,'samplemodel')
                algorithmname="KNN"
                accuracy=KnnTestPrediction                  
                self.sendinfomail()

                
                
                
    def sendinfomail(self,algorithmname):
       import smtplib
       from email.mime.text import MIMEText
       from email.mime.multipart import MIMEMultipart
       send_to_email='mohammedessamomar@gmail.com'
       appemail='htibreastcancerapp.finalproject@gmail.com'
       apppassword='htibreastcancerapp.finalproject2019'
       subject='Breast Cancer CheckMate app Update'
       intro='Hello Guys greetings,\n there some updates now happend in the app'
       topic='the number of sample became a '+count+'sammples'
       end= 'and now we use Algorithm'+algorithmname+'with accuracy'+accuracy
       message=intro+topic+end
       print(message)
       
       try:
           msg=MIMEMultipart()
           msg["From"]=appemail
           msg["To"]='mohammedessamomar@gmail.com'
           msg["Subject"]=subject
           msg.attach(MIMEText(message,'plain'))
           server=smtplib.SMTP('smtp.gmail.com',587)
           server.starttls()
           server.login(appemail,apppassword)
           text=msg.as_string()
           server.sendmail(appemail,send_to_email,text)
           server.quit()                
       except Exception as e:
           print('no connection'+e)
           
    def setupUi(self, SampleDetect):
        SampleDetect.setObjectName("SampleDetect")
        SampleDetect.resize(1380, 730)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/img/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SampleDetect.setWindowIcon(icon)
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
        self.frame.setGeometry(QtCore.QRect(265, 50, 1041, 621))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Obacity = QtWidgets.QLabel(self.frame)
        self.Obacity.setGeometry(QtCore.QRect(690, 70, 641, 591))
        self.Obacity.setStyleSheet("image: url(:/images/img/Obacity.png);")
        self.Obacity.setText("")
        self.Obacity.setObjectName("Obacity")
        self.SampleDetectT = QtWidgets.QLabel(self.frame)
        self.SampleDetectT.setGeometry(QtCore.QRect(340, 90, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.SampleDetectT.setFont(font)
        self.SampleDetectT.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.SampleDetectT.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.SampleDetectT.setFrameShape(QtWidgets.QFrame.Box)
        self.SampleDetectT.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SampleDetectT.setObjectName("SampleDetectT")
        self.SampleF = QtWidgets.QFrame(self.frame)
        self.SampleF.setGeometry(QtCore.QRect(250, 110, 531, 421))
        self.SampleF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SampleF.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SampleF.setObjectName("SampleF")
        self.NextB = QtWidgets.QPushButton(self.SampleF)
        self.NextB.setGeometry(QtCore.QRect(126, 320, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.NextB.setFont(font)
        self.NextB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.NextB.setObjectName("NextB")
        self.ResetB = QtWidgets.QPushButton(self.SampleF)
        self.NextB.clicked.connect(self.Machinelearning)
        #self.NextB.clicked.connect(self.openSampleRecurrenceWindowPage)
        self.ResetB.setGeometry(QtCore.QRect(306, 320, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ResetB.setFont(font)
        self.ResetB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResetB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.ResetB.setObjectName("ResetB")
        self.comboBox_4 = QtWidgets.QComboBox(self.SampleF)
        self.comboBox_4.setGeometry(QtCore.QRect(190, 220, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_4.setStyleSheet("")
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setMaxVisibleItems(10)
        self.comboBox_4.setMaxCount(10)
        self.comboBox_4.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_4.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_4.setMinimumContentsLength(1)
        self.comboBox_4.setDuplicatesEnabled(False)
        self.comboBox_4.setModelColumn(0)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_1 = QtWidgets.QLabel(self.SampleF)
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
        self.comboBox_7 = QtWidgets.QComboBox(self.SampleF)
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
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.SampleF)
        self.comboBox_3.setGeometry(QtCore.QRect(190, 170, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_3.setStyleSheet("")
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setMaxVisibleItems(10)
        self.comboBox_3.setMaxCount(10)
        self.comboBox_3.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_3.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_3.setMinimumContentsLength(1)
        self.comboBox_3.setDuplicatesEnabled(False)
        self.comboBox_3.setModelColumn(0)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_27 = QtWidgets.QLabel(self.SampleF)
        self.label_27.setGeometry(QtCore.QRect(260, 170, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_27.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.comboBox_6 = QtWidgets.QComboBox(self.SampleF)
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
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_28 = QtWidgets.QLabel(self.SampleF)
        self.label_28.setGeometry(QtCore.QRect(50, 220, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_28.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.SampleF)
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
        self.label_24 = QtWidgets.QLabel(self.SampleF)
        self.label_24.setGeometry(QtCore.QRect(50, 170, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_24.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.comboBox_1 = QtWidgets.QComboBox(self.SampleF)
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
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_5 = QtWidgets.QComboBox(self.SampleF)
        self.comboBox_5.setGeometry(QtCore.QRect(190, 270, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_5.setStyleSheet("")
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setMaxVisibleItems(10)
        self.comboBox_5.setMaxCount(10)
        self.comboBox_5.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_5.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_5.setMinimumContentsLength(1)
        self.comboBox_5.setDuplicatesEnabled(False)
        self.comboBox_5.setModelColumn(0)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_26 = QtWidgets.QLabel(self.SampleF)
        self.label_26.setGeometry(QtCore.QRect(50, 270, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.comboBox_9 = QtWidgets.QComboBox(self.SampleF)
        self.comboBox_9.setGeometry(QtCore.QRect(400, 220, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_9.setFont(font)
        self.comboBox_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_9.setStyleSheet("")
        self.comboBox_9.setEditable(False)
        self.comboBox_9.setMaxVisibleItems(10)
        self.comboBox_9.setMaxCount(10)
        self.comboBox_9.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_9.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_9.setMinimumContentsLength(1)
        self.comboBox_9.setDuplicatesEnabled(False)
        self.comboBox_9.setModelColumn(0)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.label_23 = QtWidgets.QLabel(self.SampleF)
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
        self.comboBox_8 = QtWidgets.QComboBox(self.SampleF)
        self.comboBox_8.setGeometry(QtCore.QRect(400, 170, 41, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_8.setFont(font)
        self.comboBox_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_8.setStyleSheet("")
        self.comboBox_8.setEditable(False)
        self.comboBox_8.setMaxVisibleItems(10)
        self.comboBox_8.setMaxCount(10)
        self.comboBox_8.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_8.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_8.setMinimumContentsLength(1)
        self.comboBox_8.setDuplicatesEnabled(False)
        self.comboBox_8.setModelColumn(0)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.label_30 = QtWidgets.QLabel(self.SampleF)
        self.label_30.setGeometry(QtCore.QRect(260, 220, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_25 = QtWidgets.QLabel(self.SampleF)
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
        self.comboBox_2 = QtWidgets.QComboBox(self.SampleF)
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
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.SampleF)
        self.frame_2.setGeometry(QtCore.QRect(10, 370, 221, 41))
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
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(30, 20, 161, 111))
        self.Logo.setStyleSheet("image: url(:/images/img/Logo.png);")
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
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
        self.SampleF.raise_()
        self.SampleDetectT.raise_()
        self.Logo.raise_()
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
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_1.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_9.setCurrentIndex(0)
        self.comboBox_8.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.ResetB.clicked.connect(self.comboBox_1.clear)
        self.ResetB.clicked.connect(self.comboBox_2.clear)
        self.ResetB.clicked.connect(self.comboBox_3.clear)
        self.ResetB.clicked.connect(self.comboBox_4.clear)
        self.ResetB.clicked.connect(self.comboBox_5.clear)
        self.ResetB.clicked.connect(self.comboBox_6.clear)
        self.ResetB.clicked.connect(self.comboBox_7.clear)
        self.ResetB.clicked.connect(self.comboBox_8.clear)
        self.ResetB.clicked.connect(self.comboBox_9.clear)
        QtCore.QMetaObject.connectSlotsByName(SampleDetect)
        SampleDetect.setTabOrder(self.PatientInfoB, self.DiagnosisB)
        SampleDetect.setTabOrder(self.DiagnosisB, self.SampleB)
        SampleDetect.setTabOrder(self.SampleB, self.MammoB)
        SampleDetect.setTabOrder(self.MammoB, self.FNAB)
        SampleDetect.setTabOrder(self.FNAB, self.PrintB)
        SampleDetect.setTabOrder(self.PrintB, self.comboBox_1)
        SampleDetect.setTabOrder(self.comboBox_1, self.comboBox_2)
        SampleDetect.setTabOrder(self.comboBox_2, self.comboBox_3)
        SampleDetect.setTabOrder(self.comboBox_3, self.comboBox_4)
        SampleDetect.setTabOrder(self.comboBox_4, self.comboBox_5)
        SampleDetect.setTabOrder(self.comboBox_5, self.comboBox_6)
        SampleDetect.setTabOrder(self.comboBox_6, self.comboBox_7)
        SampleDetect.setTabOrder(self.comboBox_7, self.comboBox_8)
        SampleDetect.setTabOrder(self.comboBox_8, self.comboBox_9)
        SampleDetect.setTabOrder(self.comboBox_9, self.NextB)
        SampleDetect.setTabOrder(self.NextB, self.ResetB)
        SampleDetect.setTabOrder(self.ResetB, self.Help)

        '''
        Button ACtion 
        
        '''
        self.PatientInfoB.clicked.connect(self.DAWarnning)
        self.MammoB.clicked.connect(self.DAWarnning)
        self.DiagnosisB.clicked.connect(self.DAWarnning)
        self.FNAB.clicked.connect(self.DAWarnning)
        self.SampleB.clicked.connect(self.SPWarnning)
        self.PrintB.clicked.connect(self.DAWarnning)
        #self.SampleB.clicked.connect(self.DAWarnning)
        '''
        Button ACtion 
        
        '''

    def retranslateUi(self, SampleDetect):
        _translate = QtCore.QCoreApplication.translate
        SampleDetect.setWindowTitle(_translate("SampleDetect", "Sample Detect"))
        self.SampleDetectT.setText(_translate("SampleDetect", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#4d4d4d;\">Sample Detect</span></p></body></html>"))
        self.NextB.setToolTip(_translate("SampleDetect", "Next to Tumor Recerrence"))
        self.NextB.setText(_translate("SampleDetect", "Next"))
        self.NextB.setShortcut(_translate("SampleDetect", "Enter"))
        self.ResetB.setToolTip(_translate("SampleDetect", "Reset"))
        self.ResetB.setStatusTip(_translate("SampleDetect", "Reset all fields"))
        self.ResetB.setText(_translate("SampleDetect", "Reset"))
        self.ResetB.setShortcut(_translate("SampleDetect", "Ctrl+R"))
        self.comboBox_4.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_4.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_4.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_4.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_4.setItemText(4, _translate("SampleDetect", "5"))
        self.comboBox_4.setItemText(5, _translate("SampleDetect", "6"))
        self.comboBox_4.setItemText(6, _translate("SampleDetect", "7"))
        self.comboBox_4.setItemText(7, _translate("SampleDetect", "8"))
        self.comboBox_4.setItemText(8, _translate("SampleDetect", "9"))
        self.comboBox_4.setItemText(9, _translate("SampleDetect", "10"))
        self.label_1.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Marginal Adhesion :</span></p></body></html>"))
        self.comboBox_7.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_7.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_7.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_7.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_7.setItemText(4, _translate("SampleDetect", "5"))
        self.comboBox_7.setItemText(5, _translate("SampleDetect", "6"))
        self.comboBox_7.setItemText(6, _translate("SampleDetect", "7"))
        self.comboBox_7.setItemText(7, _translate("SampleDetect", "8"))
        self.comboBox_7.setItemText(8, _translate("SampleDetect", "9"))
        self.comboBox_7.setItemText(9, _translate("SampleDetect", "10"))
        self.comboBox_3.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_3.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_3.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_3.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_3.setItemText(4, _translate("SampleDetect", "5"))
        self.comboBox_3.setItemText(5, _translate("SampleDetect", "6"))
        self.comboBox_3.setItemText(6, _translate("SampleDetect", "7"))
        self.comboBox_3.setItemText(7, _translate("SampleDetect", "8"))
        self.comboBox_3.setItemText(8, _translate("SampleDetect", "9"))
        self.comboBox_3.setItemText(9, _translate("SampleDetect", "10"))
        self.label_27.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Bare Nuclue :</span></p></body></html>"))
        self.comboBox_6.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_6.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_6.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_6.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_6.setItemText(4, _translate("SampleDetect", "5"))
        self.comboBox_6.setItemText(5, _translate("SampleDetect", "6"))
        self.comboBox_6.setItemText(6, _translate("SampleDetect", "7"))
        self.comboBox_6.setItemText(7, _translate("SampleDetect", "8"))
        self.comboBox_6.setItemText(8, _translate("SampleDetect", "9"))
        self.comboBox_6.setItemText(9, _translate("SampleDetect", "10"))
        self.label_28.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Size Uniformity :</span></p></body></html>"))
        self.label_29.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Normal Nucleoli :</span></p></body></html>"))
        self.label_24.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Clumb Thickness :</span></p></body></html>"))
        self.comboBox_1.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_1.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_1.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_1.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_1.setItemText(4, _translate("SampleDetect", "5"))
        self.comboBox_1.setItemText(5, _translate("SampleDetect", "6"))
        self.comboBox_1.setItemText(6, _translate("SampleDetect", "7"))
        self.comboBox_1.setItemText(7, _translate("SampleDetect", "8"))
        self.comboBox_1.setItemText(8, _translate("SampleDetect", "9"))
        self.comboBox_1.setItemText(9, _translate("SampleDetect", "10"))
        self.comboBox_5.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_5.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_5.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_5.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_5.setItemText(4, _translate("SampleDetect", "5"))
        self.comboBox_5.setItemText(5, _translate("SampleDetect", "6"))
        self.comboBox_5.setItemText(6, _translate("SampleDetect", "7"))
        self.comboBox_5.setItemText(7, _translate("SampleDetect", "8"))
        self.comboBox_5.setItemText(8, _translate("SampleDetect", "9"))
        self.comboBox_5.setItemText(9, _translate("SampleDetect", "10"))
        self.label_26.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Epithelial Size  :</span></p></body></html>"))
        self.comboBox_9.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_9.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_9.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_9.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_9.setItemText(4, _translate("SampleDetect", "5"))
        self.comboBox_9.setItemText(5, _translate("SampleDetect", "6"))
        self.comboBox_9.setItemText(6, _translate("SampleDetect", "7"))
        self.comboBox_9.setItemText(7, _translate("SampleDetect", "8"))
        self.comboBox_9.setItemText(8, _translate("SampleDetect", "9"))
        self.comboBox_9.setItemText(9, _translate("SampleDetect", "10"))
        self.label_23.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Bland Chromatin :</span></p></body></html>"))
        self.comboBox_8.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_8.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_8.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_8.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_8.setItemText(4, _translate("SampleDetect", "5"))
        self.comboBox_8.setItemText(5, _translate("SampleDetect", "6"))
        self.comboBox_8.setItemText(6, _translate("SampleDetect", "7"))
        self.comboBox_8.setItemText(7, _translate("SampleDetect", "8"))
        self.comboBox_8.setItemText(8, _translate("SampleDetect", "9"))
        self.comboBox_8.setItemText(9, _translate("SampleDetect", "10"))
        self.label_30.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Mitoses :</span></p></body></html>"))
        self.label_25.setText(_translate("SampleDetect", "<html><head/><body><p><span style=\" color:#232323;\">Shape Uniformity :</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("SampleDetect", "1"))
        self.comboBox_2.setItemText(1, _translate("SampleDetect", "2"))
        self.comboBox_2.setItemText(2, _translate("SampleDetect", "3"))
        self.comboBox_2.setItemText(3, _translate("SampleDetect", "4"))
        self.comboBox_2.setItemText(4, _translate("SampleDetect", "5"))
        self.comboBox_2.setItemText(5, _translate("SampleDetect", "6"))
        self.comboBox_2.setItemText(6, _translate("SampleDetect", "7"))
        self.comboBox_2.setItemText(7, _translate("SampleDetect", "8"))
        self.comboBox_2.setItemText(8, _translate("SampleDetect", "9"))
        self.comboBox_2.setItemText(9, _translate("SampleDetect", "10"))
        self.Hint.setText(_translate("SampleDetect", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">you must enter all fields.</span></p></body></html>"))
        self.Hint_2.setText(_translate("SampleDetect", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">These features are include patient age</span></p></body></html>"))
        self.Help.setToolTip(_translate("SampleDetect", "Help"))
        self.Help.setStatusTip(_translate("SampleDetect", "Need a help ? go to help center."))
        self.Help.setShortcut(_translate("SampleDetect", "Ctrl+H"))
        self.SampleB.setToolTip(_translate("SampleDetect", "Sample detect"))
        self.SampleB.setStatusTip(_translate("SampleDetect", "detect tumor by sample  "))
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


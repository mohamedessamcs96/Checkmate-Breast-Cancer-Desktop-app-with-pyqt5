
import sqlite3

def Create_Table():
    #Notes
    #if exist connect if not create a one
    
    
    # I will take an object from the data base 
    #connection=sqlite3.connect("sqlitedatabase.db")
    connection=sqlite3.connect("sqlitedatabase5.db")

    ''' 
    Admin Tables
    '''
    connection.execute("CREATE TABLE ADMIN(admin TEXT NOT NULL,EMAIL TEXT,PASSWORD TEXT)")
    #The Question mark ? is a Place holder for the data 
    connection.execute("INSERT INTO ADMIN VALUES(?,?,?)",('admin','htibreastcancerapp.finalproject@gmail.com','htibcadmin')) 
    
    
    
    '''
    User
    
    '''
    connection.execute("CREATE TABLE DOCTORS(USER TEXT NOT NULL,EMAIL TEXT,PASSWORD TEXT,PATH INT NOT NULL)")
    
    
       
    '''
    Patient Table
    '''
    connection.execute("CREATE TABLE  PATIENT(FIRSTNAME TEXT NOT NULL,FAMILYNAME TEXT NOT NULL,PATIENTID TEXT  NOT NULL ,PHONENUMBER TEXT NOT NULL,BIRTHDATE text format 'DD-MM-YYYY' NOT NULL,GENDER TEXT NOT NULL,CANCER TEXT NOT NULL,DIABETES TEXT NOT NULL,BLOODPRESSURE TEXT NOT NULL,ANEMIA TEXT NOT NULL,PRIMARY KEY (PATIENTID))")
    connection.execute("INSERT INTO PATIENT VALUES(?,?,?,?,?,?,?,?,?,?)",('moh','essam',35545678910112,'01144931949','01-12-2010','Male','Yes','Yes','Yes','Yes'))
    connection.commit() 
    result=connection.execute("SELECT * FROM PATIENT")    
    
    
    for data in result:
        print("name:",data[0])
        print("family:",data[1])
        print("id:",data[2]) 
        print("date:",data[3])
        print("gender:",data[4])
        print("Cancer:",data[5])
        print("Diabetes:",data[6])
        print("Blood Pressure:",data[7])
        print("Anemia:",data[8])
    

    #time Now
    #timenow=datetime.datetime.now()
    
    '''
    The Records tables
    '''                                                                                         
    connection.execute("CREATE TABLE BLOODANALYSIS(BLOODID INTEGER PRIMARY KEY AUTOINCREMENT,DATE REAL,BLOODRESULT TEXT NOT NULL,BMI TEXT NOT NULL,LEPTIN TEXT NOT NULL,GLUCOSE TEXT NOT NULL,ADIPONECTIN TEXT NOT NULL,INSULIN TEXT NOT NULL,RESISTINT TEXT NOT NULL,HOMA TEXT NOT NULL,MCP TEXT NULL,PATIENTID TEXT NOT NULL)")
    connection.execute("CREATE TABLE MOMGRAPH(MOMOID INTEGER PRIMARY KEY AUTOINCREMENT,DATE REAL,MAMORESULT TEXT NOT NULL,BIRADS TEXT NOT NULL,MASSHAPE TEXT NOT NULL,MASSSMARGIN TEXT NOT NULL,MASSDENISITY TEXT NOT NULL,BREAST TEXT NOT NULL,BREASTSQUAD TEXT NOT NULL,TUMORSIZE TEXT NOT NULL,DEGMALIG TEXT NOT NULL,INVFALSEDES TEXT NOT NULL,IRRADIAT TEXT NOT NULL,PATIENTID TEXT NOT NULL)")
    connection.execute("CREATE TABLE SAMPLE(SampleID INTEGER PRIMARY KEY AUTOINCREMENT,DATE REAL,SAMPLRESULT TEXT NOT NULL,TUMORRECURRENCE TEXT NOT NULL,BREAST TEXT NOT NULL,BREASTSQUAD TEXT NOT NULL,TUMORSIZE TEXT NOT NULL,DEGMALIG TEXT NOT NULL,IRRADIAT TEXT NOT NULL,INVFALSEDES TEXT NOT NULL,PATIENTID TEXT NOT NULL)")
    #connection.execute("CREATE TABLE  RECURRENCE(RECURRENCEID INTEGER PRIMARY KEY AUTOINCREMENT ,MEFALSEPAUSE TEXT NOT NULL,BREASTQUAD  TEXT NOT NULL,FALSEDECAPS TEXT NOT NULL,IRRADIAT  TEXT NOT NULL,DEGMALIG INT NOT NULL,TUMORSIZE INT NOT NULL,BREAST INT NOT NULL,INVFALSEDES INT NULL,TIME_NOW TEXT NOT NULL,PATIENTID INT  NOT NULL,FOREIGN KEY (PATIENTID) REFERENCES PATIENT(PATIENTID))")

    connection.commit()
    connection.close()
    
    
Create_Table()

    
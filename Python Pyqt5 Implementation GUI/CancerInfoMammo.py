# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Recerrence.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Mammography import Ui_MammoDetect
class Ui_CancerInfo(object):

        #I Call it when the account and the password of the user is match
    def openMammoWindowPage(self):
            self.getting_data()    
            #Create an object from two classes the qtgui and qmain window is inside
            self.selectWindow=QtWidgets.QMainWindow()
            self.ui=Ui_MammoDetect()
            self.ui.setupUi(self.selectWindow)
            self.selectWindow.show()
            
    def getting_data(self):    
        global Mefalsepause,Breastquad,Falsedecaps,Irradiat,Degmalig,Tumorsize,Breast,Invnodes
        Mefalsepause =self.comboBox_26.currentText()
        Breastquad=self.comboBox_27.currentText()
        Falsedecaps=self.comboBox_24.currentText()
        Irradiat =self.comboBox_25.currentText()
        Degmalig =self.comboBox_22.currentText()
        Tumorsize  =self.lineEdit_19.text()
        Breast=self.comboBox_20.currentText()
        Invnodes =self.lineEdit_20.text()
        import Mammography
        Mammography.Mefalsepause=Mefalsepause
        Mammography.Breastquad=Breastquad
        Mammography.Falsedecaps=Falsedecaps
        Mammography.Irradiat=Irradiat
        Mammography.Degmalig=Degmalig
        Mammography.Tumorsize=Tumorsize
        Mammography.Breast=Breast
        Mammography.Invnodes=Invnodes
        
        
        #doesn't avilable
    def DAWarnning(self):
        self.ShowMessageBox('Warning',"You can't open this")
    def SPWarnning(self):
        self.ShowMessageBox('Warning',"You are in the same page")
        
    def ShowMessageBox(self,title,message):
        messagebox=QtWidgets.QMessageBox()
        messagebox.setIcon(QtWidgets.QMessageBox.Warning)
        messagebox.setWindowTitle(title)
        messagebox.setText(message)
        messagebox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        messagebox.exec_() 
    
    def setupUi(self, MainWindow):
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
        self.RecerrenceT = QtWidgets.QLabel(self.frame)
        self.RecerrenceT.setGeometry(QtCore.QRect(330, 90, 351, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        self.RecerrenceT.setFont(font)
        self.RecerrenceT.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.RecerrenceT.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.RecerrenceT.setFrameShape(QtWidgets.QFrame.Box)
        self.RecerrenceT.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.RecerrenceT.setObjectName("RecerrenceT")
        self.BloodF = QtWidgets.QFrame(self.frame)
        self.BloodF.setGeometry(QtCore.QRect(240, 110, 531, 411))
        self.BloodF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BloodF.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.BloodF.setObjectName("BloodF")
        self.DetectB = QtWidgets.QPushButton(self.BloodF)
        self.DetectB.setGeometry(QtCore.QRect(210, 310, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.DetectB.setFont(font)
        self.DetectB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DetectB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.DetectB.setObjectName("Continue")
        self.DetectB.clicked.connect(self.openMammoWindowPage)
        self.ResetB = QtWidgets.QPushButton(self.BloodF)
        self.ResetB.setGeometry(QtCore.QRect(330, 310, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ResetB.setFont(font)
        self.ResetB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResetB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.ResetB.setObjectName("ResetB")
        self.label_59 = QtWidgets.QLabel(self.BloodF)
        self.label_59.setGeometry(QtCore.QRect(21, 140, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_59.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_59.setObjectName("label_59")
        self.label_57 = QtWidgets.QLabel(self.BloodF)
        self.label_57.setGeometry(QtCore.QRect(49, 190, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_57.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_57.setObjectName("label_57")
        self.label_3 = QtWidgets.QLabel(self.BloodF)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_54 = QtWidgets.QLabel(self.BloodF)
        self.label_54.setGeometry(QtCore.QRect(60, 240, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_54.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_54.setObjectName("label_54")
        self.comboBox_24 = QtWidgets.QComboBox(self.BloodF)
        self.comboBox_24.setGeometry(QtCore.QRect(161, 140, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_24.setFont(font)
        self.comboBox_24.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_24.setStyleSheet("")
        self.comboBox_24.setEditable(False)
        self.comboBox_24.setMaxVisibleItems(10)
        self.comboBox_24.setMaxCount(10)
        self.comboBox_24.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_24.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_24.setMinimumContentsLength(1)
        self.comboBox_24.setDuplicatesEnabled(False)
        self.comboBox_24.setModelColumn(0)
        self.comboBox_24.setObjectName("comboBox_24")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_26 = QtWidgets.QComboBox(self.BloodF)
        self.comboBox_26.setGeometry(QtCore.QRect(161, 90, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_26.setFont(font)
        self.comboBox_26.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_26.setStyleSheet("")
        self.comboBox_26.setEditable(False)
        self.comboBox_26.setMaxVisibleItems(10)
        self.comboBox_26.setMaxCount(10)
        self.comboBox_26.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_26.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_26.setMinimumContentsLength(1)
        self.comboBox_26.setIconSize(QtCore.QSize(3, 3))
        self.comboBox_26.setDuplicatesEnabled(False)
        self.comboBox_26.setModelColumn(0)
        self.comboBox_26.setObjectName("comboBox_26")
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_22 = QtWidgets.QComboBox(self.BloodF)
        self.comboBox_22.setGeometry(QtCore.QRect(160, 190, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_22.setFont(font)
        self.comboBox_22.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_22.setStyleSheet("")
        self.comboBox_22.setEditable(False)
        self.comboBox_22.setMaxVisibleItems(10)
        self.comboBox_22.setMaxCount(10)
        self.comboBox_22.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_22.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_22.setMinimumContentsLength(1)
        self.comboBox_22.setDuplicatesEnabled(False)
        self.comboBox_22.setModelColumn(0)
        self.comboBox_22.setObjectName("comboBox_22")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_20 = QtWidgets.QComboBox(self.BloodF)
        self.comboBox_20.setGeometry(QtCore.QRect(160, 240, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_20.setFont(font)
        self.comboBox_20.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_20.setStyleSheet("")
        self.comboBox_20.setEditable(False)
        self.comboBox_20.setMaxVisibleItems(10)
        self.comboBox_20.setMaxCount(10)
        self.comboBox_20.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_20.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_20.setMinimumContentsLength(1)
        self.comboBox_20.setDuplicatesEnabled(False)
        self.comboBox_20.setModelColumn(0)
        self.comboBox_20.setObjectName("comboBox_20")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.label_56 = QtWidgets.QLabel(self.BloodF)
        self.label_56.setGeometry(QtCore.QRect(269, 190, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_56.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_56.setObjectName("label_56")
        self.label_55 = QtWidgets.QLabel(self.BloodF)
        self.label_55.setGeometry(QtCore.QRect(269, 240, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_55.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_55.setObjectName("label_55")
        self.PreviousB = QtWidgets.QPushButton(self.BloodF)
        self.PreviousB.setGeometry(QtCore.QRect(90, 310, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.PreviousB.setFont(font)
        self.PreviousB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PreviousB.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.PreviousB.setObjectName("PreviousB")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.BloodF)
        self.lineEdit_19.setGeometry(QtCore.QRect(370, 190, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.BloodF)
        self.lineEdit_20.setGeometry(QtCore.QRect(369, 240, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_58 = QtWidgets.QLabel(self.BloodF)
        self.label_58.setGeometry(QtCore.QRect(269, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_58.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_58.setObjectName("label_58")
        self.comboBox_25 = QtWidgets.QComboBox(self.BloodF)
        self.comboBox_25.setGeometry(QtCore.QRect(370, 140, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_25.setFont(font)
        self.comboBox_25.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_25.setStyleSheet("")
        self.comboBox_25.setEditable(False)
        self.comboBox_25.setMaxVisibleItems(10)
        self.comboBox_25.setMaxCount(10)
        self.comboBox_25.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_25.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_25.setMinimumContentsLength(1)
        self.comboBox_25.setDuplicatesEnabled(False)
        self.comboBox_25.setModelColumn(0)
        self.comboBox_25.setObjectName("comboBox_25")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.label_60 = QtWidgets.QLabel(self.BloodF)
        self.label_60.setGeometry(QtCore.QRect(270, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_60.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_60.setObjectName("label_60")
        self.comboBox_27 = QtWidgets.QComboBox(self.BloodF)
        self.comboBox_27.setGeometry(QtCore.QRect(370, 90, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.comboBox_27.setFont(font)
        self.comboBox_27.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_27.setStyleSheet("")
        self.comboBox_27.setEditable(False)
        self.comboBox_27.setMaxVisibleItems(10)
        self.comboBox_27.setMaxCount(10)
        self.comboBox_27.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_27.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_27.setMinimumContentsLength(1)
        self.comboBox_27.setDuplicatesEnabled(False)
        self.comboBox_27.setModelColumn(0)
        self.comboBox_27.setObjectName("comboBox_27")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.frame_3 = QtWidgets.QFrame(self.BloodF)
        self.frame_3.setGeometry(QtCore.QRect(10, 360, 221, 41))
        self.frame_3.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Hint_2 = QtWidgets.QLabel(self.frame_3)
        self.Hint_2.setGeometry(QtCore.QRect(38, 10, 171, 21))
        self.Hint_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Hint_2.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.Hint_2.setObjectName("Hint_2")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(22, 10, 21, 21))
        self.label_2.setStyleSheet("image: url(:/images/img/Hint.png);\n"
"background-color: rgb(242, 242, 242);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 550, 221, 51))
        self.frame_2.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Hint = QtWidgets.QLabel(self.frame_2)
        self.Hint.setGeometry(QtCore.QRect(38, 10, 171, 31))
        self.Hint.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.Hint.setStyleSheet("background-color: rgb(242, 242, 242);")
        self.Hint.setObjectName("Hint")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(22, 17, 21, 21))
        self.label.setStyleSheet("image: url(:/images/img/Hint.png);\n"
"background-color: rgb(242, 242, 242);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Logo = QtWidgets.QLabel(self.frame)
        self.Logo.setGeometry(QtCore.QRect(30, 20, 161, 111))
        self.Logo.setStyleSheet("image: url(:/images/img/Logo.png);")
        self.Logo.setText("")
        self.Logo.setObjectName("Logo")
        self.frame_2.raise_()
        self.Obacity.raise_()
        self.BloodF.raise_()
        self.RecerrenceT.raise_()
        self.Logo.raise_()
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
        self.comboBox_24.setCurrentIndex(0)
        self.comboBox_26.setCurrentIndex(0)
        self.comboBox_22.setCurrentIndex(0)
        self.comboBox_20.setCurrentIndex(0)
        self.comboBox_25.setCurrentIndex(0)
        self.comboBox_27.setCurrentIndex(0)
        self.ResetB.clicked.connect(self.comboBox_25.clear)
        self.ResetB.clicked.connect(self.comboBox_24.clear)
        self.ResetB.clicked.connect(self.comboBox_27.clear)
        self.ResetB.clicked.connect(self.comboBox_20.clear)
        self.ResetB.clicked.connect(self.comboBox_26.clear)
        self.ResetB.clicked.connect(self.comboBox_22.clear)
        self.ResetB.clicked.connect(self.lineEdit_19.clear)
        self.ResetB.clicked.connect(self.lineEdit_20.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.PatientInfoB, self.DiagnosisB)
        MainWindow.setTabOrder(self.DiagnosisB, self.SampleB)
        MainWindow.setTabOrder(self.SampleB, self.MammoB)
        MainWindow.setTabOrder(self.MammoB, self.FNAB)
        MainWindow.setTabOrder(self.FNAB, self.PrintB)
        MainWindow.setTabOrder(self.PrintB, self.comboBox_26)
        MainWindow.setTabOrder(self.comboBox_26, self.comboBox_24)
        MainWindow.setTabOrder(self.comboBox_24, self.comboBox_22)
        MainWindow.setTabOrder(self.comboBox_22, self.comboBox_20)
        MainWindow.setTabOrder(self.comboBox_20, self.comboBox_27)
        MainWindow.setTabOrder(self.comboBox_27, self.comboBox_25)
        MainWindow.setTabOrder(self.comboBox_25, self.lineEdit_19)
        MainWindow.setTabOrder(self.lineEdit_19, self.lineEdit_20)
        MainWindow.setTabOrder(self.lineEdit_20, self.PreviousB)
        MainWindow.setTabOrder(self.PreviousB, self.DetectB)
        MainWindow.setTabOrder(self.DetectB, self.ResetB)
        MainWindow.setTabOrder(self.ResetB, self.Help)

        '''
        Button ACtion 
        
        '''
        self.PatientInfoB.clicked.connect(self.DAWarnning)
        self.MammoB.clicked.connect(self.DAWarnning)
        self.DiagnosisB.clicked.connect(self.DAWarnning)
        self.FNAB.clicked.connect(self.DAWarnning)
        self.PrintB.clicked.connect(self.DAWarnning)
        self.SampleB.clicked.connect(self.DAWarnning)
        '''
        Button ACtion 
        
        '''

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tumor Recurrence"))
        self.RecerrenceT.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#4d4d4d;\">Tumor Recerrence</span></p></body></html>"))
        self.DetectB.setToolTip(_translate("MainWindow", "Continue"))
        self.DetectB.setText(_translate("MainWindow", "Continue"))
        self.DetectB.setShortcut(_translate("MainWindow", "Enter"))
        self.ResetB.setToolTip(_translate("MainWindow", "Reset"))
        self.ResetB.setStatusTip(_translate("MainWindow", "Reset all fields"))
        self.ResetB.setText(_translate("MainWindow", "Reset"))
        self.ResetB.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.label_59.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#232323;\">Falsede-caps :</span></p></body></html>"))
        self.label_57.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#232323;\">Deg-malig :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#232323;\">Mefalsepause :</span></p></body></html>"))
        self.label_54.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#232323;\">Breast  :</span></p></body></html>"))
        self.comboBox_24.setItemText(0, _translate("MainWindow", "True"))
        self.comboBox_24.setItemText(1, _translate("MainWindow", "False"))
        self.comboBox_26.setItemText(0, _translate("MainWindow", "Premefalse"))
        self.comboBox_26.setItemText(1, _translate("MainWindow", "ge40"))
        self.comboBox_26.setItemText(2, _translate("MainWindow", "It40"))
        self.comboBox_22.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_22.setItemText(1, _translate("MainWindow", "2"))
        self.comboBox_22.setItemText(2, _translate("MainWindow", "3"))
        self.comboBox_20.setItemText(0, _translate("MainWindow", "Right"))
        self.comboBox_20.setItemText(1, _translate("MainWindow", "Left"))
        self.label_56.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#232323;\">Tumor-size :</span></p></body></html>"))
        self.label_55.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#232323;\">Inv-falsedes :</span></p></body></html>"))
        self.PreviousB.setToolTip(_translate("MainWindow", "Previous"))
        self.PreviousB.setStatusTip(_translate("MainWindow", "Previous"))
        self.PreviousB.setText(_translate("MainWindow", "Previous"))
        self.label_58.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#232323;\">Irradiat :</span></p></body></html>"))
        self.comboBox_25.setItemText(0, _translate("MainWindow", "True"))
        self.comboBox_25.setItemText(1, _translate("MainWindow", "False"))
        self.label_60.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#232323;\">Breast-quad :</span></p></body></html>"))
        self.comboBox_27.setItemText(0, _translate("MainWindow", "Right up"))
        self.comboBox_27.setItemText(1, _translate("MainWindow", "Right low"))
        self.comboBox_27.setItemText(2, _translate("MainWindow", "Central"))
        self.comboBox_27.setItemText(3, _translate("MainWindow", "Left up"))
        self.comboBox_27.setItemText(4, _translate("MainWindow", "Left low"))
        self.Hint_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">you must enter all fields.</span></p></body></html>"))
        self.Hint.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">you must enter all fields.</span></p></body></html>"))
        self.Help.setToolTip(_translate("MainWindow", "Help"))
        self.Help.setStatusTip(_translate("MainWindow", "Need a help ? go to help center."))
        self.Help.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.SampleB.setToolTip(_translate("MainWindow", "Sample detect"))
        self.SampleB.setStatusTip(_translate("MainWindow", "detect tumor by sample"))
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
    ui = Ui_CancerInfo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


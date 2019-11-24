# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DonorDetails.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Login as l
import Database as db
import sqlite3


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 418)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 71, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(110, 30, 171, 41))
        self.idLabel.setText("")
        self.idLabel.setObjectName("idLabel")
        self.nameLE = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLE.setGeometry(QtCore.QRect(110, 90, 201, 31))
        self.nameLE.setObjectName("nameLE")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 140, 201, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.maleRB = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.maleRB.setFont(font)
        self.maleRB.setObjectName("maleRB")
        self.horizontalLayout.addWidget(self.maleRB)
        self.femaleRB = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.femaleRB.setFont(font)
        self.femaleRB.setObjectName("femaleRB")
        self.horizontalLayout.addWidget(self.femaleRB)
        self.addressTE = QtWidgets.QTextEdit(self.centralwidget)
        self.addressTE.setGeometry(QtCore.QRect(110, 190, 200, 81))
        self.addressTE.setObjectName("addressTE")
        self.phoneLE = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneLE.setGeometry(QtCore.QRect(110, 290, 201, 31))
        self.phoneLE.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.phoneLE.setObjectName("phoneLE")
        self.emailLE = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLE.setGeometry(QtCore.QRect(110, 330, 201, 31))
        self.emailLE.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.emailLE.setObjectName("emailLE")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(370, 120, 76, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.lastDonatedDE = QtWidgets.QDateEdit(self.centralwidget)
        self.lastDonatedDE.setGeometry(QtCore.QRect(450, 210, 111, 31))
        self.lastDonatedDE.setObjectName("lastDonatedDE")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(460, 310, 141, 61))
        self.addBtn.setObjectName("addBtn")
        self.bloodGroupCB = QtWidgets.QComboBox(self.centralwidget)
        self.bloodGroupCB.setGeometry(QtCore.QRect(450, 140, 111, 31))
        self.bloodGroupCB.setObjectName("bloodGroupCB")
        self.bloodGroupCB.addItem("")
        self.bloodGroupCB.addItem("")
        self.bloodGroupCB.addItem("")
        self.bloodGroupCB.addItem("")
        self.bloodGroupCB.addItem("")
        self.bloodGroupCB.addItem("")
        self.bloodGroupCB.addItem("")
        self.bloodGroupCB.addItem("")
        self.bloodGroupCB.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.addBtn.clicked.connect(self.read)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Donor ID"))
        self.label.setText(_translate("MainWindow", "Full Name"))
        self.label_2.setText(_translate("MainWindow", "Gender"))
        self.label_3.setText(_translate("MainWindow", "Address"))
        self.label_4.setText(_translate("MainWindow", "Phone"))
        self.label_5.setText(_translate("MainWindow", "Email"))
        self.maleRB.setText(_translate("MainWindow", "Male"))
        self.femaleRB.setText(_translate("MainWindow", "Female"))
        self.label_7.setText(_translate("MainWindow", "Blood Group"))
        self.label_9.setText(_translate("MainWindow", "Last Donated"))
        self.addBtn.setText(_translate("MainWindow", "Add To Record"))
        self.bloodGroupCB.setItemText(0, _translate("MainWindow", "Select Group"))
        self.bloodGroupCB.setItemText(1, _translate("MainWindow", "A +"))
        self.bloodGroupCB.setItemText(2, _translate("MainWindow", "A -"))
        self.bloodGroupCB.setItemText(3, _translate("MainWindow", "B +"))
        self.bloodGroupCB.setItemText(4, _translate("MainWindow", "B -"))
        self.bloodGroupCB.setItemText(5, _translate("MainWindow", "O +"))
        self.bloodGroupCB.setItemText(6, _translate("MainWindow", "O -"))
        self.bloodGroupCB.setItemText(7, _translate("MainWindow", "AB +"))
        self.bloodGroupCB.setItemText(8, _translate("MainWindow", "AB -"))

    def read(self):

        # connObj = sqlite3.connect('BloodBank.db')
        # cur = connObj.cursor()

        name = self.nameLE.text()
        address = self.addressTE.text()
        phone = self.phoneLE.text()
        email = self.emailLE.text()
        gender = 'm'
        bloodGroup = 'a'
        lastDonated = '00-00-0000'

        BBID = 345

        #db.cur.execute('INSERT INTO DonorDetails (Name, Location, Gender, BloodGroup, LastDonated, Email, Phone, BBID) VALUES (?,?,?,?,?,?,?,?)', (name,address,gender,bloodGroup,lastDonated,email,phone,BBID))

        db.donorDetails(name,address,phone,email,gender,bloodGroup,lastDonated,BBID)

        #dId = db.cur.execute('''SELECT DID FROM DonorDetails''')

       # db.connObj.commit()

        #set text for label


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

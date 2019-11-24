# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddBloodBank.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Database as db

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(344, 382)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 101, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.passwordLE = QtWidgets.QLineEdit(Dialog)
        self.passwordLE.setGeometry(QtCore.QRect(140, 240, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordLE.setFont(font)
        self.passwordLE.setObjectName("passwordLE")
        self.nameLE = QtWidgets.QLineEdit(Dialog)
        self.nameLE.setGeometry(QtCore.QRect(140, 110, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLE.setFont(font)
        self.nameLE.setObjectName("nameLE")
        self.idLabel = QtWidgets.QLabel(Dialog)
        self.idLabel.setGeometry(QtCore.QRect(140, 30, 131, 41))
        self.idLabel.setText("")
        self.idLabel.setObjectName("idLabel")
        self.locationLE = QtWidgets.QLineEdit(Dialog)
        self.locationLE.setGeometry(QtCore.QRect(140, 180, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.locationLE.setFont(font)
        self.locationLE.setObjectName("locationLE")
        self.add = QtWidgets.QPushButton(Dialog)
        self.add.setGeometry(QtCore.QRect(234, 312, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add.setFont(font)
        self.add.setObjectName("add")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.add.clicked.connect(self.read)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Blood Bank ID"))
        self.label_2.setText(_translate("Dialog", "Name"))
        self.label_3.setText(_translate("Dialog", "Location"))
        self.label_4.setText(_translate("Dialog", "Create Password"))
        self.add.setText(_translate("Dialog", "Add"))

    def read(self):
        name = self.nameLE.text()
        location = self.locationLE.text()
        password = self.passwordLE.text()

        db.bloodbank(name,location,password)

        # db.cur.execute('''INSERT INTO BloodBankDetails (BBName, Location) VALUES (?,?)''', (name,location))
        # db.cur.execute('''INSERT INTO login (Password) VALUES (?)''', (password))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

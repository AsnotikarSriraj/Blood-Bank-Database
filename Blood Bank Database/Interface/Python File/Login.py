# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from InvalidCredentials import Ui_invalidCredentials
import AddBloodBank as bb
import AddHospital as h
import Options as o
import Database as db

class Ui_Dialog(object):

    global dbId
    global dbPassword

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(366, 503)
        self.loginBtn = QtWidgets.QPushButton(Dialog)
        self.loginBtn.setGeometry(QtCore.QRect(234, 332, 91, 31))
        self.loginBtn.setObjectName("loginBtn")
        self.passwordLE = QtWidgets.QLineEdit(Dialog)
        self.passwordLE.setGeometry(QtCore.QRect(60, 270, 261, 41))
        self.passwordLE.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.passwordLE.setText("")
        self.passwordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLE.setObjectName("passwordLE")
        self.idLE = QtWidgets.QLineEdit(Dialog)
        self.idLE.setGeometry(QtCore.QRect(60, 210, 261, 41))
        self.idLE.setText("")
        self.idLE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.idLE.setReadOnly(False)
        self.idLE.setObjectName("idLE")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(50, 190, 281, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(50, 370, 281, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 400, 261, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBBBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addBBBtn.setObjectName("addBBBtn")
        self.horizontalLayout.addWidget(self.addBBBtn)
        self.addHBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addHBtn.setObjectName("addHBtn")
        self.horizontalLayout.addWidget(self.addHBtn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.loginBtn.clicked.connect(self.verify)
        self.addBBBtn.clicked.connect(self.addBB)
        self.addHBtn.clicked.connect(self.addH)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginBtn.setText(_translate("Dialog", "Login"))
        self.passwordLE.setPlaceholderText(_translate("Dialog", "Password"))
        self.idLE.setPlaceholderText(_translate("Dialog", "ID"))
        self.addBBBtn.setText(_translate("Dialog", "Add Blood Bank"))
        self.addHBtn.setText(_translate("Dialog", "Add Hospital"))

    def invalidCredentials(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_invalidCredentials()
        self.ui.setupUi(self.window)
        self.window.show()

    def options(self):
        self.window = QtWidgets.QDialog()
        self.ui = o.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def addBB(self):
        self.window = QtWidgets.QDialog()
        self.ui = bb.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def addH(self):
        self.window = QtWidgets.QDialog()
        self.ui = h.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def verify(self):

        id = self.idLE.text()
        password = self.passwordLE.text()

        if ((id == "master" and password == "master123") or (id == dbId and password == dbPassword)):
            self.options()
        else:
            self.invalidCredentials()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

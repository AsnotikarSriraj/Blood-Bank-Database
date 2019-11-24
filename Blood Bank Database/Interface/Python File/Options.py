# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Options.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import DonorDetails as dd
import UpdateStock as us
import View as v


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(284, 421)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 191, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout.addWidget(self.addBtn)
        self.viewBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.viewBtn.setFont(font)
        self.viewBtn.setObjectName("viewBtn")
        self.verticalLayout.addWidget(self.viewBtn)
        self.updateBtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.updateBtn.setFont(font)
        self.updateBtn.setObjectName("updateBtn")
        self.verticalLayout.addWidget(self.updateBtn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.addBtn.clicked.connect(self.addDonor)
        self.viewBtn.clicked.connect(self.view)
        self.updateBtn.clicked.connect(self.updateStock)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addBtn.setText(_translate("Dialog", "Add Donor"))
        self.viewBtn.setText(_translate("Dialog", "View Details"))
        self.updateBtn.setText(_translate("Dialog", "Update Stock"))

    def addDonor(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = dd.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def view(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = v.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def updateStock(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = us.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

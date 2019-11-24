# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSelect = QtWidgets.QMenu(self.menubar)
        self.menuSelect.setObjectName("menuSelect")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBlood_Bank = QtWidgets.QAction(MainWindow)
        self.actionBlood_Bank.setObjectName("actionBlood_Bank")
        self.actionHospital = QtWidgets.QAction(MainWindow)
        self.actionHospital.setObjectName("actionHospital")
        self.menuSelect.addAction(self.actionBlood_Bank)
        self.menuSelect.addAction(self.actionHospital)
        self.menubar.addAction(self.menuSelect.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSelect.setTitle(_translate("MainWindow", "Select"))
        self.actionBlood_Bank.setText(_translate("MainWindow", "Blood Bank"))
        self.actionHospital.setText(_translate("MainWindow", "Hospital"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

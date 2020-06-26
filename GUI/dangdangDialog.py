# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dangdangDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dangdangDialog(object):
    def setupUi(self, dangdangDialog):
        dangdangDialog.setObjectName("dangdangDialog")
        dangdangDialog.resize(661, 457)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dangdangDialog.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(dangdangDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(dangdangDialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)

        self.retranslateUi(dangdangDialog)
        QtCore.QMetaObject.connectSlotsByName(dangdangDialog)

    def retranslateUi(self, dangdangDialog):
        _translate = QtCore.QCoreApplication.translate
        dangdangDialog.setWindowTitle(_translate("dangdangDialog", "Dialog"))
import image

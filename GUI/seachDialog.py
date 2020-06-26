# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seachDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_searchResultDialog(object):
    def setupUi(self, searchResultDialog):
        searchResultDialog.setObjectName("searchResultDialog")
        searchResultDialog.resize(648, 372)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        searchResultDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(searchResultDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(searchResultDialog)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(searchResultDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.countLabel = QtWidgets.QLabel(searchResultDialog)
        self.countLabel.setObjectName("countLabel")
        self.horizontalLayout.addWidget(self.countLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(searchResultDialog)
        QtCore.QMetaObject.connectSlotsByName(searchResultDialog)

    def retranslateUi(self, searchResultDialog):
        _translate = QtCore.QCoreApplication.translate
        searchResultDialog.setWindowTitle(_translate("searchResultDialog", "Dialog"))
        self.label.setText(_translate("searchResultDialog", "当前共搜索到 "))
        self.countLabel.setText(_translate("searchResultDialog", "TextLabel"))
import image

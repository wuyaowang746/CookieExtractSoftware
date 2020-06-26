# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loadingDialog(object):
    def setupUi(self, loadingDialog):
        loadingDialog.setObjectName("loadingDialog")
        loadingDialog.resize(200, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loadingDialog.sizePolicy().hasHeightForWidth())
        loadingDialog.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(loadingDialog)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(loadingDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.retranslateUi(loadingDialog)
        QtCore.QMetaObject.connectSlotsByName(loadingDialog)

    def retranslateUi(self, loadingDialog):
        _translate = QtCore.QCoreApplication.translate
        loadingDialog.setWindowTitle(_translate("loadingDialog", "Dialog"))

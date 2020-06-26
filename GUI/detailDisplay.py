# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_detailDialog(object):
    def setupUi(self, detailDialog):
        detailDialog.setObjectName("detailDialog")
        detailDialog.resize(659, 486)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        detailDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(detailDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(detailDialog)
        self.label.setStyleSheet("font: 36pt \"Arial\";\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.hosttextBrowser = QtWidgets.QTextBrowser(detailDialog)
        self.hosttextBrowser.setStyleSheet("font: 18pt \"Arial\";")
        self.hosttextBrowser.setObjectName("hosttextBrowser")
        self.verticalLayout.addWidget(self.hosttextBrowser)
        self.label_2 = QtWidgets.QLabel(detailDialog)
        self.label_2.setStyleSheet("font: 36pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.nametextBrowser = QtWidgets.QTextBrowser(detailDialog)
        self.nametextBrowser.setStyleSheet("font: 18pt \"Arial\";")
        self.nametextBrowser.setObjectName("nametextBrowser")
        self.verticalLayout.addWidget(self.nametextBrowser)
        self.label_3 = QtWidgets.QLabel(detailDialog)
        self.label_3.setStyleSheet("font: 36pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.valuetextBrowser = QtWidgets.QTextBrowser(detailDialog)
        self.valuetextBrowser.setStyleSheet("font: 18pt \"Arial\";")
        self.valuetextBrowser.setObjectName("valuetextBrowser")
        self.verticalLayout.addWidget(self.valuetextBrowser)
        self.label_4 = QtWidgets.QLabel(detailDialog)
        self.label_4.setStyleSheet("font: 36pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pathtextBrowser = QtWidgets.QTextBrowser(detailDialog)
        self.pathtextBrowser.setStyleSheet("font: 18pt \"Arial\";")
        self.pathtextBrowser.setObjectName("pathtextBrowser")
        self.verticalLayout.addWidget(self.pathtextBrowser)

        self.retranslateUi(detailDialog)
        QtCore.QMetaObject.connectSlotsByName(detailDialog)

    def retranslateUi(self, detailDialog):
        _translate = QtCore.QCoreApplication.translate
        detailDialog.setWindowTitle(_translate("detailDialog", "Dialog"))
        self.label.setText(_translate("detailDialog", "Host："))
        self.label_2.setText(_translate("detailDialog", "Name："))
        self.label_3.setText(_translate("detailDialog", "Value："))
        self.label_4.setText(_translate("detailDialog", "Path："))
import image

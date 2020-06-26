# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_helpDialog(object):
    def setupUi(self, helpDialog):
        helpDialog.setObjectName("helpDialog")
        helpDialog.resize(591, 240)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(helpDialog.sizePolicy().hasHeightForWidth())
        helpDialog.setSizePolicy(sizePolicy)
        helpDialog.setMinimumSize(QtCore.QSize(330, 240))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        helpDialog.setWindowIcon(icon)
        helpDialog.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(helpDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(helpDialog)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.144, 0.578, 1.0, 0.05)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.465909, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(230, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.144, 0.578, 1.0, 0.05)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.465909, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(230, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.144, 0.578, 1.0, 0.05)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.465909, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(230, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.144, 0.578, 1.0, 0.05)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.465909, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(230, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.144, 0.578, 1.0, 0.05)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.465909, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(230, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.144, 0.578, 1.0, 0.05)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.465909, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(230, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(0.144, 0.578, 1.0, 0.05)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.465909, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(230, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.144, 0.578, 1.0, 0.05)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.465909, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(230, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.144, 0.578, 1.0, 0.05)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.465909, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(230, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.textBrowser.setPalette(palette)
        self.textBrowser.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.144, y1:0.578, x2:1, y2:0.05, stop:0.465909 rgba(0, 0, 0, 255), stop:1 rgba(230, 0, 0, 255));\n"
"font: 15pt \"华文宋体\";")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(helpDialog)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(helpDialog)
        QtCore.QMetaObject.connectSlotsByName(helpDialog)

    def retranslateUi(self, helpDialog):
        _translate = QtCore.QCoreApplication.translate
        helpDialog.setWindowTitle(_translate("helpDialog", "Dialog"))
        self.textBrowser.setHtml(_translate("helpDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'华文宋体\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">本软件主要实现从Google Chrome、Firefox等主流浏览器中提取Cookie并显示。功能点如下：</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">1、可以提取本地浏览器中的Cookie文件并解码</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">2、当鼠标右键点击时会显示该条记录的详细信息。</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">3、可以将提取到的Cookie文件保存为.xls文件</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">4、加载以前保存的cookie.xls文件并显示</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#ffffff;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("helpDialog", "确定"))
import image

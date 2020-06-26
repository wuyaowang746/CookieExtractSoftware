import sys

import numpy
from PyQt5.QtGui import QBrush, QColor, QPixmap, QImage, QMovie
from requests import RequestException

import get_other_cookie
from helpDialog import Ui_helpDialog
from mainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QAbstractItemView, QTableWidgetItem, QHeaderView, \
    QFileDialog, QMessageBox, QLabel
import extract_chrome_cookie
from detailDisplay import Ui_detailDialog
import xlwt
import pandas
from aboutDialog import Ui_aboutDialog
from seachDialog import Ui_searchResultDialog
from dangdangDialog import Ui_dangdangDialog
import getWebContent
import requests
from loadingDialog import Ui_loadingDialog

NETWORK_ERROR = "NETWORK_ERROR"
SUCCESS_CODE = "200"
"""
错误码
"""
CHROME_ERROR = "CHROME_FILE_NOT_EXISTS"
FIREFOX_ERROR = "FIREFOX_FILE_NOT_EXISTS"


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("Cookie提取软件")
        self.showWelcomePage()
        self.set_table()
        # 绑定按钮和对应的事件
        self.saveAction.triggered.connect(self.onSaveAction)
        self.chromeAction.triggered.connect(self.onChromeAction)
        self.firefoxAction.triggered.connect(self.onFireFoxAction)
        self.helpAction.triggered.connect(self.onHelpAction)
        self.openAction.triggered.connect(self.openFile)
        self.aboutAction.triggered.connect(self.onAboutAction)
        self.comboBox.activated.connect(self.search)
        self.analysisAction_2.triggered.connect(self.onCookieAnalysisAction)
        # self.analysisAction.triggered.connect(self.onCookieAnalysisAction)

        # 允许产生右键菜单
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.right_menu)

        # 实例化子窗口
        self.detailDisplay = MyDetailDisplayWindow()
        self.aboutMeDialog = MyAboutDialog()
        self.helpDialog = MyHelpDialog()
        self.seachDialog = MySearchResultDialog()
        self.dangdangDialog = MyDangDangDialog()
        self.loadingDialog = MyLoadingDialog()

        # 允许通过点击表头实现排序,self.flag是一个标记位，用来标记升降序重复的
        self.flag = True
        # 禁用自带排序
        self.tableWidget.setSortingEnabled(False)
        # 显示排序箭头
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.sortByColumns)

    """
    按照表头排序函数
    """

    def sortByColumns(self, column):
        # flag为True的时候升序，flag设为False
        if self.flag:
            self.tableWidget.sortItems(column, QtCore.Qt.AscendingOrder)
            self.flag = False
        else:
            self.tableWidget.sortItems(column, QtCore.Qt.DescendingOrder)
            self.flag = True

    """
    隐藏tableWidget等控件，只显示一个欢迎界面
    """

    def showWelcomePage(self):
        self.tableWidget.hide()
        self.countLabel.hide()
        self.inforLabel.hide()
        self.comboBox.hide()
        self.lineEdit.hide()

    """
    隐藏欢迎界面，显示数据
    """

    def showExtractCookie(self):
        self.backgroundLabel.hide()
        self.tableWidget.show()
        self.countLabel.show()
        self.inforLabel.show()
        self.lineEdit.show()
        self.comboBox.show()

    '''
    对tableWidget进行各种设置
    '''

    def set_table(self):
        # init the tableWidget row and column
        self.tableWidget.setColumnCount(4)
        # 设置表头标题
        self.tableWidget.setHorizontalHeaderLabels(['Host', 'Name', 'Value', 'Path'])
        # 设置表格铺满整个tableWidget控件
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置表格内容无法编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格默认选中的是整个单元格
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置表格列宽
        self.tableWidget.horizontalHeader().resizeSection(0, 120)
        self.tableWidget.horizontalHeader().resizeSection(1, 120)
        self.tableWidget.horizontalHeader().resizeSection(2, 120)
        self.tableWidget.horizontalHeader().resizeSection(3, 120)
        # 最后一列自适应宽度
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)

    """
    把从本地数据库提取出来的cookie填到表里面
    """

    def fillTable(self, items):
        # 将tableWidget行数置为0，避免提取后的数据都在一起
        self.tableWidget.setRowCount(0)
        # if value == 'Chrome':
        #     items = extract_chrome_cookie.get_cookies_from_chrome()
        # elif value == 'Firefox':
        #     items = get_other_cookie.get_cookie_from_firefox()
        # if items == -1:
        #     QMessageBox.warning(self, '警告', '没有找到Cookie文件', QMessageBox.Yes)
        if items:
            self.countLabel.setText(str(len(items)) + ' 条数据')
            for i in range(len(items)):
                item = items[i]
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)
                for j in range(len(item)):
                    item = QTableWidgetItem(str(items[i][j]))
                    self.tableWidget.setItem(row, j, item)
            self.tableWidget.resizeColumnsToContents()
        else:
            self.showWelcomePage()
            QMessageBox.information(self, '提示', '没有找到cookie文件或者cookie文件为空', QMessageBox.Yes)

    """
    chromeAction 的响应函数
    """

    def onChromeAction(self):
        # 隐藏欢迎界面，显示tableWidget等控件

        self.chromeThread = ChromeCookieThread()
        self.chromeThread.signal.connect(self.onChromeCallBack)
        self.chromeThread.start()
        self.showExtractCookie()

    def onChromeCallBack(self, items):
        self.fillTable(items)

    """
    firefoxAction 的响应函数
    @:param fireFoxThread:fireFox的子线程，子线程实现从本地数据库查询数据
    
    """

    def onFireFoxAction(self):
        # 隐藏欢迎界面，显示tableWidget等控件
        self.showExtractCookie()
        self.fireFoxThread = FireFoxCookieThread()
        self.fireFoxThread.signal.connect(self.onFireFoxCallBack)
        self.fireFoxThread.start()

    def onFireFoxCallBack(self, items):
        self.fillTable(items)

    def onAboutAction(self):
        # 打开之前先关闭先前打开的另一个窗口
        self.aboutMeDialog.close()

        self.aboutMeDialog.show()

    def search(self):
        self.seachDialog.close()

        searchText = self.lineEdit.text()
        if searchText == '':
            QMessageBox.information(self.seachDialog, "警告", "您当前没有输入任何信息，请重新输入", QMessageBox.Yes)
        else:
            row = self.comboBox.currentIndex()
            if row == 0:
                items = self.tableWidget.findItems(searchText, QtCore.Qt.MatchExactly)
                self.searchResult(items)
            elif row == 1:
                items = self.tableWidget.findItems(searchText, QtCore.Qt.MatchContains)
                self.searchResult(items)
            self.seachDialog.show()

    """
    将搜索到的结果填表
    @:param dataList: 保存从原来的表里面搜索到的数据
    @:param finalList：保存删除重复数据之后得列表
    """

    def searchResult(self, items):
        dataList = []
        for i in range(len(items)):
            item = items[i]
            row = item.row()
            host = self.tableWidget.item(row, 0).text()
            name = self.tableWidget.item(row, 1).text()
            value = self.tableWidget.item(row, 2).text()
            path = self.tableWidget.item(row, 3).text()
            dataList.append([host, name, value, path])
        self.seachDialog.tableWidget.setRowCount(0)
        finalList = self.deduplication(dataList)
        self.seachDialog.countLabel.setText(str(len(finalList)) + '条数据')
        for i in range(len(finalList)):
            item = finalList[i]
            row = self.seachDialog.tableWidget.rowCount()
            self.seachDialog.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(finalList[i][j]))
                self.seachDialog.tableWidget.setItem(row, j, item)

        self.seachDialog.tableWidget.resizeColumnsToContents()

    """
    去除搜索后列表中的重复项
    """

    def deduplication(self, dataList):
        temp_list = []
        [temp_list.append(o) for o in dataList if o not in temp_list]
        return temp_list

    def onSaveAction(self):
        # 当前表格内没有内容时，即当前界面是初始界面的时候，显示对话框
        rowNum = self.tableWidget.rowCount()
        if rowNum == 0:
            QMessageBox.warning(self, '警告', '当前没有可保存的内容', QMessageBox.Yes)
        else:
            self.getFilePath()

    def onHelpAction(self):
        # 打开之前先关闭先前打开的另一个窗口
        self.helpDialog.close()
        self.helpDialog.show()

    """
    鼠标右键菜单函数，实现右键查看详细信息
    """

    def right_menu(self):
        self.detailDisplay.close()
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        host = self.tableWidget.item(row_num, 0).text()
        name = self.tableWidget.item(row_num, 1).text()
        path = self.tableWidget.item(row_num, 3).text()
        value = self.tableWidget.item(row_num, 2).text()
        detail = [host, name, value, path]
        self.detailDisplay.setLabelText(detail)
        self.detailDisplay.setWindowTitle("详细信息")
        self.detailDisplay.show()

    """
    打开文件选择对话框，选择或者新建文件
    """

    def getFilePath(self):
        fileName = QFileDialog.getSaveFileName(self, "保存文件", "./", ".xls(*.xls)")
        workBook = xlwt.Workbook()
        sheet = workBook.add_sheet("Cookie提取结果", cell_overwrite_ok=True)
        self.saveFile(sheet)
        workBook.save(fileName[0])
        QMessageBox.information(self, '信息提示', '文件已成功保存至 {}'.format(fileName[0]), QMessageBox.Yes)

    """
    保存文件函数
    """

    def saveFile(self, sheet):
        rowNum = self.tableWidget.rowCount()
        columnNum = self.tableWidget.columnCount()
        for i in range(rowNum):
            for j in range(columnNum):
                try:
                    data = str(self.tableWidget.item(i, j).text())
                    sheet.write(i, j, data)
                except Exception as e:
                    print(e)

    """
    打开文件函数
    """

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, "打开文件", "./", ".xls(*.xls)")
        dataFile = ''
        if filename[0]:
            dataFile = pandas.read_excel(filename[0], 0, header=None)
            data = numpy.array(dataFile)
            self.tableWidget.setRowCount(0)
            self.showExtractCookie()
            items = data.tolist()
            self.countLabel.setText(str(len(items)) + ' 条数据')
            for i in range(len(items)):
                item = items[i]
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)
                for j in range(len(item)):
                    item = QTableWidgetItem(str(items[i][j]))
                    self.tableWidget.setItem(row, j, item)

            self.tableWidget.resizeColumnsToContents()

    def onCookieAnalysisAction(self):
        self.dangdangDialog.close()

        self.myThread = MyDangDangThread()
        self.myThread.signal.connect(self.callBack)
        self.loadingDialog.show()
        self.myThread.start()

    def callBack(self, browsingHistory):
        # 如果存在浏览历史
        if browsingHistory:
            if browsingHistory[0] == "NETWORK_ERROR":
                QMessageBox.information(self, '提示', '当前网络出现异常，请检查网络连接后重试', QMessageBox.Yes)
                self.loadingDialog.close()
            else:
                status = self.dangdangDialog.setRowData(browsingHistory)
                if status == SUCCESS_CODE:
                    self.loadingDialog.close()

        else:
            QMessageBox.warning(self, '警告', '当前您的浏览器内没有浏览数据，请确认在当当网上浏览过商品', QMessageBox.Yes)
            self.loadingDialog.close()


"""
鼠标右键后的展示的数据详细信息窗口
"""


class MyDetailDisplayWindow(QDialog, Ui_detailDialog):
    def __init__(self):
        super(MyDetailDisplayWindow, self).__init__()

        self.setupUi(self)
        self.retranslateUi(self)
        # 允许窗口最大最小化
        self.set_MinMax_window()

    def setLabelText(self, detail):
        self.hosttextBrowser.setText(detail[0])
        self.nametextBrowser.setText(detail[1])
        self.valuetextBrowser.setText(detail[2])
        self.pathtextBrowser.setText(detail[3])

    """
    设置最大化最小化窗口的按钮
    """

    def set_MinMax_window(self):
        flags = QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)


"""
关于我的界面
"""


class MyAboutDialog(QDialog, Ui_aboutDialog):
    def __init__(self):
        super(MyAboutDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("关于我")


"""
帮助界面
"""


class MyHelpDialog(QDialog, Ui_helpDialog):
    def __init__(self):
        super(MyHelpDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("帮助")
        self.pushButton.clicked.connect(self.onConfirmButton)

    def onConfirmButton(self):
        self.close()


class MySearchResultDialog(QDialog, Ui_searchResultDialog):
    def __init__(self):
        super(MySearchResultDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setWindowTitle("搜索结果")
        self.set_table()

        # 允许通过点击表头实现排序,self.flag是一个标记位，用来标记升降序重复的
        self.flag = True
        # 禁用自带排序
        self.tableWidget.setSortingEnabled(False)
        # 显示排序箭头
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.sortByColumns)

        self.set_MinMax_window()

        # 实例化一个子窗口
        self.detailDisplay = MyDetailDisplayWindow()

        # 允许产生右键菜单
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.right_menu)

    def sortByColumns(self, column):
        # flag为True的时候升序，flag设为False
        if self.flag:
            self.tableWidget.sortItems(column, QtCore.Qt.AscendingOrder)
            self.flag = False
        else:
            self.tableWidget.sortItems(column, QtCore.Qt.DescendingOrder)
            self.flag = True

    '''
    对tableWidget进行各种设置
    '''

    def set_table(self):
        # init the tableWidget row and column
        self.tableWidget.setColumnCount(4)
        # 设置表头标题
        self.tableWidget.setHorizontalHeaderLabels(['Host', 'Name', 'Value', 'Path'])
        # 设置表格铺满整个tableWidget控件
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置表格内容无法编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格默认选中的是整个单元格
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置表格列宽
        self.tableWidget.horizontalHeader().resizeSection(0, 120)
        self.tableWidget.horizontalHeader().resizeSection(1, 120)
        self.tableWidget.horizontalHeader().resizeSection(2, 120)
        self.tableWidget.horizontalHeader().resizeSection(3, 120)
        # 最后一列自适应宽度
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)

    """
    设置最大化最小化窗口的按钮
    """

    def set_MinMax_window(self):
        flags = QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)

    def right_menu(self):
        self.detailDisplay.close()
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        host = self.tableWidget.item(row_num, 0).text()
        name = self.tableWidget.item(row_num, 1).text()
        path = self.tableWidget.item(row_num, 3).text()
        value = self.tableWidget.item(row_num, 2).text()
        detail = [host, name, value, path]
        self.detailDisplay.setLabelText(detail)
        self.detailDisplay.setWindowTitle("详细信息")
        self.detailDisplay.show()


"""
当当网的cookie分析展示窗口
"""


class MyDangDangDialog(QDialog, Ui_dangdangDialog):
    def __init__(self):
        super(MyDangDangDialog, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.setTable()
        self.set_MinMax_window()

    """
    最大最小化窗口
    """

    def set_MinMax_window(self):
        flags = QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)

    """
    初始化表格，设置表格的内容，行高等等
    """

    def setTable(self):
        self.tableWidget.setColumnCount(2)
        # 设置表格铺满整个tableWidget控件
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置表格内容无法编辑
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格默认选中的是整个单元格
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 设置表头不显示
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setColumnWidth(0, 50)
        # 最后一列自适应宽度
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

    """
    将爬到的数据填表，第一列填写商品的主图，第二列填写商品的各种属性
    """

    def setRowData(self, browsingHistory):
        self.tableWidget.setRowCount(0)
        # browsingHistory = getWebContent.analysisPage()
        # 在浏览器上没有当当网的cookie数据，可能是没有在当当网上浏览过任何商品或者producthistoryid一项已经过期，抛出警示框

        if browsingHistory == []:
            QMessageBox.warning(self, '警告', '当前您的浏览器内没有浏览数据，请确认在当当网上浏览过商品', QMessageBox.Yes)
        # # 当网络异常请求不到数据时抛出信息提示框
        # elif browsingHistory[0] == "NETWORK_ERROR":
        #     QMessageBox.information(self, '提示', '当前网络出现异常，请检查网络连接后重试', QMessageBox.Yes)
        # 正常情况下分析当当网的cookie
        else:
            self.show()
            try:
                if browsingHistory == '':
                    QMessageBox.warning(self, '提示', 'cookie分析失败，请重试或者确认', QMessageBox.Yes)
                else:
                    startRow = 0
                    for i in range(len(browsingHistory)):
                        item = browsingHistory[i]
                        for j in range(1, len(item)):
                            row = self.tableWidget.rowCount()
                            self.tableWidget.insertRow(row)
                            tempItem = QTableWidgetItem(str(item[j]))
                            self.tableWidget.setItem(row, 1, tempItem)
                            if len(item) == 3:
                                self.tableWidget.setRowHeight(row, 100)
                            else:
                                self.tableWidget.setRowHeight(row, 50)

                        # 一个大的单元格的长度
                        length = len(item) - 1

                        # 合并单元格
                        self.tableWidget.setSpan(startRow, 0, length, 1)

                        # 插入爬到的图片，或者在网络链接不通畅的情况下只显示商品主图的链接
                        try:
                            imageLabel = QLabel()
                            res = requests.get(item[0])
                            imageLabel.setScaledContents(True)
                            imageLabel.setPixmap(QPixmap.fromImage(QImage.fromData(res.content)))
                            self.tableWidget.setCellWidget(startRow, 0, imageLabel)
                        # 当网络出现异常的时候，先弹出信息提示框，然后只把商品主图的链接插入表格中
                        except RequestException as e:
                            QMessageBox.information(self, '提示', str(e), QMessageBox.Yes)
                            picItem = QTableWidgetItem(str(item[0]))
                            self.tableWidget.setItem(startRow, 0, picItem)
                        startRow = startRow + length

                    self.tableWidget.resizeColumnsToContents()

            except Exception as e:
                print(e)
            return SUCCESS_CODE


class MyDangDangThread(QThread):
    signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        browsingHistory = getWebContent.analysisPage()
        self.signal.emit(browsingHistory)


class ChromeCookieThread(QThread):
    signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        items = extract_chrome_cookie.get_cookies_from_chrome()
        self.signal.emit(items)


class FireFoxCookieThread(QThread):
    signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        items = get_other_cookie.get_cookie_from_firefox()
        self.signal.emit(items)


"""
加载动画类，实现加载动画窗口
"""
import base64
from loading import img

class MyLoadingDialog(QDialog, Ui_loadingDialog):
    def __init__(self):
        super(MyLoadingDialog, self).__init__()
        self.setupUi(self)
        self.setFixedSize(200, 200)
        self.retranslateUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.loadGIF()

    def loadGIF(self):
        tmp = open('tmp.gif', 'wb+')  # 临时文件用来保存gif文件
        tmp.write(base64.b64decode(img))
        tmp.close()
        pic = QMovie('tmp.gif')
        # pic = QMovie('.\loading.gif')
        self.label.setMovie(pic)
        self.label.setScaledContents(True)
        pic.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

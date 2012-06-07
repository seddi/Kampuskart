# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'satis.ui'
#
# Created: Tue Jun  5 04:28:31 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QChar
import sys

import os, sys
sys.path.append(os.path.join('..','mysqldb'))
from database import *
from pay import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(709, 584)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Satış Ekranı", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 10, 651, 421))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(230, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Şirket Satış Noktası", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(230, 40, 171, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.comboBox = QtGui.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(110, 90, 171, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Ürün:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(310, 100, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Adet:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(370, 90, 71, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(466, 90, 61, 31))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Ekle", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(370, 370, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Tutar:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line_2 = QtGui.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(370, 380, 51, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(50, 110, 41, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(310, 110, 41, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Müşteri Bilgileri:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line_5 = QtGui.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(50, 170, 131, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(50, 200, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "İsim:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line_6 = QtGui.QFrame(self.frame)
        self.line_6.setGeometry(QtCore.QRect(50, 210, 41, 20))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(50, 250, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Soyisim:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.line_7 = QtGui.QFrame(self.frame)
        self.line_7.setGeometry(QtCore.QRect(50, 260, 61, 20))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(50, 300, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Ünvan:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.line_8 = QtGui.QFrame(self.frame)
        self.line_8.setGeometry(QtCore.QRect(50, 310, 51, 20))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.label_9 = QtGui.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(50, 350, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Mevcut Bakiye:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.line_9 = QtGui.QFrame(self.frame)
        self.line_9.setGeometry(QtCore.QRect(50, 360, 111, 20))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.frame)
        self.textBrowser_3.setGeometry(QtCore.QRect(180, 190, 151, 31))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_4 = QtGui.QTextBrowser(self.frame)
        self.textBrowser_4.setGeometry(QtCore.QRect(180, 240, 151, 31))
        self.textBrowser_4.setObjectName(_fromUtf8("textBrowser_4"))
        self.textBrowser_5 = QtGui.QTextBrowser(self.frame)
        self.textBrowser_5.setGeometry(QtCore.QRect(180, 290, 151, 31))
        self.textBrowser_5.setObjectName(_fromUtf8("textBrowser_5"))
        self.textBrowser_6 = QtGui.QTextBrowser(self.frame)
        self.textBrowser_6.setGeometry(QtCore.QRect(180, 340, 151, 31))
        self.textBrowser_6.setObjectName(_fromUtf8("textBrowser_6"))
        self.pushButton_6 = QtGui.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 90, 51, 31))
        self.pushButton_6.setText(QtGui.QApplication.translate("MainWindow", "Sil", None, QtGui.QApplication.UnicodeUTF8))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.textEdit = QtGui.QTextEdit(self.frame, readOnly=True)
        self.textEdit.setGeometry(QtCore.QRect(370, 140, 231, 201))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame, readOnly=True)
        self.lineEdit_2.setGeometry(QtCore.QRect(430, 360, 113, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 450, 101, 27))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "&Çıkış", None, QtGui.QApplication.UnicodeUTF8))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 450, 101, 27))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "&Yenile", None, QtGui.QApplication.UnicodeUTF8))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 450, 111, 27))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "&Ödeme Yap", None, QtGui.QApplication.UnicodeUTF8))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/pay.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(90, 490, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(500, 490, 91, 41))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pay = pay(self)
        self.priceList = dict()
        self.product = list()
        self.productNum = dict()

        for row in self.pay.products:
            self.comboBox.addItem(_fromUtf8(row[1]))
            self.priceList[_fromUtf8(row[1])] = row[2]
            self.priceList[row[0]] = _fromUtf8(row[1])

        self.pushButton.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.lineEdit.setText("1")
        self.lineEdit_2.setText("0")

        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pay.buy)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.click_buy)
        
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.click_refresh)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.userInfo)


        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.removeList)

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.addList)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

    def click_refresh(self):
        self.pushButton.setEnabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton_6.setDisabled(True)
    
    def click_buy(self):
        self.pushButton_4.setDisabled(True)
    
    def removeList(self):
        reload(sys)
        sys.setdefaultencoding("latin-1")
        total = 0
        self.textEdit.undo()
        delProduct = self.product.pop()
        del(self.productNum[delProduct])
        
        tmp = _fromUtf8(str(self.textEdit.toPlainText()))
        deleteRows = tmp.split('\n')
        for i in deleteRows:
            if i == '':
                total = 0
                self.pushButton_4.setDisabled(True)
                self.pushButton_6.setDisabled(True)
            else:
                b = i.split(' ')
                price = b[-2]
                units = b[-1]
                total += float(price)*int(units)

        if total <= self.result['bakiye']:
            self.label_10.clear()
            self.label_11.clear()

        self.lineEdit_2.setText(str(total))

    def addList(self):
        reload(sys)
        sys.setdefaultencoding("latin-1")
        
        self.pushButton_4.setEnabled(True)
        self.pushButton_6.setEnabled(True)

        selectedProduct = self.comboBox.currentText()
        self.product.append(selectedProduct)
        print self.product
        self.productNum[_fromUtf8(str(selectedProduct))] = int(self.lineEdit.text())
        
        total = float(self.lineEdit_2.text()) + self.priceList[selectedProduct]*int(self.lineEdit.text())

        if total > self.result['bakiye']:
            self.label_10.setText(_fromUtf8("Bakiyeniz Yetersiz."))
            error = QtGui.QPixmap("icons/error.png")
            self.label_11.setPixmap(error)

        else:
            self.textEdit.append(selectedProduct + " " + str(self.priceList[selectedProduct]) + " " + self.lineEdit.text())
            self.lineEdit_2.setText(str(total))
            self.label_10.setText(_fromUtf8("Kayıt Başarıyla Alındı."))
            success = QtGui.QPixmap("icons/ok.png")
            self.label_11.setPixmap(success)

    def userInfo(self):
        self.textEdit.clear()
        self.textBrowser_3.clear()
        self.textBrowser_4.clear()
        self.textBrowser_5.clear()
        self.textBrowser_6.clear()
        self.lineEdit.setText("1")
        self.lineEdit_2.setText("0")
        self.label_10.clear()
        self.label_11.clear()

        self.result = self.pay.fetch()
        if not len(self.result):
            self.label_10.setText(_fromUtf8("Kullanıcı Bulunamadı."))
            error = QtGui.QPixmap("icons/error.png")
            self.label_11.setPixmap(error)
            self.pushButton.setDisabled(True)
        else:
            if not self.result['aktif'] or not self.result['bakiye']:
                if not self.result['aktif']:
                    self.label_10.setText(_fromUtf8("Kart Aktif degil."))
                else:
                    self.label_10.setText(_fromUtf8("Mevcut Bakiyeniz Yetersiz."))
                error = QtGui.QPixmap("icons/error.png")
                self.label_11.setPixmap(error)
                self.pushButton.setDisabled(True)

            self.textBrowser_3.setText(_fromUtf8(self.result['isim']))
            self.textBrowser_4.setText(_fromUtf8(self.result['soyisim']))
            self.textBrowser_5.setText(_fromUtf8(self.result['unvan']))
            self.textBrowser_6.setText(_fromUtf8(str(self.result['bakiye'])))

app = QtGui.QApplication(sys.argv)
window = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())

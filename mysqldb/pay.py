#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os
import datetime

sys.path.append(os.path.join('..','card'))
from connectionCard import *

import MySQLdb
from sendmail import *
import random

from floatToHex import *
from keyLoadCard import *

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QChar

from smartcard.util import toHexString
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class pay:
    def __init__(self, ui):
        self.cn = MySQLdb.connect("mysql_server_ip","user","password","db_name")
        self.cn.set_character_set('utf8')
        self.cursor = self.cn.cursor()
        
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')

        self.companyName = "omkan"
        self.department = "muhendislik"

        self.cursor.execute("Select id from sirkets where isim = '%s'" %(self.companyName))
        self.company_id = self.cursor.fetchone()
       
        self.cursor.execute("Select id from subes where isim = '%s' and sirket_id = %d" %(self.department,self.company_id[0]))
        self.department_id = self.cursor.fetchone()

        self.cursor.execute("select id, isim, fiyat, adet from uruns where sirket_id = %d" %(self.company_id))
        self.products = self.cursor.fetchall()


        self.block = [0x03]  # 0. sektor trailer (keyA keyB ve acces bitlerin oldugu blok)
        self.keyA = [0x11, 0x11, 0x11, 0x11, 0x11, 0x11]
        self.keyB = [0x22, 0x22, 0x22, 0x22, 0x22, 0x22]
        self.defKey = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        
        self.keyType = "B"
        self.authKey = self.keyB
        self.accesCond = [0x5D, 0x27, 0x8A, 00] # byte-6 => 0x5D byte-7 => 0x27 byte-8 => 0x8A

        self.ui = ui
        self.errImg = QtGui.QPixmap("icons/error.png")
        self.successImg = QtGui.QPixmap("icons/ok.png")

    def fetch(self):
        try:
            result = dict()
            block= [0x01]
            result['bakiye'] = 0.0    # eger bakiye okuma basarisiz ise 0 bas
            card = sCard()
            cardtype = AnyCardType()
            timeout = 10
            card.cardConnect(timeout, cardtype)
            
            opr = Operation(card.target_num, card.UID, self.keyType, self.block, card.cardservice)
            err, sw1, sw2 = opr.authenticate(self.authKey)

            if sw1 == 0x90 and not err:
                data = opr.read(block)
                err = data[0]
                if not err:
                    bakiye = hex2float(data[1:5])
                    result['bakiye'] = bakiye
                else:
                    self.ui.label_10.setText(_fromUtf8("Mevcut Bakiye okuma basarisiz..."))
                    self.ui.label_11.setPixmap(self.errImg)
            else:
                self.ui.label_10.setText(_fromUtf8("Authenticate basarısız..."))
                self.ui.label_11.setPixmap(self.errImg)
            
            self.cursor.execute("select id, user_id, aktif from cards where kartid ='%s'"%(toHexString(card.UID)))
            card_id, user_id, aktif = self.cursor.fetchone()

            self.cursor.execute("select isim, soyisim, unvan from users where id = %d"%(user_id))
            isim, soyisim, unvan = self.cursor.fetchone()
            self.cn.commit()

            result['isim'] = isim
            result['soyisim'] = soyisim
            result['unvan'] = unvan
            result['UID'] = str(toHexString(card.UID))
            result['userid'] = user_id
            result['cardid'] = card_id
            result['aktif'] = aktif

            card.disConnect()
            return result
        except:
            card.disConnect()
            return {}
         
    def buy(self, block = [0x01]):
        
        sube_id = self.department_id[0]
        
        card = sCard()
        cardtype = AnyCardType()
        timeout = 10
        card.cardConnect(timeout, cardtype)
        
        self.cursor.execute("select id from cards where kartid ='%s'" %(toHexString(card.UID))) 
        card_id = self.cursor.fetchone()
        card_id = card_id[0]
        
        opr = Operation(card.target_num, card.UID, self.keyType, block, card.cardservice)
        try:
            err, sw1, sw2 = opr.authenticate(self.authKey)

            if sw1 == 0x90 and not err:
                cashFloat = float(self.ui.lineEdit_2.text())
                cashHex = float2hex(cashFloat)
                err, sw1 = opr.decrement(block, cashHex)

                if sw1 == 0x90 and not err:
                    err, sw1 = opr.transfer(block)
                    if sw1 == 0x90 and not err:
                        self.cursor.execute("update cards set bakiye = '%.2f' where kartid='%s'"\
                                            %((self.ui.result['bakiye'] - cashFloat), toHexString(card.UID)))
                        

                        for product in self.ui.product:
                            print "Urun Adı: ", product
                            self.cursor.execute("select id from uruns where isim ='%s'" %(product))
                            urun_id = self.cursor.fetchone()
                            urun_id = urun_id[0]
                            print "urun_id : ", urun_id
                            
                            numeral = self.ui.productNum[product]
                            price = self.ui.priceList[product]
                            totalPay = float(numeral*price)
                            
                            self.cursor.execute("insert into harcamas (zaman, adet, card_id, sube_id, urun_id, tutar)\
                                                    values('%s', %d, %d, %d, %d, %.2f)"%(datetime.datetime.now(),\
                                                    numeral , card_id, sube_id, urun_id, totalPay))
                            self.cn.commit()

                        self.ui.label_10.setText(_fromUtf8("Odeme islemi basarılı..."))
                        self.ui.label_11.setPixmap(self.successImg)
                    else:
                        self.ui.label_10.setText(_fromUtf8("Bakiye transfer islemi basarısız..."))
                        self.ui.label_11.setPixmap(self.errImg)
                else:
                    self.ui.label_10.setText(_fromUtf8("Bakiye azaltma islemi basarısız..."))
                    self.ui.label_11.setPixmap(self.errImg)
            else:
                self.ui.label_10.setText(_fromUtf8("Authenticate islemi basarısız..."))
                self.ui.label_11.setPixmap(self.errImg)

            card.disConnect()
        except:
            self.ui.label_10.setText(_fromUtf8("Odeme islemi basarısız..."))
            self.ui.label_11.setPixmap(self.errImg)

    def dbclose(self):
        self.cn.close()

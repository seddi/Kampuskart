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


class database:
    def __init__(self, ui):
        self.cn = MySQLdb.connect("mysql_server_ip","user","password","db_name")
        self.cn.set_character_set('utf8')
        self.cursor = self.cn.cursor()
        
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection = utf8;')
        self.block = [0x03]  # 0. sektor trailer (keyA keyB ve acces bitlerin oldugu blok)
        self.keyA = [0x11, 0x11, 0x11, 0x11, 0x11, 0x11]
        self.keyB = [0x22, 0x22, 0x22, 0x22, 0x22, 0x22]
        self.defKey = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
        self.defkeyType = "A"  # smart card default key type
        
        self.loadCenter = "Muhendislik" # belirlenen yukleme noktası ismi

        self.keyType = "B"  # yeni olusturulan key icin key type'i
        self.authKey = self.keyB # yeni olusturulan yetkilendirme anahtarı ile authenticate yapmak icin kullanılıyor
        
        self.accesCond = [0x5D, 0x27, 0x8A, 00] # byte-6 => 0x5D byte-7 => 0x27 byte-8 => 0x8A

        self.ui = ui
        self.errImg = QtGui.QPixmap("icons/error.png")

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
                    self.ui.label_7.setText(_fromUtf8("Mevcut Bakiye okuma basarisiz..."))
                    self.ui.label_8.setPixmap(self.errImg)
            else:
                self.ui.label_7.setText(_fromUtf8("Authenticate basarısız..."))
                self.ui.label_8.setPixmap(self.errImg)
            
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
            return result
        except:
            return {}
         
    def insert_user(self):
        user_data = {}
        _fromUtf8 = QtCore.QString.fromUtf8
        user_data['isim'] = self.ui.lineEdit.text()
        user_data['soyisim'] = self.ui.lineEdit_2.text()
        user_data['tc'] = self.ui.lineEdit_3.text()
        user_data['number'] = self.ui.lineEdit_4.text()
        user_data['email'] = self.ui.lineEdit_5.text()
        user_data['telefon'] = self.ui.lineEdit_6.text()
        user_data['password'] = random.randint(1000000, 9999999)
        user_data['dogumgunu'] = self.ui.dateEdit.date().toPyDate()
        user_data['unvan'] = self.ui.comboBox.currentText()
        user_data['gecici'] = 1

        sql = "insert into users(number, tc, isim, soyisim, email, telefon, \
                password, dogumgunu, unvan, gecici) values('%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%d')" \
                %(user_data['number'],user_data['tc'],user_data['isim'],user_data['soyisim'],user_data['email'], \
                                    user_data['telefon'],user_data['password'],user_data['dogumgunu'],user_data['unvan'],user_data['gecici'])
        self.cursor.execute(sql)

        self.add_user_card(user_data) # ilk kart kaydı
        self.cn.commit()
        
        msg = "Merhaba, " + str(user_data['isim']) + str(user_data['soyisim']) + " Gecici sifreniz : " + str(user_data['password'])
        send_email(msg, str(user_data['email']))
    	
        self.ui.label_9.setText(_fromUtf8("Kayıt Başarıyla Alındı."))
        success = QtGui.QPixmap("icons/ok.png")
        self.ui.label_10.setPixmap(success)

    def add_user_card(self, user_data):
        bakiye = 0
        aktif = 1
        card = sCard()
        cardtype = AnyCardType()
        timeout = 10
        card.cardConnect(timeout, cardtype)
        sql_id = "select id from users  where tc = %s" %(user_data['tc'])
        self.cursor.execute(sql_id)
        userid = self.cursor.fetchone()

        sql = "insert into cards(kartid, aktif, user_id, bakiye) values('%s', '%d', '%d', '%.2f')" %(toHexString(card.UID), aktif, userid[0], bakiye)
        self.cursor.execute(sql)

        authKeyLoad(self.defKey, self.defkeyType, self.keyA, self.accesCond, self.keyB, self.block)

    def cashLoad(self, authKey = None, keyType = "B", block = [0x01]):
        authKey = self.keyB
        card = sCard()
        cardtype = AnyCardType()
        timeout = 10 
        card.cardConnect(timeout, cardtype)
        opr = Operation(card.target_num, card.UID, keyType, block, card.cardservice)
        err, sw1, sw2 = opr.authenticate(authKey)
        
        if sw1 == 0x90 and not err:
            cashFloat = float(self.ui.lineEdit.text())
            cashHex = float2hex(cashFloat)
            err, sw1 = opr.increment(block, cashHex)
            
            if sw1 == 0x90 and not err:
                err, sw1 = opr.transfer(block)
                if sw1 == 0x90 and not err:
                    self.cursor.execute("update cards set bakiye = '%.2f' where kartid='%s'"\
                            %((cashFloat + self.ui.result['bakiye']), toHexString(card.UID)))

                    self.cursor.execute("insert into yuklemes(card_id, kartid, miktar, created_at, updated_at, yer)\
                                        values(%d, '%s', %.2f, '%s', '%s', '%s')"\
                                        %(self.ui.result['cardid'], toHexString(card.UID), cashFloat, datetime.datetime.now(),\
                                        datetime.datetime.now(), self.loadCenter))
                    self.cn.commit()

                    self.ui.label_7.setText(_fromUtf8("Transfer islemi basarılı..."))
                    success = QtGui.QPixmap("icons/ok.png")
                    self.ui.label_8.setPixmap(success)
                else:
                    self.ui.label_7.setText(_fromUtf8("Transfer islemi basarısız..."))
                    self.ui.label_8.setPixmap(self.errImg)
            else:
                self.ui.label_7.setText(_fromUtf8("Ekleme islemi basarısız..."))
                self.ui.label_8.setPixmap(self.errImg)
        else:
            self.ui.label_7.setText(_fromUtf8("Authenticate basarısız..."))
            self.ui.label_8.setPixmap(self.errImg)
    
    def cashLoadBack(self, authKey = None, keyType = "B", block = [0x01]):
        authKey = self.keyB
        card = sCard()
        cardtype = AnyCardType()
        timeout = 10 
        card.cardConnect(timeout, cardtype)
        try:
            self.cursor.execute("select miktar, id from yuklemes where kartid ='%s' order by updated_at desc limit 1"%(toHexString(card.UID)))
            self.cn.commit()
            miktar, yukleme_id = self.cursor.fetchone()
            opr = Operation(card.target_num, card.UID, keyType, block, card.cardservice)
            err, sw1, sw2 = opr.authenticate(authKey) 
            
            if sw1 == 0x90 and not err:
                cash = float2hex(miktar)
                err, sw1 = opr.decrement(block, cash)
                if sw1 == 0x90 and not err:
                    err, sw1 = opr.transfer(block)
                    if sw1 == 0x90 and not err:
                        data = opr.read(block)
                        err = data[0]
                        if not err:
                            self.cursor.execute("delete from yuklemes where id ='%s'"%(yukleme_id))
                            self.cursor.execute("update cards set bakiye=%.2f where kartid='%s'"%(hex2float(data[1:5]),toHexString(card.UID)))
                            self.cn.commit()
                            
                            self.ui.label_7.setText(_fromUtf8("Son yukleme geri alındı"))
                            success = QtGui.QPixmap("icons/ok.png")
                            self.ui.label_8.setPixmap(success)
                        else:
                            self.ui.label_7.setText(_fromUtf8("Kart Bakiyesi okunamadi.."))
                            self.ui.label_8.setPixmap(self.errImg)
                    else:
                        self.ui.label_7.setText(_fromUtf8("Geri alma islemi basarısız..."))
                        self.ui.label_8.setPixmap(self.errImg)
                else:
                    self.ui.label_7.setText(_fromUtf8("Azaltma islemi basarısız..."))
                    self.ui.label_8.setPixmap(self.errImg)
            else:
                self.ui.label_7.setText(_fromUtf8("Authenticate basarısız..."))
                self.ui.label_8.setPixmap(self.errImg)
        except:
            self.ui.label_7.setText(_fromUtf8("Geri Alınacak Bakiye Yok."))
            self.ui.label_8.setPixmap(self.errImg)
    
    def dbclose(self):
        self.cn.close()

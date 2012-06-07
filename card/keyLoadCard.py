#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
from connectionCard import *
from Operations import *

def authKeyLoad(authKey, keyType, keyA, accesBit, keyB, block):
    value_block = [0x01]
    value = [0x00, 0x00, 0x00, 0x00]   # ilk kayıtta decimal = 00 yuklemek istedigin decimal deger
    value_data = value + [value[0]^0xFF, value[1]^0xFF, value[2]^0xFF, value[3]^0xFF] + value + value_block + [value_block[0]^0xFF] + value_block + [value_block[0]^0xFF]

    key_data = keyA + accesBit + keyB
    card = sCard()
    cardtype = AnyCardType()
    timeout = 10
    card.cardConnect(timeout, cardtype)

    opr = Operation(card.target_num, card.UID, keyType, block, card.cardservice)
    result = opr.authenticate(authKey)
    if not result[0]:
        response = opr.write(value_block, value_data)
        err = response[0]
        sw1 = response[1]
        if not err and sw1 == 0x90:
            print "Bakiye"  + str(value) + " ile ilklendirildi..."
        else:
            print "Error : " + str(err) +  "ilk bakiye yuklenemedi... "
            sys.exit()
        
        response = opr.write(block, key_data)
        err = response[0]
        sw1 = response[1]
        if not err and sw1 == 0x90:
            print "Key Load succesfull..."
        else:
            print "Error : " + str(err)  + "Key is not load... "
            sys.exit()
    else:
        print "Error : " + str(result[0]) +  "Authenticate yapılamadı.."
        sys.exit()


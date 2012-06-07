#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
from Operations import *
from getTag import *
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.Exceptions import CardRequestTimeoutException

if __name__ == "__main__":
    if sys.platform == "linux2":
        try:
            block = [0x02]
            bindata = [0xA0, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, \
                    0x08, 0x09, 0x0A ,0x0B, 0x0C, 0x0D, 0x0E, 0x0F]
            value = [0x01, 0x00, 0x00, 0x00]   # decimal = 100 yuklemek istedigin decimal deger
            valdata = value + [value[0]^0xFF, value[1]^0xFF, value[2]^0xFF, value[3]^0xFF] + \
                        value + block + [block[0]^0xFF] + block + [block[0]^0xFF]
            
            card = sCard()
            cardtype = AnyCardType()
            timeout = 10
            card.cardConnect(timeout, cardtype)
            print "dogru : UID : ", card.UID, "Target num : ", card.target_num, "Tag Type : ", card.tagType

            opr = Operation(card.target_num, card.UID, "A", [0x03], card.cardservice)
            result = opr.authenticate()
            print " Authenticate sonucu :  ", result
##########################################################
######### Write, Increment and Decrement block ############
###########################################################
           result = opr.write(block, bindata)
            if not result:          # Result 0 ise basarılı
                print "Write operation is succesfull..."
            else:
                print "Error code : ", result
            card.cardservice.connection.disconnect()
            sys.exit()
        except AttributeError, e: 
            print "%s" %(e)
            sys.exit()
    else:
        print "Isletim sistemi uyumsuz..."
        print "Uygun sistem linux"

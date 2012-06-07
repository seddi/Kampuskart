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
            block = [0x01]
            card = sCard()
            cardtype = AnyCardType()
            timeout = 10
            card.cardConnect(timeout, cardtype)
            print "dogru : UID : ", card.UID, "Target num : ", card.target_num, "Tag Type : ", card.tagType

##########################################################
############# Authenticate and read block ################
##########################################################
            opr = Operation(card.target_num, card.UID, "A", [0x03], card.cardservice)
            result = opr.authenticate()
            print " Authenticate sonucu :  ", result
            if result[0] == 0x00:
                data = opr.read(block)
                if data[0] == 0x00:
                    print "Okunan veri : ", data[1:]
                else:
                    print "Okuma Hata kodu : ", data[0], "sw1 : ", data[1]
            else:
                print " Authenticate yapılamadı "
                sys.exit()
            card.cardservice.connection.disconnect()
            sys.exit()
        except AttributeError, e: 
            print "%s" %(e)
            sys.exit()
    else:
        print "Isletim sistemi uyumsuz..."
        print "Uygun sistem linux"

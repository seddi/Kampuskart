#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.Exceptions import CardRequestTimeoutException

class sCard:
    std_command = [0xFF,0x00,0x00,0x00]
    def __init__(self):
        self.get_tag_apdu = self.std_command + [0x04,0xD4,0x4A,0x01,0x00]
        self.UID = None
        self.target_num = None
        self.tagType = None    # Mifare 1k gibi
        self.cardservice = None

    def cardConnect(self, time = 10, cardtype = None):
        try:
            # request card insertion
            print 'insert a card (SIM card if possible) within 10s'
            cardrequest = CardRequest(timeout = time, cardType = cardtype)
            self.cardservice = cardrequest.waitforcard()

            # attach the console tracer
            observer = ConsoleCardConnectionObserver()
            self.cardservice.connection.addObserver(observer)

            # connect to the card and perform a few transmits
            self.cardservice.connection.connect()
            response, sw1, sw2 = self.cardservice.connection.transmit(self.get_tag_apdu)
            if sw1 == 0x90:
                self.get_tag(response)
            else :
                print "Get Tag Apdu transmit işlemi basarısız"
                sys.exit()
        except CardRequestTimeoutException:
            print 'time-out: no card inserted during last 10s'
    
    def disConnect(self):
        self.cardservice.connection.disconnect()

    def get_tag(self, response):
        number_of_tag_found = response[2]       # bulunan tag sayisi
        if number_of_tag_found:                 # bulunan tag sayisi 0 dan farkli mi?
            print 'Number of tag found : ', number_of_tag_found
            length_UID = response[7]            # UID uzunlugu
            self.UID = response[8:8 + length_UID]      # kart id
            self.target_num = [response[3]]
            self.tagType = response[6]              # tag tipi mifare 1k gibi
            
            if self.tagType == 0x08:
                print "Mifare 1k ..."
            else:
                print "Tanınmayan kart tipi. Mifare 1k tipinde bir kart olmalı..."
                sys.exit()
        else:
            print 'Tag bulunmadi...'
            sys.exit()

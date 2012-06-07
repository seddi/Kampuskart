#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.Exceptions import CardRequestTimeoutException

class Operation:
    readCommand = [0x30]
    writeCommand = [0xA0]           # write command
    incCommand = [0xC1]             # value block isleminde increment islemi oldugunu gosteren deger
    decCommand = [0xC0]             # value block isleminde decrement islemi oldugunu gosteren deger
    transCommand = [0xB0]           # onceki decrement veya increment hesaplanan degeri ilgili blok a aktar
    restCommand = [0xC2]            # onceki decrement veya increment hesaplanan islemi iptal et

    authTypeA = [0x60]      # Authentication with key A
    authTypeB = [0x61]      # Authentication with key B
    defKey = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
    std_command = [0xFF, 0x00, 0x00, 0x00]

    def __init__(self, target_num, UID, keyType, block, cardservice):
        self.target_num = target_num
        self.block = block
        self.UID = UID
        if (keyType == "A"):              # keyA ile authenticate yapılıyor ise
            self.authType = self.authTypeA
        else:
            self.authType = self.authTypeB
        self.card = cardservice
    
    def authenticate(self, authKey = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]):
        Apdu = self.std_command + [0x0F, 0xD4, 0x40] + self.target_num + self.authType + self.block + authKey + self.UID
        response, sw1, sw2 = self.card.connection.transmit(Apdu)
        error_code = response[2]  # Return 0x00 if Authenticate is succesfull
        return [error_code, sw1, sw2]
    
    def read(self, block):
        apdu = self.std_command + [0x05, 0xD4, 0x40] + self.target_num + self.readCommand + block
        response, sw1, sw2 = self.card.connection.transmit(apdu)
        error_code = response[2] # Return 0x00 if Read is succesfull
        if sw1 == 0x90:
            data = response[2:]  # data[0] = response[2] error code eger 0x00 ise okuma basarılı
            return data
        else:
            return [error_code]
    
    def write(self, block, data): 
        apdu = self.std_command + [0x15, 0xD4, 0x40] + self.target_num + self.writeCommand + block + data
        response, sw1, sw2 = self.card.connection.transmit(apdu)
        error_code = response[2]    # Return 0x00 if write is succesfull
        return [error_code, sw1]                # Write operation is succesfull if return 0x00

#####################################################
########## VALUE BLOCK OPERATİONS ###################
#####################################################

    def increment(self, block, incValue):
        apdu = self.std_command + [0x09, 0xD4, 0x40] + self.target_num + self.incCommand + block + incValue  # increment value block
        response, sw1, sw2 = self.card.connection.transmit(apdu)
        error_code = response[2]
        return [error_code, sw1]                # Increment operation is succesfull...

    def decrement(self, block, decValue):
        apdu = self.std_command + [0x09, 0xD4, 0x40] + self.target_num + self.decCommand + block + decValue  # decrement value block
        response, sw1, sw2 = self.card.connection.transmit(apdu)
        error_code = response[2]
        return [error_code, sw1]                # Decrement is succesfull

    # Onceki islemin sonucunu karta aktar
    def transfer(self, block):
        apdu = self.std_command + [0x05, 0xD4, 0x40] + self.target_num + self.transCommand + block
        response, sw1, sw2 = self.card.connection.transmit(apdu)
        error_code = response[2]
        return [error_code, sw1]                # Transfer operation is succesfull...

    # Onceki islemi iptal et
    def restore(self, block):
        apdu = self.std_command + [0x05, 0xD4, 0x40] + self.target_num + self.restCommand + block
        response, sw1, sw2 = self.card.connection.transmit(apdu)
        error_code = response[2]
        return [error_code, sw1]                # Restore operation is succesfull...

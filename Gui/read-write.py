import sys
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.Exceptions import CardRequestTimeoutException

cardtype = AnyCardType()

get_tag_apdu = [0xFF,0x00,0x00,0x00,0x04,0xD4,0x4A,0x01,0x00]

read_block_num = [0x01]      # okunacak olan block numarasi
write_block_num = [0x03]
auth_block_num = [0x03]      # authenticate yapilacak olan block numarasi (ayni sektor icinde )

write = [0xA0] 
read = [0x30]                # read command

key_typeA = [0x60]
key_typeB = [0x61]

def_key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

acces = [0xFF, 0x07, 0x80, 0x00] # default acces bitlerinin byte 6 byte 7 ve byte 8 hali ve 0x00 byte 9(kullanilmiyor)
keyA =  [0x11, 0x11, 0x11, 0x11, 0x11, 0x11] # ilk yetki key'i
keyB =  [0x22, 0x22, 0x22, 0x22, 0x22, 0x22] # ilk yetki key'i

auth_key = keyB
auth_type = key_typeB
data = def_key + acces + def_key
try:
    # request card insertion
    print 'insert a card (SIM card if possible) within 10s'
    cardrequest = CardRequest(timeout = 10, cardType=cardtype)
    cardservice = cardrequest.waitforcard()

    # attach the console tracer
    observer = ConsoleCardConnectionObserver()
    cardservice.connection.addObserver(observer)

    # connect to the card and perform a few transmits
    cardservice.connection.connect()
    response, sw1, sw2 = cardservice.connection.transmit(get_tag_apdu)

    print 'response : ', response
    print "get tag islemi...  sw1 deger : %d, sw2 deger : %d"%(sw1, sw2)

    number_of_tag_found = response[2]       # bulunan tag sayisi
    if number_of_tag_found:                 # bulunan tag sayisi 0 dan farkli mi?
        print 'Number of tag found : ', number_of_tag_found
        length_UID = response[7]            # UID uzunlugu
        UID = response[8:8+length_UID]      # kart id
        target_num = [response[3]]
        sel_res = response[6]               # tag tipi mifare 1k gibi
    else:
        print 'Tag bulunmadi...'
        sys.exit()

    read_apdu = [0xFF, 0x00, 0x00, 0x00, 0x05, 0xD4, 0x40] + target_num + read + read_block_num
    write_apdu = [0xFF, 0x00, 0x00, 0x00, 0x15, 0xD4, 0x40] + target_num + write + write_block_num + data
    
    auth_apdu = [0xFF, 0x00, 0x00, 0x00, 0x0F, 0xD4, 0x40] + target_num + auth_type + auth_block_num + auth_key + UID[-4:] # key A ile authenticate yapmak icin, response[8:12] 4 bytelik UID get_tag apdusunun ciktisi

    response, sw1, sw2 = cardservice.connection.transmit(auth_apdu)
    error_code = response[2] # eger authenticate yapilirsa 0x00 olmazsa hata kodu doner	

    if sw1 == 0x90:
        if not error_code:
            print 'Authenticate Yapildi...'
            response, sw1, sw2 = cardservice.connection.transmit(write_apdu)
            error_code = response[2]          # islem basarili ise 0x00
            if sw1 == 0x90 and not error_code:
                data = response[3:]           # okunan veri"
                print 'Okuma basarili...'
                print 'Okunan veri : ', data, ' sw1 : ', sw1, ' sw2 : ', sw2
            else:
                print response
                print 'Okuma yapilamadi..!!'
        else:
            print 'Authenticate error code : ', error_code
    else:
        print 'Authenticate hatasi...'

except CardRequestTimeoutException:
    print 'time-out: no card inserted during last 10s'

except:
    import sys
    print sys.exc_info()[1]

import sys
if 'linux2' == sys.platform:
    print 'press Enter to continue'
    sys.stdin.read(1)

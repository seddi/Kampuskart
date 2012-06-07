#!/usr/bin/python
#-*- conding:utf-8 -*-

def float2hex(num):
    factor = 100
    numByte = 256
    hexArray = []
    num = int(num*factor)
    hexArray.insert(0, num/(numByte**3))
    tmp = num%(numByte**3)
    hexArray.insert(0, tmp/(numByte**2))
    tmp = tmp%(numByte**2)
    hexArray.insert(0, tmp/numByte)
    tmp = tmp%numByte
    hexArray.insert(0, tmp)
    print hexArray
    return hexArray

def hex2float(hexArray):
    k = 0
    numByte = 256
    num = 0
    for i in hexArray:
        num = num + int(i)*(numByte**k)
        k += 1
    print num/100.0
    return num/100.0

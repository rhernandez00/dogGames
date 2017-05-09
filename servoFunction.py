# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:56:10 2017

@author: Raul
"""

import serial
import serial.tools.list_ports
import time

#
nPelletsMax = 13
nTubes = 4

tube = 1
nPelletsGiven = 0
tubesCord = [106,83,58,36]
rotTube = tubesCord[0]
outCord = 132


ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "CH340" in p[1]:
        strTmp = str(p)
        strTmp = strTmp[0:5]
        strTmp = strTmp.replace('COM','')
        nPort = 'com' + strTmp
        
data = serial.Serial('com8',9600,timeout=1)   
#time.sleep(1)
#data.write(str(rotTube))


def reward():
    #global nPelletsGiven
    #global rotTube
    #global tube
    #data.write(str(outCord))
    data.write(str(99))
#    nPelletsGiven += 1
#    if nPelletsGiven >= nPelletsMax:
#        nPelletsGiven = 1
#        tube += 1
#        if tube > 4:
#            tube = 1
#        rotTube = tubesCord[tube-1]
#    print 'tubo: ' + str(rotTube)
#    print 'pellets: ' + str(nPelletsGiven)
#    time.sleep(2)
#    data.write(str(rotTube))
        
time.sleep(2)    
data.write(str(rotTube))
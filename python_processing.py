# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:28:00 2019

@author: User
"""

import serial

ser = serial.Serial('/dev/ttyACM0',9600)

s = [0]

while True:
	read_serial=ser.readline()

	print(read_serial)
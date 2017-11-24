#!/usr/bin/python
import serial
import time
from curses import ascii
import sys
import subprocess
import os
import time


def sendSMS(number,text):
	ser = serial.Serial('/dev/ttyUSB0',460800,timeout=1)
	ser.write("AT\r\n")
	time.sleep(1)

	ser.write("AT+CMGF=1\r\n")
	time.sleep(1)

	ser.write('AT+CMGS="%s"\r\n' %number)
	ser.write(text)
	ser.write(ascii.ctrl('z'))
	time.sleep(3)
	ser.close()
	return


if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "Zla ilosc argumentow!"
		print "sendsms.py <numer telefonu> <wiadomosc>"
		sys.exit(-1)
	phoneNumber = sys.argv[1]
	smsText = sys.argv[2]
	sendSMS(phoneNumber, smsText)

#!/usr/bin/env python3
#----------------------------------------------------------------
#	Note:
#	Save it as seconds since epoch and convert it when accessing it (makes the file unreadable manually but makes it more flexible and saves memory)
#----------------------------------------------------------------
#ENHANCE create an automatic backup at 2 in the morning to allow the programm to continue while I analyse the data
import os
import time

ds18b20 = ''

def setup():
	global ds18b20
	for i in os.listdir('/sys/bus/w1/devices'):
		if i != 'w1_bus_master1':
			ds18b20 = '28-01204bd1256e'

def read():
#	global ds18b20
	location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
	with  open(location) as tfile:
		text = tfile.read()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = temperaturedata[2:]
#	temperature = temperature / 1000 # 1000? this seems rather strange. I would expect a base 2 value.
	return temperature
	
def loop():
	global temperaturelist
	for i in range(5): #while True
		if read() != None:
			temperaturelist.append([int(time.time()), read()])
		time.sleep(1) #300 measure every 5 minutes

if __name__ == '__main__':
	try:
		temperaturelist = []
		setup()
		temperaturelist.append(["Epoch-Time", "Temperature * 1000"])
		loop()
	finally:
		#safe to file?
		pass

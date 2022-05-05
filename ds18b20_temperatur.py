#!/usr/bin/env python3
#----------------------------------------------------------------
#	Note:
#	Save it as seconds since epoch and convert it when accessing it (makes the file unreadable manually but makes it more flexible and saves memory)
#----------------------------------------------------------------
# BUG the last comma is wrong
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
	tfile = open(location)
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
#	temperature = float(temperaturedata[2:])
#	temperature = temperature / 1000
	return temperature
	
def loop():
	for i in range(10):
		if read() != None:
			print ("{", f'"time_epoch": {time.time()}, "temperature": %0.0f' % read(), "},")

def destroy():
	pass

if __name__ == '__main__':
	try:
		setup()
		print('{"temperatur": [')
		loop()
		print ("{", f'"time_epoch": {time.time()}, "temperature": %0.0f' % read(), "}") #workaround to avoid the last comma
		print("]}")
	except KeyboardInterrupt:
		destroy()

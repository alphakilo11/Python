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
	for i in range(1):
		if read() != None:
			print ("{", f'"time_epoch": {time.time()}, "temperature":', read(), "},")
#		time.sleep(300) # measure every 5 minutes

def destroy():
	pass

if __name__ == '__main__':
	try:
		temperaturelist = []
		setup()
		print('{"temperatur": [')
		loop()
		print ("{", f'"time_epoch": {int(time.time())}, "temperature":', read(), "}") #workaround to avoid the last comma
		print("]}")
	except KeyboardInterrupt:
		destroy()

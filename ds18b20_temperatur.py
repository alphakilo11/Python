#!/usr/bin/env python3
#----------------------------------------------------------------
#	Note:
#	Save it as seconds since epoch and convert it when accessing it (makes the file unreadable manually but makes it more flexible and saves memory)
#----------------------------------------------------------------
import os
import time

progress_update = True # print every measurement to CLI
time_between_measurements = 300 # s
ds18b20 = ''

def read():
	location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
	with  open(location) as tfile:
		text = tfile.read()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = temperaturedata[2:]
#	temperature = temperature / 1000 # 1000? this seems rather strange. I would expect a base 2 value.
	return temperature

if __name__ == '__main__':
	try:
		temperaturelist = []
		next_save_day = time.gmtime(time.time() + 3600 * 24)[2]
		# setup
		for i in os.listdir('/sys/bus/w1/devices'):
			if i != 'w1_bus_master1':
				ds18b20 = '28-01204bd1256e'
				
		temperaturelist.append(["Epoch-Time", "Temperature * 1000"])

		while True:
			if read() != None:
				step = [int(time.time()), read()]
				temperaturelist.append(step)
				if progress_update:
					print(step, "next in", time_between_measurements, "s.")
			now = time.localtime(time.time())
			if now[2] == next_save_day and now[3] >= 2: #triggers once a day after 2 o'clock 
				filename = str(now[0]) + str(now[1]) + str(now[2]) + "_temperatures.txt"
				with open(filename, "w") as file:
					file.write(str(temperaturelist))
				temperaturelist = []
				next_save_day = time.localtime(time.time() + 3600 * 24)[2]
				print("Successfully saved to", filename, "Next save on", next_save_day,".")
				del filename, now

			time.sleep(time_between_measurements) 
	finally:
		now = time.localtime(time.time())
		filename = str(now[0]) + str(now[1]) + str(now[2]) + "_temperatures.txt"
		with open(filename, "w") as file:
			file.write(str(temperaturelist))
		print("Successfully saved to", filename, ". Program terminated.")


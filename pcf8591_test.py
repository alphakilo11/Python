# BUG it looks like A0 only knows 0, 256 and 512 as measured values
import time
import board
import random

import adafruit_pcf8591.pcf8591 as PCF
from adafruit_pcf8591.analog_in import AnalogIn
from adafruit_pcf8591.analog_out import AnalogOut

############# AnalogOut & AnalogIn Example ##########################
#
# This example shows how to use the included AnalogIn and AnalogOut
# classes to set the internal DAC to output a voltage and then measure
# it with the first ADC channel.
#
# Wiring:
# Connect the DAC output to the first ADC channel, in addition to the
# normal power and I2C connections
#
#####################################################################
i2c = board.I2C()
pcf = PCF.PCF8591(i2c)

pcf_in_0 = AnalogIn(pcf, PCF.A1)
pcf_out = AnalogOut(pcf, PCF.OUT)

while True:

#    print("Setting out to ", 65535)
    pcf_out.value = 65535 #random.randint(1, 65535) 
    raw_value = pcf_in_0.value
    if raw_value == 256 or raw_value == 0:
        continue
    scaled_value = (raw_value / 65535) * pcf_in_0.reference_voltage
#    print(raw_value)
#    print("Pin 0: %0.2fV" % (scaled_value))
#    print("")
    time.sleep(0.01)
    pcf_out.value = 0
    time.sleep(0.01)

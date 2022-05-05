#!/usr/bin/env python3
import smbus
import time
import random
bus = smbus.SMBus(1)
adresse = 0x48

def read(control):
    write = bus.write_byte_data(adresse, control, 0)
    read = bus.read_byte(adresse)
    return read

def set (a_wert):
    write = bus.write_byte_data(adresse, 0x40, a_wert) # AOUT

while True:
    for i in range(60):
        set(random.randint(1, 255))
        time.sleep(1)

    power = input("Welchen Wert wollen Sie setzen (1 - 255):")
    if power == "q":
        break;
    power = int(power)
    set(power)
    print("Power Set:", power / 2.55, " %")
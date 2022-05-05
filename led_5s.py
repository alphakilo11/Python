#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
try:
    start = time.time();
    iterations = 5
    for i in range(round(iterations)):
        GPIO.output(37, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(37, GPIO.LOW)
        time.sleep(5)
        

    duration = time.time() - start
    print(f"Finished in {duration} s. Average Frequency: {iterations / duration} Hz.")

finally:
    GPIO.cleanup()
    print("\nprogram manually terminated")
